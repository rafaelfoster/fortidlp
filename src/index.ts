import fs from 'node:fs/promises';
import path from 'node:path';
import { Buffer } from 'node:buffer';
import manifest from './generated-manifest.json' with { type: 'json' };

export const version = '1.0';
export interface ApiSuccess<T = unknown> { status: true; data: T }
export interface ApiFailure { status: false; data: { status_code: number; error_message: unknown } | string }
export type ApiResult<T = unknown> = ApiSuccess<T> | ApiFailure | string;
export type Params = Record<string, unknown>;

const isObject = (value: unknown): value is Params => typeof value === 'object' && value !== null && !Array.isArray(value);
const withoutNulls = (params: Params = {}) => Object.fromEntries(Object.entries(params).filter(([, value]) => value !== null && value !== undefined));
function resolveUrl(template: string, params: Params): { url: string; remaining: Params } {
  const used = new Set<string>();
  const url = template.replace(/\{([A-Za-z_]\w*)\}/g, (_match, key: string) => { used.add(key); return encodeURIComponent(String(params[key] ?? '')); });
  return { url, remaining: Object.fromEntries(Object.entries(params).filter(([key]) => !used.has(key))) };
}
function stamp() { const d = new Date(); const p = (n: number) => String(n).padStart(2, '0'); return `${d.getFullYear()}${p(d.getMonth()+1)}${p(d.getDate())}_${p(d.getHours())}${p(d.getMinutes())}${p(d.getSeconds())}`; }

export class APIHandler {
  host: string | null = null; headers: Record<string, string> | null = null; SSL_Verify = true; debug_enabled = false; download_folder = '.';
  enable_debug() { this.debug_enabled = true; }
  conn(headers?: Record<string, string>, host?: string, enable_debug = false, enable_ssl = true, _organization?: string) { this.headers = headers ?? null; this.host = host ?? null; this.SSL_Verify = enable_ssl; if (enable_debug) this.enable_debug(); }
  get(url: string, params?: Params, type?: string) { return this.exec('GET', url, params, type); }
  send(url: string, params?: unknown, type?: string) { return this.exec('POST', url, params, type); }
  post(url: string, params?: unknown, type?: string) { return this.send(url, params, type); }
  insert(url: string, params?: unknown, type?: string) { return this.exec('PUT', url, params, type); }
  put(url: string, params?: unknown, type?: string) { return this.insert(url, params, type); }
  update(url: string, params?: unknown, type?: string) { return this.exec('PATCH', url, params, type); }
  delete(url: string, params?: Params, type?: string) { return this.exec('DELETE', url, params, type); }
  async download(url: string, params?: Params, type?: string, format = 'zip', folder = '') { this.download_folder = folder || '.'; return this.exec('GET', url, params, type, { download: true, format }); }
  async upload(url: string, file: unknown, params?: Params, type?: string) { return this.exec('POST', url, params, type, { upload: file }); }
  private async exec(method: string, relative: string, raw?: unknown, type?: string, options: { download?: boolean; format?: string; upload?: unknown } = {}): Promise<ApiResult> {
    if (!this.headers || !this.host) return { status: false, data: 'NOT AUTHENTICATED. Run Auth() first.' };
    const params = isObject(raw) ? withoutNulls(raw) : raw;
    const resolved = isObject(params) ? resolveUrl(relative, params) : { url: relative, remaining: {} };
    const url = new URL(resolved.url, `https://${this.host}`).toString();
    const headers = { ...this.headers, ...(type ? { 'Content-Type': type } : {}) };
    const init: RequestInit = { method, headers };
    try {
      let requestUrl = url;
      if (method === 'GET' || method === 'DELETE') {
        const query = new URLSearchParams();
        for (const [key, value] of Object.entries(resolved.remaining)) Array.isArray(value) ? value.forEach((item) => query.append(key, String(item))) : query.append(key, String(value));
        if ([...query].length) requestUrl += `${requestUrl.includes('?') ? '&' : '?'}${query}`;
      } else if (options.upload !== undefined) init.body = options.upload as BodyInit;
      else if (params !== undefined) { init.body = JSON.stringify(params); headers['Content-Type'] ??= 'application/json'; }
      if (this.debug_enabled) console.debug('URL =', requestUrl, params);
      return this.read(await fetch(requestUrl, init), options);
    } catch (error) { return { status: false, data: { status_code: 500, error_message: error } }; }
  }
  private async read(response: Response, options: { download?: boolean; format?: string }): Promise<ApiResult> {
    if (!response.ok) { const text = await response.text(); let message: unknown = text; try { message = JSON.parse(text).errorMessage ?? text; } catch {} return { status: false, data: { status_code: response.status, error_message: message } }; }
    if (options.download) { const name = new URL(response.url).pathname.split('/').pop()?.replaceAll('-', '_') || 'download'; const file = path.join(this.download_folder, `${name}_${stamp()}.${options.format || 'zip'}`); await fs.writeFile(file, Buffer.from(await response.arrayBuffer())); return { status: true, data: file }; }
    const text = await response.text(); try { return { status: true, data: JSON.parse(text) }; } catch { return { status: true, data: text }; }
  }
}

export class AuthenticationHandler {
  async test_authentication(headers: Record<string, string>, host: string): Promise<[boolean, unknown, Headers | null]> { for (const endpoint of ['api/v2/users/search', 'api/v2/dashboards']) { try { const response = await fetch(`https://${host}/${endpoint}`, { headers }); if (response.status === 401) return [false, 'Unauthorized', null]; if (response.status === 403) return [false, 'Forbidden', null]; if (response.status === 404) return [false, 'Not Found', null]; if (response.status === 500) return [false, 'Internal Server Error', null]; return [true, response, response.headers]; } catch (error) { return [false, error, null]; } } return [false, 'Authentication failed', null]; }
  async get_headers(host: string, accessToken: string): Promise<[Record<string, string> | null, unknown]> { const headers = { Authorization: `Bearer ${accessToken}` }; const [ok, data] = await this.test_authentication(headers, host); return ok ? [headers, host] : [null, data]; }
}

let fortidlp_connection: APIHandler | null = null; let debug = false; let ssl_enabled = true;
export function ignore_certificate() { ssl_enabled = false; console.warn('[!] - SSL validation cannot be disabled for native Node fetch. Use a trusted certificate.'); }
export function enable_debug() { debug = true; }
export function get_connection() { return fortidlp_connection; }
export async function auth(host: string, access_token: string): Promise<{ status: boolean; data: unknown }> { const normalized = host.replace(/^https?:\/\//, '').replace(/\/$/, '').split('/')[0]; const [headers, result] = await new AuthenticationHandler().get_headers(normalized, access_token); if (!headers) return { status: false, data: result }; fortidlp_connection = new APIHandler(); fortidlp_connection.conn(headers, normalized, debug, ssl_enabled); return { status: true, data: 'AUTHENTICATION_SUCCEEDED' }; }

type MethodSpec = { params: string[]; method: string; url: string }; type Manifest = { classes: Record<string, Record<string, MethodSpec>> };
export interface ControllerInstance { conn: APIHandler; [method: string]: any }
export type ControllerConstructor<T extends ControllerInstance = ControllerInstance> = new (conn?: APIHandler) => T;
function createControllerClass<T extends ControllerInstance>(name: string): ControllerConstructor<T> {
  const specs = (manifest as Manifest).classes[name] ?? {};
  class Generated { conn: APIHandler; constructor(conn?: APIHandler) { this.conn = conn ?? fortidlp_connection ?? new APIHandler(); } }
  for (const [methodName, spec] of Object.entries(specs)) Object.defineProperty(Generated.prototype, methodName, { value: function(this: { conn: APIHandler }, ...args: unknown[]) { const params = args.length === 1 && isObject(args[0]) && spec.params.length !== 1 ? args[0] : Object.fromEntries(spec.params.map((param, i) => [param, args[i]])); const body = args.length === 1 && isObject(args[0]) && spec.params.length === 1 ? args[0] : params; if (spec.method === 'GET') return this.conn.get(spec.url, withoutNulls(body)); if (spec.method === 'POST') return this.conn.post(spec.url, withoutNulls(body)); if (spec.method === 'PUT') return this.conn.put(spec.url, withoutNulls(body)); if (spec.method === 'PATCH') return this.conn.update(spec.url, withoutNulls(body)); return this.conn.delete(spec.url, withoutNulls(body)); } });
  return Generated as unknown as ControllerConstructor<T>;
}

// Generated from fortidlp/fortidlp.py and all standalone controllers.
export const Audit: ControllerConstructor = createControllerClass("Audit");
export const Cases: ControllerConstructor = createControllerClass("Cases");
export const Operators: ControllerConstructor = createControllerClass("Operators");
export const Users: ControllerConstructor = createControllerClass("Users");
export const Policies: ControllerConstructor = createControllerClass("Policies");
export const PoliciesData: ControllerConstructor = createControllerClass("PoliciesData");
export const Incidents: ControllerConstructor = createControllerClass("Incidents");
export const SaaS: ControllerConstructor = createControllerClass("SaaS");
export const Agents: ControllerConstructor = createControllerClass("Agents");
export const AgentConfigs: ControllerConstructor = createControllerClass("AgentConfigs");
export const AgentEnrollment: ControllerConstructor = createControllerClass("AgentEnrollment");
export const Labels: ControllerConstructor = createControllerClass("Labels");
export const AccessTokens: ControllerConstructor = createControllerClass("AccessTokens");
export const Admin: ControllerConstructor = createControllerClass("Admin");
export const AgentActions: ControllerConstructor = createControllerClass("AgentActions");
export const AgentOfflineConfig: ControllerConstructor = createControllerClass("AgentOfflineConfig");
export const Box: ControllerConstructor = createControllerClass("Box");
export const BoxDirectory: ControllerConstructor = createControllerClass("BoxDirectory");
export const Classifications: ControllerConstructor = createControllerClass("Classifications");
export const CloudActions: ControllerConstructor = createControllerClass("CloudActions");
export const Dashboards: ControllerConstructor = createControllerClass("Dashboards");
export const DriveLabelsScheduledSync: ControllerConstructor = createControllerClass("DriveLabelsScheduledSync");
export const Emails: ControllerConstructor = createControllerClass("Emails");
export const EntraID: ControllerConstructor = createControllerClass("EntraID");
export const Events: ControllerConstructor = createControllerClass("Events");
export const FileShadow: ControllerConstructor = createControllerClass("FileShadow");
export const GlobalOperators: ControllerConstructor = createControllerClass("GlobalOperators");
export const Google: ControllerConstructor = createControllerClass("Google");
export const GoogleDirectory: ControllerConstructor = createControllerClass("GoogleDirectory");
export const Indicators: ControllerConstructor = createControllerClass("Indicators");
export const Ldap: ControllerConstructor = createControllerClass("Ldap");
export const Locations: ControllerConstructor = createControllerClass("Locations");
export const MFA: ControllerConstructor = createControllerClass("MFA");
export const ManagedServiceReports: ControllerConstructor = createControllerClass("ManagedServiceReports");
export const Microsoft: ControllerConstructor = createControllerClass("Microsoft");
export const OperatorPreferences: ControllerConstructor = createControllerClass("OperatorPreferences");
export const Outlook: ControllerConstructor = createControllerClass("Outlook");
export const Passphrase: ControllerConstructor = createControllerClass("Passphrase");
export const Permissions: ControllerConstructor = createControllerClass("Permissions");
export const Perspectives: ControllerConstructor = createControllerClass("Perspectives");
export const Quota: ControllerConstructor = createControllerClass("Quota");
export const Roles: ControllerConstructor = createControllerClass("Roles");
export const SAML: ControllerConstructor = createControllerClass("SAML");
export const SavedQueries: ControllerConstructor = createControllerClass("SavedQueries");
export const ScopedInvestigations: ControllerConstructor = createControllerClass("ScopedInvestigations");
export const Search: ControllerConstructor = createControllerClass("Search");
export const SequenceDetection: ControllerConstructor = createControllerClass("SequenceDetection");
export const Siem: ControllerConstructor = createControllerClass("Siem");
export const Slack: ControllerConstructor = createControllerClass("Slack");
export const StackFederation: ControllerConstructor = createControllerClass("StackFederation");
export const SupportingOperators: ControllerConstructor = createControllerClass("SupportingOperators");
export const TenantPreferences: ControllerConstructor = createControllerClass("TenantPreferences");
export const Tenants: ControllerConstructor = createControllerClass("Tenants");
export const TimelineSearch: ControllerConstructor = createControllerClass("TimelineSearch");
export const UsageStatistics: ControllerConstructor = createControllerClass("UsageStatistics");
export const Webhooks: ControllerConstructor = createControllerClass("Webhooks");
export const ActionEvents: ControllerConstructor = createControllerClass("ActionEvents");
export const AgentGroups: ControllerConstructor = createControllerClass("AgentGroups");
export const AuditLogs: ControllerConstructor = createControllerClass("AuditLogs");
export const Authentication: ControllerConstructor = createControllerClass("Authentication");
export const DashboardService: ControllerConstructor = createControllerClass("DashboardService");
export const EntitiesSearch: ControllerConstructor = createControllerClass("EntitiesSearch");
export const ML: ControllerConstructor = createControllerClass("ML");
export const SaaSApplications: ControllerConstructor = createControllerClass("SaaSApplications");
