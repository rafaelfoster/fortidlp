from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class EntraID:
    '''
    Class EntraID
    Description: Manages Entra ID configurations.
    '''

    def get_entra_id_configs(self) -> dict:
        '''
        Description: Gets EntraID configurations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/entraid/configs'
        return fortidlp_connection.get(url)

    def create_entra_id_config(self, name: str, client_id: str, client_secret: str, tenant_id: str) -> dict:
        '''
        Description: Creates an EntraID configuration.
        Args:
            name (str): The name of the configuration.
            client_id (str): The client ID.
            client_secret (str): The client secret.
            tenant_id (str): The tenant ID.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/entraid/configs'
        data = {
            "name": name,
            "client_id": client_id,
            "client_secret": client_secret,
            "tenant_id": tenant_id
        }
        return fortidlp_connection.post(url, json=data)

    def delete_entra_id_config(self, config_id: str) -> dict:
        '''
        Description: Deletes an EntraID configuration.
        Args:
            config_id (str): The ID of the configuration to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/entraid/configs/{config_id}'
        return fortidlp_connection.delete(url)

    def get_entra_id_config(self, config_id: str) -> dict:
        '''
        Description: Gets an EntraID configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/entraid/configs/{config_id}'
        return fortidlp_connection.get(url)

    def update_entra_id_config(self, config_id: str, name: Optional[str] = None, client_id: Optional[str] = None, client_secret: Optional[str] = None, tenant_id: Optional[str] = None) -> dict:
        '''
        Description: Updates an EntraID configuration.
        Args:
            config_id (str): The ID of the configuration.
            name (str, optional): The new name for the configuration.
            client_id (str, optional): The new client ID.
            client_secret (str, optional): The new client secret.
            tenant_id (str, optional): The new tenant ID.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/entraid/configs/{config_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if tenant_id is not None:
            data["tenant_id"] = tenant_id
        return fortidlp_connection.put(url, json=data)

    def sync_entra_id_config(self, config_id: str) -> dict:
        '''
        Description: Requests an immediate EntraID sync for the specified configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/entraid/configs/{config_id}/sync'
        return fortidlp_connection.post(url)

    def sync_entra_id_groups(self, config_id: str) -> dict:
        '''
        Description: Requests an immediate EntraID sync to update the groups labels for the specified configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/entraid/configs/{config_id}/sync/groups'
        return fortidlp_connection.post(url)

    def get_entra_id_user_count(self) -> dict:
        '''
        Description: Returns the number of user that will be synced.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/entraid/count'
        return fortidlp_connection.post(url)

    def get_entra_id_groups(self) -> dict:
        '''
        Description: Gets all Entra ID groups.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/entraid/groups'
        return fortidlp_connection.post(url)
