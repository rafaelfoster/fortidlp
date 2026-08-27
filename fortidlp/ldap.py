from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Ldap:
    '''
    Class Ldap
    Description: Configures LDAP integrations.
    '''

    def get_ldap_configs(self) -> dict:
        '''
        Description: Gets LDAP configurations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/ldap/config'
        return fortidlp_connection.get(url)

    def create_ldap_config(self, name: str, host: str, port: int, base_dn: str, bind_dn: str, bind_password: str) -> dict:
        '''
        Description: Creates an LDAP configuration.
        Args:
            name (str): The name of the configuration.
            host (str): The LDAP host.
            port (int): The LDAP port.
            base_dn (str): The base DN for searches.
            bind_dn (str): The bind DN for authentication.
            bind_password (str): The bind password for authentication.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/ldap/config'
        data = {
            "name": name,
            "host": host,
            "port": port,
            "base_dn": base_dn,
            "bind_dn": bind_dn,
            "bind_password": bind_password
        }
        return fortidlp_connection.post(url, json=data)

    def delete_ldap_config(self, config_id: str) -> dict:
        '''
        Description: Deletes an LDAP configuration.
        Args:
            config_id (str): The ID of the configuration to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/ldap/config/{config_id}'
        return fortidlp_connection.delete(url)

    def get_ldap_config(self, config_id: str) -> dict:
        '''
        Description: Gets an LDAP configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/ldap/config/{config_id}'
        return fortidlp_connection.get(url)

    def update_ldap_config(self, config_id: str, name: Optional[str] = None, host: Optional[str] = None, port: Optional[int] = None, base_dn: Optional[str] = None, bind_dn: Optional[str] = None, bind_password: Optional[str] = None) -> dict:
        '''
        Description: Updates an LDAP configuration.
        Args:
            config_id (str): The ID of the configuration.
            name (str, optional): The new name for the configuration.
            host (str, optional): The new LDAP host.
            port (int, optional): The new LDAP port.
            base_dn (str, optional): The new base DN for searches.
            bind_dn (str, optional): The new bind DN for authentication.
            bind_password (str, optional): The new bind password for authentication.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/ldap/config/{config_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if host is not None:
            data["host"] = host
        if port is not None:
            data["port"] = port
        if base_dn is not None:
            data["base_dn"] = base_dn
        if bind_dn is not None:
            data["bind_dn"] = bind_dn
        if bind_password is not None:
            data["bind_password"] = bind_password
        return fortidlp_connection.put(url, json=data)

    def get_ldap_sync_status(self, config_id: str) -> dict:
        '''
        Description: Fetches the sync status for the last performed LDAP sync.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/ldap/config/{config_id}/status'
        return fortidlp_connection.get(url)

    def update_ldap_sync_status(self, config_id: str, status: str) -> dict:
        '''
        Description: Updates the sync status for the last performed LDAP sync.
        Args:
            config_id (str): The ID of the configuration.
            status (str): The new sync status.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/ldap/config/{config_id}/status'
        data = {"status": status}
        return fortidlp_connection.put(url, json=data)

    def get_ldap_sync_tool_versions(self) -> dict:
        '''
        Description: Returns versions of the LDAP sync tool.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/ldap/sync-tool'
        return fortidlp_connection.get(url)

    def perform_ldap_sync(self, config_id: str) -> dict:
        '''
        Description: Performs an LDAP sync for the specified configuration.
        Args:
            config_id (str): The ID of the configuration.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/ldap/sync/{config_id}'
        return fortidlp_connection.post(url)
