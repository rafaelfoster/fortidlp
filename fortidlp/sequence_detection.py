from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class SequenceDetection:
    '''
    Class SequenceDetection
    Description: Manages Sequence Detection Definitions.
    '''

    def get_bounded_definitions(self) -> dict:
        '''
        Description: Gets bounded definitions.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/sequence-detections/bounded-definitions'
        return fortidlp_connection.get(url)

    def get_bounded_definitions_entity_count(self, uuid: str) -> dict:
        '''
        Description: Gets bounded definitions entity count.
        Args:
            uuid (str): The UUID of the definition.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/sequence-detections/bounded-definitions/{uuid}/entity-count'
        return fortidlp_connection.get(url)

    def get_definitions(self) -> dict:
        '''
        Description: Gets definitions.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/sequence-detections/definitions'
        return fortidlp_connection.get(url)

    def create_definition(self, name: str, description: Optional[str] = None, definition_data: Optional[dict] = None) -> dict:
        '''
        Description: Creates a new definition.
        Args:
            name (str): The name of the definition.
            description (str, optional): The description of the definition.
            definition_data (dict, optional): The definition data.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/sequence-detections/definitions'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if definition_data is not None:
            data["definition_data"] = definition_data
        return fortidlp_connection.post(url, json=data)

    def delete_definition(self, uuid: str) -> dict:
        '''
        Description: Deletes a definition.
        Args:
            uuid (str): The UUID of the definition to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/sequence-detections/definitions/{uuid}'
        return fortidlp_connection.delete(url)

    def get_definition(self, uuid: str) -> dict:
        '''
        Description: Gets a definition.
        Args:
            uuid (str): The UUID of the definition.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/sequence-detections/definitions/{uuid}'
        return fortidlp_connection.get(url)

    def update_definition(self, uuid: str, name: Optional[str] = None, description: Optional[str] = None, definition_data: Optional[dict] = None) -> dict:
        '''
        Description: Updates a definition.
        Args:
            uuid (str): The UUID of the definition.
            name (str, optional): The new name for the definition.
            description (str, optional): The new description for the definition.
            definition_data (dict, optional): The new definition data.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/sequence-detections/definitions/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if definition_data is not None:
            data["definition_data"] = definition_data
        return fortidlp_connection.put(url, json=data)

    def publish_definition(self, uuid: str) -> dict:
        '''
        Description: Publishes a definition.
        Args:
            uuid (str): The UUID of the definition to publish.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/sequence-detections/definitions/{uuid}/publish'
        return fortidlp_connection.post(url)
