from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Roles:
    '''
    Class Roles
    Description: Manages operator roles.
    '''

    def get_roles(self) -> dict:
        '''
        Description: Return a list of roles.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/roles'
        return fortidlp_connection.get(url)

    def create_role(self, name: str, description: Optional[str] = None, permissions: Optional[List[str]] = None) -> dict:
        '''
        Description: Creates a new role.
        Args:
            name (str): The name of the role.
            description (str, optional): The description of the role.
            permissions (List[str], optional): List of permissions for the role.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/roles'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if permissions is not None:
            data["permissions"] = permissions
        return fortidlp_connection.post(url, json=data)

    def delete_role(self, role_id: str) -> dict:
        '''
        Description: Delete a role.
        Args:
            role_id (str): The ID of the role to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/roles/{role_id}'
        return fortidlp_connection.delete(url)

    def get_role(self, role_id: str) -> dict:
        '''
        Description: Return a role.
        Args:
            role_id (str): The ID of the role.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/roles/{role_id}'
        return fortidlp_connection.get(url)

    def update_role(self, role_id: str, name: Optional[str] = None, description: Optional[str] = None, permissions: Optional[List[str]] = None) -> dict:
        '''
        Description: Update a role.
        Args:
            role_id (str): The ID of the role.
            name (str, optional): The new name for the role.
            description (str, optional): The new description for the role.
            permissions (List[str], optional): The new list of permissions for the role.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/roles/{role_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if permissions is not None:
            data["permissions"] = permissions
        return fortidlp_connection.put(url, json=data)
