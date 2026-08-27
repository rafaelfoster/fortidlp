export declare const version = "1.0";
export interface ApiSuccess<T = unknown> {
    status: true;
    data: T;
}
export interface ApiFailure {
    status: false;
    data: {
        status_code: number;
        error_message: unknown;
    } | string;
}
export type ApiResult<T = unknown> = ApiSuccess<T> | ApiFailure | string;
export type Params = Record<string, unknown>;
export declare class APIHandler {
    host: string | null;
    headers: Record<string, string> | null;
    SSL_Verify: boolean;
    debug_enabled: boolean;
    download_folder: string;
    enable_debug(): void;
    conn(headers?: Record<string, string>, host?: string, enable_debug?: boolean, enable_ssl?: boolean, _organization?: string): void;
    get(url: string, params?: Params, type?: string): Promise<ApiResult<unknown>>;
    send(url: string, params?: unknown, type?: string): Promise<ApiResult<unknown>>;
    post(url: string, params?: unknown, type?: string): Promise<ApiResult<unknown>>;
    insert(url: string, params?: unknown, type?: string): Promise<ApiResult<unknown>>;
    put(url: string, params?: unknown, type?: string): Promise<ApiResult<unknown>>;
    update(url: string, params?: unknown, type?: string): Promise<ApiResult<unknown>>;
    delete(url: string, params?: Params, type?: string): Promise<ApiResult<unknown>>;
    download(url: string, params?: Params, type?: string, format?: string, folder?: string): Promise<ApiResult<unknown>>;
    upload(url: string, file: unknown, params?: Params, type?: string): Promise<ApiResult<unknown>>;
    private exec;
    private read;
}
export declare class AuthenticationHandler {
    test_authentication(headers: Record<string, string>, host: string): Promise<[boolean, unknown, Headers | null]>;
    get_headers(host: string, accessToken: string): Promise<[Record<string, string> | null, unknown]>;
}
export declare function ignore_certificate(): void;
export declare function enable_debug(): void;
export declare function get_connection(): APIHandler | null;
export declare function auth(host: string, access_token: string): Promise<{
    status: boolean;
    data: unknown;
}>;
export interface ControllerInstance {
    conn: APIHandler;
    [method: string]: any;
}
export type ControllerConstructor<T extends ControllerInstance = ControllerInstance> = new (conn?: APIHandler) => T;
export declare const Audit: ControllerConstructor;
export declare const Cases: ControllerConstructor;
export declare const Operators: ControllerConstructor;
export declare const Users: ControllerConstructor;
export declare const Policies: ControllerConstructor;
export declare const PoliciesData: ControllerConstructor;
export declare const Incidents: ControllerConstructor;
export declare const SaaS: ControllerConstructor;
export declare const Agents: ControllerConstructor;
export declare const AgentConfigs: ControllerConstructor;
export declare const AgentEnrollment: ControllerConstructor;
export declare const Labels: ControllerConstructor;
export declare const AccessTokens: ControllerConstructor;
export declare const Admin: ControllerConstructor;
export declare const AgentActions: ControllerConstructor;
export declare const AgentOfflineConfig: ControllerConstructor;
export declare const Box: ControllerConstructor;
export declare const BoxDirectory: ControllerConstructor;
export declare const Classifications: ControllerConstructor;
export declare const CloudActions: ControllerConstructor;
export declare const Dashboards: ControllerConstructor;
export declare const DriveLabelsScheduledSync: ControllerConstructor;
export declare const Emails: ControllerConstructor;
export declare const EntraID: ControllerConstructor;
export declare const Events: ControllerConstructor;
export declare const FileShadow: ControllerConstructor;
export declare const GlobalOperators: ControllerConstructor;
export declare const Google: ControllerConstructor;
export declare const GoogleDirectory: ControllerConstructor;
export declare const Indicators: ControllerConstructor;
export declare const Ldap: ControllerConstructor;
export declare const Locations: ControllerConstructor;
export declare const MFA: ControllerConstructor;
export declare const ManagedServiceReports: ControllerConstructor;
export declare const Microsoft: ControllerConstructor;
export declare const OperatorPreferences: ControllerConstructor;
export declare const Outlook: ControllerConstructor;
export declare const Passphrase: ControllerConstructor;
export declare const Permissions: ControllerConstructor;
export declare const Perspectives: ControllerConstructor;
export declare const Quota: ControllerConstructor;
export declare const Roles: ControllerConstructor;
export declare const SAML: ControllerConstructor;
export declare const SavedQueries: ControllerConstructor;
export declare const ScopedInvestigations: ControllerConstructor;
export declare const Search: ControllerConstructor;
export declare const SequenceDetection: ControllerConstructor;
export declare const Siem: ControllerConstructor;
export declare const Slack: ControllerConstructor;
export declare const StackFederation: ControllerConstructor;
export declare const SupportingOperators: ControllerConstructor;
export declare const TenantPreferences: ControllerConstructor;
export declare const Tenants: ControllerConstructor;
export declare const TimelineSearch: ControllerConstructor;
export declare const UsageStatistics: ControllerConstructor;
export declare const Webhooks: ControllerConstructor;
export declare const ActionEvents: ControllerConstructor;
export declare const AgentGroups: ControllerConstructor;
export declare const AuditLogs: ControllerConstructor;
export declare const Authentication: ControllerConstructor;
export declare const DashboardService: ControllerConstructor;
export declare const EntitiesSearch: ControllerConstructor;
export declare const ML: ControllerConstructor;
export declare const SaaSApplications: ControllerConstructor;
//# sourceMappingURL=index.d.ts.map