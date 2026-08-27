from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class AgentConfigs:
    '''
    Class AgentConfigs
    Description: Applies configuration to agents.
    '''

    def list_agent_configurations(self) -> dict:
        '''
        Description: List agent configurations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/agent-configs'
        return fortidlp_connection.get(url)

    def create_agent_configuration(self, name: str, description: Optional[str] = None, data: Optional[dict] = None) -> dict:
        '''
        Description: Creates a new agent configuration and returns the new agent configuration.
        Args:
            name (str): The name of the agent configuration.
            description (str, optional): The description of the agent configuration.
            data (dict, optional): The configuration data.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/agent-configs'
        payload = {
            "name": name,
            "description": description,
            "data": data
        }
        return fortidlp_connection.post(url, json=payload)

    def export_agent_configs(self, config_ids: List[str]) -> dict:
        '''
        Description: Export the agent configs specified in the request.
        Args:
            config_ids (List[str]): List of agent configuration IDs to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/agent-configs/export'
        data = {"config_ids": config_ids}
        return fortidlp_connection.post(url, json=data)

    def import_agent_configs(self, configs_file_content: bytes, content_type: str) -> dict:
        '''
        Description: Import agent configs.
        Args:
            configs_file_content (bytes): The content of the configurations file.
            content_type (str): The content type of the file (e.g., "application/json").
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/agent-configs/import'
        files = {'file': ('configs', configs_file_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def test_agent_configs(self, label_uuids: List[str]) -> dict:
        '''
        Description: Return config key-values by label uuids.
        Args:
            label_uuids (List[str]): List of label UUIDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/agent-configs/test'
        data = {"label_uuids": label_uuids}
        return fortidlp_connection.post(url, json=data)

    def delete_agent_configuration(self, config_id: str) -> dict:
        '''
        Description: Delete an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}'
        return fortidlp_connection.delete(url)

    def get_agent_configuration(self, config_id: str) -> dict:
        '''
        Description: Get an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}'
        return fortidlp_connection.get(url)

    def update_agent_configuration(self, config_id: str, name: Optional[str] = None, description: Optional[str] = None, data: Optional[dict] = None) -> dict:
        '''
        Description: Updates an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
            name (str, optional): The new name for the agent configuration.
            description (str, optional): The new description for the agent configuration.
            data (dict, optional): The new configuration data.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}'
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if data is not None:
            payload["data"] = data
        return fortidlp_connection.put(url, json=payload)

    def delete_agent_config_key(self, config_id: str, key: str) -> dict:
        '''
        Description: Deletes the given key if it exists and its value.
        Args:
            config_id (str): The ID of the agent configuration.
            key (str): The key to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}/keys/{key}'
        return fortidlp_connection.delete(url)

    def get_agent_config_key(self, config_id: str, key: str) -> dict:
        '''
        Description: Retrieves the value for a given key from the data field of an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
            key (str): The key to retrieve.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}/keys/{key}'
        return fortidlp_connection.get(url)

    def add_or_update_agent_config_key(self, config_id: str, key: str, value: str) -> dict:
        '''
        Description: Adds the given key-value pair to an agent configuration. If the key exists, the value is updated.
        Args:
            config_id (str): The ID of the agent configuration.
            key (str): The key to add or update.
            value (str): The value for the key.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}/keys/{key}'
        data = {"value": value}
        return fortidlp_connection.post(url, json=data)

    def unassign_labels_from_agent_config(self, config_id: str) -> dict:
        '''
        Description: Unassign labels from an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}/labels'
        return fortidlp_connection.delete(url)

    def get_labels_assigned_to_agent_config(self, config_id: str) -> dict:
        '''
        Description: Return labels assigned to an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}/labels'
        return fortidlp_connection.get(url)

    def assign_labels_to_agent_config(self, config_id: str, label_ids: List[str]) -> dict:
        '''
        Description: Assign labels to an agent configuration.
        Args:
            config_id (str): The ID of the agent configuration.
            label_ids (List[str]): List of label IDs to assign.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/agent-configs/{config_id}/labels'
        data = {"label_ids": label_ids}
        return fortidlp_connection.put(url, json=data)
