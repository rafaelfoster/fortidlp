from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Operators:
    '''
    Class Operators
    Description: Manages the internal operators directory.
    '''

    def get_authentication_log(self) -> dict:
        '''
        Description: List the authentication log for operator.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/authentication-log'
        return fortidlp_connection.get(url)

    def get_operators(self) -> dict:
        '''
        Description: Return a list of operators.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/operators'
        return fortidlp_connection.get(url)

    def add_operator(self, username: str, name: str, email: str, company: str, password: str, role: str, link_expiration: int = 1, password_reset_on_login: bool = True) -> dict:
        '''
        Description: Adds a new operator.
        Args:
            username (str): The username of the operator.
            name (str): The display name of the operator.
            email (str): The email of the operator.
            company (str): The company of the operator.
            password (str): The password for the operator.
            role (str): The role of the operator.
            link_expiration (int, optional): Link expiration in days. Defaults to 1.
            password_reset_on_login (bool, optional): Whether to reset password on next login. Defaults to True.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/operators'
        data = {
            "operator": {
                "company": company,
                "display_name": name,
                "email": email,
                "name": username,
                "roles": [role]
            },
            "passphrase": password,
            "passphrase_reset_link_expiry_duration": link_expiration,
            "passphrase_reset_on_login": password_reset_on_login
        }
        return fortidlp_connection.send(url, params=data)

    def delete_operator(self, operator_id: str) -> dict:
        '''
        Description: Deletes the operator.
        Args:
            operator_id (str): The ID of the operator to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}'
        return fortidlp_connection.delete(url)

    def get_operator(self, operator_id: str) -> dict:
        '''
        Description: Gets the operator.
        Args:
            operator_id (str): The ID of the operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}'
        return fortidlp_connection.get(url)

    def update_operator(self, operator_id: str, username: Optional[str] = None, name: Optional[str] = None, email: Optional[str] = None, company: Optional[str] = None, roles: Optional[List[str]] = None) -> dict:
        '''
        Description: Updates the operator.
        Args:
            operator_id (str): The ID of the operator.
            username (str, optional): The new username of the operator.
            name (str, optional): The new display name of the operator.
            email (str, optional): The new email of the operator.
            company (str, optional): The new company of the operator.
            roles (list, optional): The new roles of the operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}'
        data = {"operator": {}}
        if username is not None:
            data["operator"]["name"] = username
        if name is not None:
            data["operator"]["display_name"] = name
        if email is not None:
            data["operator"]["email"] = email
        if company is not None:
            data["operator"]["company"] = company
        if roles is not None:
            data["operator"]["roles"] = roles
        return fortidlp_connection.put(url, json=data)

    def reset_mfa_authentication(self, operator_id: str) -> dict:
        '''
        Description: Resets MFA authentication for the operator.
        Args:
            operator_id (str): The ID of the operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}/mfa'
        return fortidlp_connection.delete(url)
