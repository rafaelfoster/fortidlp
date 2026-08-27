"""Agent Groups API"""


class AgentGroups:
    """Manage Agent Groups (AgentPolicyGroup)"""

    def __init__(self, client):
        self.client = client

    def list(self, **kwargs):
        """List all agent groups."""
        return self.client.get('/api/v1/agent_policy_groups', params=kwargs)

    def create(self, data, **kwargs):
        """Create a new agent group."""
        return self.client.post('/api/v1/agent_policy_groups', json=data, params=kwargs)

    def get(self, group_id, **kwargs):
        """Get a specific agent group."""
        return self.client.get(f'/api/v1/agent_policy_groups/{group_id}', params=kwargs)

    def update(self, group_id, data, **kwargs):
        """Update an agent group."""
        return self.client.put(f'/api/v1/agent_policy_groups/{group_id}', json=data, params=kwargs)

    def delete(self, group_id, **kwargs):
        """Delete an agent group."""
        return self.client.delete(f'/api/v1/agent_policy_groups/{group_id}', params=kwargs)