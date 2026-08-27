from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Cases:
    '''
    Class Cases
    Description: Creates, manages and adds content to cases.
    '''

    def get_cases(self, content_event_uri: Optional[str] = None, content_operated_by: Optional[str] = None, created_by: Optional[str] = None) -> dict:
        '''
        Description: Return info of all cases that match QueryCasesRequest.
        Args:
            content_event_uri (str, optional): Content event URI filter.
            content_operated_by (str, optional): Content operated by filter.
            created_by (str, optional): Created by filter.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/cases'
        params = {}
        if content_event_uri is not None:
            params["content_event_uri"] = content_event_uri
        if content_operated_by is not None:
            params["content_operated_by"] = content_operated_by
        if created_by is not None:
            params["created_by"] = created_by
        return fortidlp_connection.get(url, params=params)

    def create_case(self, name: str, description: Optional[str] = None) -> dict:
        '''
        Description: Create a new case.
        Args:
            name (str): The name of the case.
            description (str, optional): The description of the case.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/cases'
        data = {
            "name": name,
            "description": description
        }
        return fortidlp_connection.post(url, json=data)

    def delete_case(self, case_id: str) -> dict:
        '''
        Description: Delete a case.
        Args:
            case_id (str): The ID of the case.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}'
        return fortidlp_connection.delete(url)

    def get_case_by_id(self, case_id: str) -> dict:
        '''
        Description: Return info of an individual case by ID.
        Args:
            case_id (str): The ID of the case.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}'
        return fortidlp_connection.get(url)

    def update_case(self, case_id: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        '''
        Description: Update a case.
        Args:
            case_id (str): The ID of the case.
            name (str, optional): The new name for the case.
            description (str, optional): The new description for the case.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return fortidlp_connection.put(url, json=data)

    def assign_case(self, case_id: str, operator_uri: str) -> dict:
        '''
        Description: Assign a case to an operator by operator URI.
        Args:
            case_id (str): The ID of the case.
            operator_uri (str): The URI of the operator to assign the case to.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/assign'
        data = {"operator_uri": operator_uri}
        return fortidlp_connection.post(url, json=data)

    def get_case_content(self, case_id: str) -> dict:
        '''
        Description: Return contents of a case by ID.
        Args:
            case_id (str): The ID of the case.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/content'
        return fortidlp_connection.get(url)

    def add_case_content(self, case_id: str, content_uuid: str) -> dict:
        '''
        Description: Add contents to a case.
        Args:
            case_id (str): The ID of the case.
            content_uuid (str): The UUID of the content to add.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/content'
        data = {"content_uuid": content_uuid}
        return fortidlp_connection.post(url, json=data)

    def delete_case_content(self, case_id: str, content_uuid: str) -> dict:
        '''
        Description: Delete contents of a case.
        Args:
            case_id (str): The ID of the case.
            content_uuid (str): The UUID of the content to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/content/{content_uuid}'
        return fortidlp_connection.delete(url)

    def update_case_content(self, case_id: str, content_uuid: str, new_content_uuid: str) -> dict:
        '''
        Description: Update the contents of a case.
        Args:
            case_id (str): The ID of the case.
            content_uuid (str): The UUID of the content to update.
            new_content_uuid (str): The new UUID for the content.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/content/{content_uuid}'
        data = {"content_uuid": new_content_uuid}
        return fortidlp_connection.put(url, json=data)

    def get_case_content_image(self, case_id: str, filename: str) -> dict:
        '''
        Description: Get image for case content.
        Args:
            case_id (str): The ID of the case.
            filename (str): The filename of the image.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/content/{filename}'
        return fortidlp_connection.get(url)

    def add_case_image(self, case_id: str, image_content: bytes, content_type: str) -> dict:
        '''
        Description: Add image to a case.
        Args:
            case_id (str): The ID of the case.
            image_content (bytes): The content of the image as bytes.
            content_type (str): The content type of the image (e.g., "image/jpeg").
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/image'
        files = {'file': ('image', image_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def unassign_case(self, case_id: str, operator_uri: str) -> dict:
        '''
        Description: Unassign a case from an operator by operator URI.
        Args:
            case_id (str): The ID of the case.
            operator_uri (str): The URI of the operator to unassign the case from.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/cases/{case_id}/unassign'
        data = {"operator_uri": operator_uri}
        return fortidlp_connection.post(url, json=data)
