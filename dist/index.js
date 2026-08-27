import fs from 'node:fs/promises';
import path from 'node:path';
import { Buffer } from 'node:buffer';
import manifest from './generated-manifest.json' with { type: 'json' };
export const version = '1.0';
const isObject = (value) => typeof value === 'object' && value !== null && !Array.isArray(value);
const withoutNulls = (params = {}) => Object.fromEntries(Object.entries(params).filter(([, value]) => value !== null && value !== undefined));
function resolveUrl(template, params) {
    const used = new Set();
    const url = template.replace(/\{([A-Za-z_]\w*)\}/g, (_match, key) => { used.add(key); return encodeURIComponent(String(params[key] ?? '')); });
    return { url, remaining: Object.fromEntries(Object.entries(params).filter(([key]) => !used.has(key))) };
}
function stamp() { const d = new Date(); const p = (n) => String(n).padStart(2, '0'); return `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}_${p(d.getHours())}${p(d.getMinutes())}${p(d.getSeconds())}`; }
export class APIHandler {
    host = null;
    headers = null;
    SSL_Verify = true;
    debug_enabled = false;
    download_folder = '.';
    enable_debug() { this.debug_enabled = true; }
    conn(headers, host, enable_debug = false, enable_ssl = true, _organization) { this.headers = headers ?? null; this.host = host ?? null; this.SSL_Verify = enable_ssl; if (enable_debug)
        this.enable_debug(); }
    get(url, params, type) { return this.exec('GET', url, params, type); }
    send(url, params, type) { return this.exec('POST', url, params, type); }
    post(url, params, type) { return this.send(url, params, type); }
    insert(url, params, type) { return this.exec('PUT', url, params, type); }
    put(url, params, type) { return this.insert(url, params, type); }
    update(url, params, type) { return this.exec('PATCH', url, params, type); }
    delete(url, params, type) { return this.exec('DELETE', url, params, type); }
    async download(url, params, type, format = 'zip', folder = '') { this.download_folder = folder || '.'; return this.exec('GET', url, params, type, { download: true, format }); }
    async upload(url, file, params, type) { return this.exec('POST', url, params, type, { upload: file }); }
    async exec(method, relative, raw, type, options = {}) {
        if (!this.headers || !this.host)
            return { status: false, data: 'NOT AUTHENTICATED. Run Auth() first.' };
        const params = isObject(raw) ? withoutNulls(raw) : raw;
        const resolved = isObject(params) ? resolveUrl(relative, params) : { url: relative, remaining: {} };
        const url = new URL(resolved.url, `https://${this.host}`).toString();
        const headers = { ...this.headers, ...(type ? { 'Content-Type': type } : {}) };
        const init = { method, headers };
        try {
            let requestUrl = url;
            if (method === 'GET' || method === 'DELETE') {
                const query = new URLSearchParams();
                for (const [key, value] of Object.entries(resolved.remaining))
                    Array.isArray(value) ? value.forEach((item) => query.append(key, String(item))) : query.append(key, String(value));
                if ([...query].length)
                    requestUrl += `${requestUrl.includes('?') ? '&' : '?'}${query}`;
            }
            else if (options.upload !== undefined)
                init.body = options.upload;
            else if (params !== undefined) {
                init.body = JSON.stringify(params);
                headers['Content-Type'] ??= 'application/json';
            }
            if (this.debug_enabled)
                console.debug('URL =', requestUrl, params);
            return this.read(await fetch(requestUrl, init), options);
        }
        catch (error) {
            return { status: false, data: { status_code: 500, error_message: error } };
        }
    }
    async read(response, options) {
        if (!response.ok) {
            const text = await response.text();
            let message = text;
            try {
                message = JSON.parse(text).errorMessage ?? text;
            }
            catch { }
            return { status: false, data: { status_code: response.status, error_message: message } };
        }
        if (options.download) {
            const name = new URL(response.url).pathname.split('/').pop()?.replaceAll('-', '_') || 'download';
            const file = path.join(this.download_folder, `${name}_${stamp()}.${options.format || 'zip'}`);
            await fs.writeFile(file, Buffer.from(await response.arrayBuffer()));
            return { status: true, data: file };
        }
        const text = await response.text();
        try {
            return { status: true, data: JSON.parse(text) };
        }
        catch {
            return { status: true, data: text };
        }
    }
}
export class AuthenticationHandler {
    async test_authentication(headers, host) { for (const endpoint of ['api/v2/users/search', 'api/v2/dashboards']) {
        try {
            const response = await fetch(`https://${host}/${endpoint}`, { headers });
            if (response.status === 401)
                return [false, 'Unauthorized', null];
            if (response.status === 403)
                return [false, 'Forbidden', null];
            if (response.status === 404)
                return [false, 'Not Found', null];
            if (response.status === 500)
                return [false, 'Internal Server Error', null];
            return [true, response, response.headers];
        }
        catch (error) {
            return [false, error, null];
        }
    } return [false, 'Authentication failed', null]; }
    async get_headers(host, accessToken) { const headers = { Authorization: `Bearer ${accessToken}` }; const [ok, data] = await this.test_authentication(headers, host); return ok ? [headers, host] : [null, data]; }
}
let fortidlp_connection = null;
let debug = false;
let ssl_enabled = true;
export function ignore_certificate() { ssl_enabled = false; console.warn('[!] - SSL validation cannot be disabled for native Node fetch. Use a trusted certificate.'); }
export function enable_debug() { debug = true; }
export function get_connection() { return fortidlp_connection; }
export async function auth(host, access_token) { const normalized = host.replace(/^https?:\/\//, '').replace(/\/$/, '').split('/')[0]; const [headers, result] = await new AuthenticationHandler().get_headers(normalized, access_token); if (!headers)
    return { status: false, data: result }; fortidlp_connection = new APIHandler(); fortidlp_connection.conn(headers, normalized, debug, ssl_enabled); return { status: true, data: 'AUTHENTICATION_SUCCEEDED' }; }
function createControllerClass(name) {
    const specs = manifest.classes[name] ?? {};
    class Generated {
        conn;
        constructor(conn) { this.conn = conn ?? fortidlp_connection ?? new APIHandler(); }
    }
    for (const [methodName, spec] of Object.entries(specs))
        Object.defineProperty(Generated.prototype, methodName, { value: function (...args) { const params = args.length === 1 && isObject(args[0]) && spec.params.length !== 1 ? args[0] : Object.fromEntries(spec.params.map((param, i) => [param, args[i]])); const body = args.length === 1 && isObject(args[0]) && spec.params.length === 1 ? args[0] : params; if (spec.method === 'GET')
                return this.conn.get(spec.url, withoutNulls(body)); if (spec.method === 'POST')
                return this.conn.post(spec.url, withoutNulls(body)); if (spec.method === 'PUT')
                return this.conn.put(spec.url, withoutNulls(body)); if (spec.method === 'PATCH')
                return this.conn.update(spec.url, withoutNulls(body)); return this.conn.delete(spec.url, withoutNulls(body)); } });
    return Generated;
}
// Generated from fortidlp/fortidlp.py and all standalone controllers.
export const Audit = createControllerClass("Audit");
export const Cases = createControllerClass("Cases");
export const Operators = createControllerClass("Operators");
export const Users = createControllerClass("Users");
export const Policies = createControllerClass("Policies");
export const PoliciesData = createControllerClass("PoliciesData");
export const Incidents = createControllerClass("Incidents");
export const SaaS = createControllerClass("SaaS");
export const Agents = createControllerClass("Agents");
export const AgentConfigs = createControllerClass("AgentConfigs");
export const AgentEnrollment = createControllerClass("AgentEnrollment");
export const Labels = createControllerClass("Labels");
export const AccessTokens = createControllerClass("AccessTokens");
export const Admin = createControllerClass("Admin");
export const AgentActions = createControllerClass("AgentActions");
export const AgentOfflineConfig = createControllerClass("AgentOfflineConfig");
export const Box = createControllerClass("Box");
export const BoxDirectory = createControllerClass("BoxDirectory");
export const Classifications = createControllerClass("Classifications");
export const CloudActions = createControllerClass("CloudActions");
export const Dashboards = createControllerClass("Dashboards");
export const DriveLabelsScheduledSync = createControllerClass("DriveLabelsScheduledSync");
export const Emails = createControllerClass("Emails");
export const EntraID = createControllerClass("EntraID");
export const Events = createControllerClass("Events");
export const FileShadow = createControllerClass("FileShadow");
export const GlobalOperators = createControllerClass("GlobalOperators");
export const Google = createControllerClass("Google");
export const GoogleDirectory = createControllerClass("GoogleDirectory");
export const Indicators = createControllerClass("Indicators");
export const Ldap = createControllerClass("Ldap");
export const Locations = createControllerClass("Locations");
export const MFA = createControllerClass("MFA");
export const ManagedServiceReports = createControllerClass("ManagedServiceReports");
export const Microsoft = createControllerClass("Microsoft");
export const OperatorPreferences = createControllerClass("OperatorPreferences");
export const Outlook = createControllerClass("Outlook");
export const Passphrase = createControllerClass("Passphrase");
export const Permissions = createControllerClass("Permissions");
export const Perspectives = createControllerClass("Perspectives");
export const Quota = createControllerClass("Quota");
export const Roles = createControllerClass("Roles");
export const SAML = createControllerClass("SAML");
export const SavedQueries = createControllerClass("SavedQueries");
export const ScopedInvestigations = createControllerClass("ScopedInvestigations");
export const Search = createControllerClass("Search");
export const SequenceDetection = createControllerClass("SequenceDetection");
export const Siem = createControllerClass("Siem");
export const Slack = createControllerClass("Slack");
export const StackFederation = createControllerClass("StackFederation");
export const SupportingOperators = createControllerClass("SupportingOperators");
export const TenantPreferences = createControllerClass("TenantPreferences");
export const Tenants = createControllerClass("Tenants");
export const TimelineSearch = createControllerClass("TimelineSearch");
export const UsageStatistics = createControllerClass("UsageStatistics");
export const Webhooks = createControllerClass("Webhooks");
export const ActionEvents = createControllerClass("ActionEvents");
export const AgentGroups = createControllerClass("AgentGroups");
export const AuditLogs = createControllerClass("AuditLogs");
export const Authentication = createControllerClass("Authentication");
export const DashboardService = createControllerClass("DashboardService");
export const EntitiesSearch = createControllerClass("EntitiesSearch");
export const ML = createControllerClass("ML");
export const SaaSApplications = createControllerClass("SaaSApplications");
