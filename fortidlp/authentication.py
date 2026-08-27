from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Authentication:
    '''
    Class Authentication
    Description: Handle user authentication.
    '''

    def login(self, username: str, password: str) -> dict:
        '''
        Description: Authenticate a user and obtain an access token.
        Args:
            username (str): The user's username.
            password (str): The user's password.
        Returns:
            dict: The response from the API, including access token.
        '''
        url = '/auth/login'
        data = {
            "username": username,
            "password": password
        }
        return fortidlp_connection.post(url, json=data)

    def logout(self) -> dict:
        '''
        Description: Invalidate the current session's access token.
        Returns:
            dict: The response from the API.
        '''
        url = '/auth/logout'
        return fortidlp_connection.post(url)

    def refresh_token(self) -> dict:
        '''
        Description: Refresh the current access token.
        Returns:
            dict: The response from the API, including a new access token.
        '''
        url = '/auth/refresh'
        return fortidlp_connection.post(url)

    def get_current_user(self) -> dict:
        '''
        Description: Get information about the currently authenticated user.
        Returns:
            dict: The response from the API, containing user details.
        '''
        url = '/auth/me'
        return fortidlp_connection.get(url)

    def get_users(self) -> dict:
        '''
        Description: Retrieve a list of all users.
        Returns:
            dict: The response from the API, containing a list of users.
        '''
        url = '/auth/users'
        return fortidlp_connection.get(url)

    def create_user(self, username: str, password: str, email: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, roles: Optional[List[str]] = None) -> dict:
        '''
        Description: Create a new user.
        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            email (str, optional): The email address of the new user.
            first_name (str, optional): The first name of the new user.
            last_name (str, optional): The last name of the new user.
            roles (list, optional): A list of roles for the new user.
        Returns:
            dict: The response from the API, containing the created user's details.
        '''
        url = '/auth/users'
        data = {
            "username": username,
            "password": password
        }
        if email is not None:
            data["email"] = email
        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if roles is not None:
            data["roles"] = roles
        return fortidlp_connection.post(url, json=data)

    def get_user_by_id(self, user_id: str) -> dict:
        '''
        Description: Retrieve a specific user by their ID.
        Args:
            user_id (str): The ID of the user.
        Returns:
            dict: The response from the API, containing user details.
        '''
        url = f'/auth/users/{user_id}'
        return fortidlp_connection.get(url)

    def update_user(self, user_id: str, email: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, password: Optional[str] = None, roles: Optional[List[str]] = None) -> dict:
        '''
        Description: Update a specific user by their ID.
        Args:
            user_id (str): The ID of the user.
            email (str, optional): The new email address for the user.
            first_name (str, optional): The new first name for the user.
            last_name (str, optional): The new last name for the user.
            password (str, optional): The new password for the user.
            roles (list, optional): The new list of roles for the user.
        Returns:
            dict: The response from the API, containing the updated user's details.
        '''
        url = f'/auth/users/{user_id}'
        data = {}
        if email is not None:
            data["email"] = email
        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if password is not None:
            data["password"] = password
        if roles is not None:
            data["roles"] = roles
        return fortidlp_connection.put(url, json=data)

    def delete_user(self, user_id: str) -> dict:
        '''
        Description: Delete a specific user by their ID.
        Args:
            user_id (str): The ID of the user.
        Returns:
            dict: The response from the API.
        '''
        url = f'/auth/users/{user_id}'
        return fortidlp_connection.delete(url)
