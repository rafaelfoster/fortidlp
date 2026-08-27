"""Access Tokens API"""


class AccessTokens:
    """Manage Access Tokens"""

    def __init__(self, client):
        self.client = client

    def list(self, **kwargs):
        """List all access tokens."""
        return self.client.get('/api/v1/access_tokens', params=kwargs)

    def create(self, data, **kwargs):
        """Create a new access token."""
        return self.client.post('/api/v1/access_tokens', json=data, params=kwargs)

    def get(self, token_id, **kwargs):
        """Get a specific access token."""
        return self.client.get(f'/api/v1/access_tokens/{token_id}', params=kwargs)

    def delete(self, token_id, **kwargs):
        """Delete an access token."""
        return self.client.delete(f'/api/v1/access_tokens/{token_id}', params=kwargs)