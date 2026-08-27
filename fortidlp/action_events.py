"""Action Events API"""


class ActionEvents:
    """Manage Action Events"""

    def __init__(self, client):
        self.client = client

    def list(self, **kwargs):
        """List all action events."""
        return self.client.get('/api/v1/action_events', params=kwargs)

    def get(self, event_id, **kwargs):
        """Get a specific action event."""
        return self.client.get(f'/api/v1/action_events/{event_id}', params=kwargs)