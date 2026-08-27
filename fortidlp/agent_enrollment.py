from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class AgentEnrollment:
    '''
    Class AgentEnrollment
    Description: Create and manage agent enrollment tokens.
    '''   

    def get_bootstrap_token(self) -> dict:
        '''
        Description: Get bootstrap token for agent enrollment.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/enrollment/bootstrap-token'
        return fortidlp_connection.get(url)

    def get_agent_enrollment_tokens(self) -> dict:
        '''
        Description: Gets agent enrollment tokens.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/enrollment/tokens'
        return fortidlp_connection.get(url)

    def create_agent_enrollment_token(self, name: str, description: Optional[str] = None) -> dict:
        '''
        Description: Creates an agent enrollment token.
        Args:
            name (str): The name of the enrollment token.
            description (str, optional): The description of the enrollment token.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/enrollment/tokens'
        data = {
            "name": name,
            "description": description
        }
        return fortidlp_connection.post(url, json=data)

    def get_agent_enrollment_token_by_id(self, token_id: str) -> dict:
        '''
        Description: Get agent enrollment token by ID.
        Args:
            token_id (str): The ID of the enrollment token.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/enrollment/tokens/{token_id}'
        return fortidlp_connection.get(url)

    def update_enroll_token_configuration(self, token_id: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        '''
        Description: Update enroll token configuration.
        Args:
            token_id (str): The ID of the enrollment token.
            name (str, optional): The new name for the enrollment token.
            description (str, optional): The new description for the enrollment token.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/enrollment/tokens/{token_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return fortidlp_connection.put(url, json=data)

    def download_enrollment_bundle(self, token_id: str) -> dict:
        '''
        Description: Download the enrollment bundle specified in the request.
        Args:
            token_id (str): The ID of the enrollment token.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/enrollment/tokens/{token_id}/bundle'
        return fortidlp_connection.get(url)

    def revoke_enroll_token(self, token_id: str) -> dict:
        '''
        Description: Revoke enroll token.
        Args:
            token_id (str): The ID of the enrollment token.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/enrollment/tokens/{token_id}/revoke'
        return fortidlp_connection.post(url)
