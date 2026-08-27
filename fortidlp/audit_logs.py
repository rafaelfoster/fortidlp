"""Audit Logs API"""


class AuditLogs:
    """Access Audit Logs"""

    def __init__(self, client):
        self.client = client

    def list(self, **kwargs):
        """List all audit logs."""
        return self.client.get('/api/v1/audit_logs', params=kwargs)

    def get(self, log_id, **kwargs):
        """Get a specific audit log."""
        return self.client.get(f'/api/v1/audit_logs/{log_id}', params=kwargs)