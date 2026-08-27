from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class GoogleDirectory:
    '''
    Class GoogleDirectory
    Description: Manages Google Directory configurations.
    '''

    def get_google_directory_configs(self) -> dict:
        '''
        Description: Gets Google Directory configurations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/google/directory/configs'
        return fortidlp_connection.get(url)

    def create_google_directory_config(self, name: str, domain: str, client_id: str, client_secret: str) -> dict:
        '''
        Description: Creates a GoogleDirectory configuration.
        Args:
            name (str): The name of the configuration.
            domain (str): The domain to sync.
            client_id (str): The client ID.
            client_secret (str): The client secret.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/google/directory/configs'
        data = {
            "name": name,
            "domain": domain,
            "client_id": client_id,
            "client_secret": client_secret
        }
        return fortidlp_connection.post(url, json=data)

    def delete_google_directory_config(self, config_id: str) -> dict:
        '''
        Description: Deletes a Google Directory configuration.
        Args:
            config_id (str): The ID of the configuration to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/directory/configs/{config_id}'
        return fortidlp_connection.delete(url)

    def get_google_directory_config(self, config_id: str) -> dict:
        '''
        Description: Gets a Google Directory configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/directory/configs/{config_id}'
        return fortidlp_connection.get(url)

    def update_google_directory_config(self, config_id: str, name: Optional[str] = None, domain: Optional[str] = None, client_id: Optional[str] = None, client_secret: Optional[str] = None) -> dict:
        '''
        Description: Updates a Google Directory configuration.
        Args:
            config_id (str): The ID of the configuration.
            name (str, optional): The new name for the configuration.
            domain (str, optional): The new domain to sync.
            client_id (str, optional): The new client ID.
            client_secret (str, optional): The new client secret.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/directory/configs/{config_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if domain is not None:
            data["domain"] = domain
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        return fortidlp_connection.put(url, json=data)

    def sync_google_directory_config(self, config_id: str) -> dict:
        '''
        Description: Requests an immediate Google Directory sync for the specified configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/directory/configs/{config_id}/sync'
        return fortidlp_connection.post(url)

    def sync_google_directory_groups(self, config_id: str) -> dict:
        '''
        Description: Requests an immediate Google Directory sync to update the group labels for the specified configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/directory/configs/{config_id}/sync/groups'
        return fortidlp_connection.post(url)

    def get_google_directory_groups(self) -> dict:
        '''
        Description: Gets all Google Directory groups.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/google/directory/groups'
        return fortidlp_connection.post(url)
