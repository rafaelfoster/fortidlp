from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Perspectives:
    '''
    Class Perspectives
    Description: Manages search perspectives.
    '''

    def get_all_perspectives(self) -> dict:
        '''
        Description: Return all perspectives.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/perspectives'
        return fortidlp_connection.get(url)

    def create_perspective(self, name: str, description: Optional[str] = None, config: Optional[dict] = None) -> dict:
        '''
        Description: Create a perspective.
        Args:
            name (str): The name of the perspective.
            description (str, optional): The description of the perspective.
            config (dict, optional): The configuration of the perspective.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/perspectives'
        data = {
            "name": name,
            "description": description,
            "config": config
        }
        return fortidlp_connection.post(url, json=data)

    def delete_perspective_by_id(self, perspective_id: str) -> dict:
        '''
        Description: Delete perspective by id.
        Args:
            perspective_id (str): The ID of the perspective to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/perspectives/{perspective_id}'
        return fortidlp_connection.delete(url)

    def get_perspective_by_id(self, perspective_id: str) -> dict:
        '''
        Description: Return perspective by id.
        Args:
            perspective_id (str): The ID of the perspective.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/perspectives/{perspective_id}'
        return fortidlp_connection.get(url)
