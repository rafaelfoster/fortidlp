from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Microsoft:
    '''
    Class Microsoft
    Description: Manages Microsoft 365 integrations and configuration.
    '''

    def get_microsoft_credentials(self) -> dict:
        '''
        Description: Gets Microsoft credentials.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/credentials'
        return fortidlp_connection.get(url)

    def create_microsoft_credentials(self, client_id: str, client_secret: str, redirect_uris: List[str]) -> dict:
        '''
        Description: Creates Microsoft credentials.
        Args:
            client_id (str): The client ID.
            client_secret (str): The client secret.
            redirect_uris (List[str]): List of redirect URIs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/credentials'
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uris": redirect_uris
        }
        return fortidlp_connection.post(url, json=data)

    def verify_microsoft_credentials(self, credentials_id: str) -> dict:
        '''
        Description: Verifies Microsoft credentials.
        Args:
            credentials_id (str): The ID of the credentials to verify.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/credentials/{credentials_id}/verify'
        return fortidlp_connection.post(url)

    def delete_microsoft_credentials(self, uuid: str) -> dict:
        '''
        Description: Deletes Microsoft credentials.
        Args:
            uuid (str): The UUID of the credentials to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/credentials/{uuid}'
        return fortidlp_connection.delete(url)

    def get_microsoft_credentials_by_uuid(self, uuid: str) -> dict:
        '''
        Description: Gets Microsoft credentials by UUID.
        Args:
            uuid (str): The UUID of the credentials.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/credentials/{uuid}'
        return fortidlp_connection.get(url)

    def update_microsoft_credentials(self, uuid: str, client_id: Optional[str] = None, client_secret: Optional[str] = None, redirect_uris: Optional[List[str]] = None) -> dict:
        '''
        Description: Updates Microsoft credentials.
        Args:
            uuid (str): The UUID of the credentials.
            client_id (str, optional): The new client ID.
            client_secret (str, optional): The new client secret.
            redirect_uris (List[str], optional): The new list of redirect URIs.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/credentials/{uuid}'
        data = {}
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if redirect_uris is not None:
            data["redirect_uris"] = redirect_uris
        return fortidlp_connection.put(url, json=data)

    def get_microsoft_onedrive_files(self) -> dict:
        '''
        Description: Gets Microsoft OneDrive files.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/onedrive'
        return fortidlp_connection.get(url)

    def create_microsoft_onedrive_file(self, file_data: dict) -> dict:
        '''
        Description: Creates a Microsoft OneDrive file.
        Args:
            file_data (dict): The data for the file.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/onedrive'
        return fortidlp_connection.post(url, json=file_data)

    def get_microsoft_onedrive_labels(self) -> dict:
        '''
        Description: Gets Microsoft OneDrive labels.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/onedrive/labels'
        return fortidlp_connection.get(url)

    def sync_microsoft_onedrive_labels(self) -> dict:
        '''
        Description: Syncs Microsoft OneDrive labels.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/onedrive/labels/sync'
        return fortidlp_connection.put(url)

    def get_microsoft_onedrive_label_by_id(self, label_id: str) -> dict:
        '''
        Description: Gets Microsoft OneDrive label by ID.
        Args:
            label_id (str): The ID of the label.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/labels/{label_id}'
        return fortidlp_connection.get(url)

    def delete_microsoft_onedrive_file(self, file_id: str) -> dict:
        '''
        Description: Deletes a Microsoft OneDrive file.
        Args:
            file_id (str): The ID of the file to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/{file_id}'
        return fortidlp_connection.delete(url)

    def get_microsoft_onedrive_file_by_id(self, file_id: str) -> dict:
        '''
        Description: Gets a Microsoft OneDrive file by ID.
        Args:
            file_id (str): The ID of the file.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/{file_id}'
        return fortidlp_connection.get(url)

    def update_microsoft_onedrive_file(self, file_id: str, file_data: dict) -> dict:
        '''
        Description: Updates a Microsoft OneDrive file.
        Args:
            file_id (str): The ID of the file.
            file_data (dict): The updated data for the file.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/{file_id}'
        return fortidlp_connection.put(url, json=file_data)
