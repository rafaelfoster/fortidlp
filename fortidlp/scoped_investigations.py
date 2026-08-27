from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class ScopedInvestigations:
    '''
    Class ScopedInvestigations
    Description: Manages scoped investigations.
    '''

    def get_scoped_investigations(self) -> dict:
        '''
        Description: Fetches a list of scoped investigations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations'
        return fortidlp_connection.get(url)

    def assign_scoped_investigation(self, investigation_id: str, operator_id: str) -> dict:
        '''
        Description: Assigns a scoped investigation.
        Args:
            investigation_id (str): The ID of the investigation.
            operator_id (str): The ID of the operator to assign.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations'
        data = {
            "investigation_id": investigation_id,
            "operator_id": operator_id
        }
        return fortidlp_connection.post(url, json=data)

    def deactivate_active_scoped_investigation(self) -> dict:
        '''
        Description: Deactivates the active scoped investigation if present.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations/active'
        return fortidlp_connection.delete(url)

    def aggregate_scoped_investigations(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Aggregate scoped investigations.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations/aggregate'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_scoped_investigation_requests(self) -> dict:
        '''
        Description: Fetches a list of scoped investigation requests for the current operator.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations/requests'
        return fortidlp_connection.get(url)

    def request_scoped_investigation(self, name: str, description: Optional[str] = None) -> dict:
        '''
        Description: Requests a scoped investigation.
        Args:
            name (str): The name of the investigation request.
            description (str, optional): The description of the investigation request.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations/requests'
        data = {
            "name": name,
            "description": description
        }
        return fortidlp_connection.post(url, json=data)

    def aggregate_scoped_investigation_requests(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Aggregate scoped investigation requests.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations/requests/aggregate'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_scoped_investigation_request_details(self, uuid: str) -> dict:
        '''
        Description: Fetches the details of a scoped investigation for the current operator.
        Args:
            uuid (str): The UUID of the investigation request.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/requests/{uuid}'
        return fortidlp_connection.get(url)

    def update_scoped_investigation_request(self, uuid: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        '''
        Description: Updates a scoped investigation request for the current operator.
        Args:
            uuid (str): The UUID of the investigation request.
            name (str, optional): The new name for the request.
            description (str, optional): The new description for the request.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/requests/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return fortidlp_connection.post(url, json=data)

    def activate_scoped_investigation(self, uuid: str) -> dict:
        '''
        Description: Activates the specified scoped investigation.
        Args:
            uuid (str): The UUID of the investigation.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/requests/{uuid}/activate'
        return fortidlp_connection.post(url)

    def cancel_scoped_investigation_request(self, uuid: str) -> dict:
        '''
        Description: Cancels a request for a scoped investigation.
        Args:
            uuid (str): The UUID of the investigation request.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/requests/{uuid}/cancel'
        return fortidlp_connection.post(url)

    def get_scoped_investigation_terms(self) -> dict:
        '''
        Description: Fetches available search terms for filtering scoped investigations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/scoped-investigations/terms'
        return fortidlp_connection.get(url)

    def get_scoped_investigation_details(self, uuid: str) -> dict:
        '''
        Description: Fetches the details of a scoped investigation.
        Args:
            uuid (str): The UUID of the investigation.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/{uuid}'
        return fortidlp_connection.get(url)

    def update_scoped_investigation(self, uuid: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        '''
        Description: Updates a scoped investigation request.
        Args:
            uuid (str): The UUID of the investigation.
            name (str, optional): The new name for the investigation.
            description (str, optional): The new description for the investigation.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return fortidlp_connection.post(url, json=data)

    def approve_scoped_investigation(self, uuid: str) -> dict:
        '''
        Description: Update the scoped investigation and approve it.
        Args:
            uuid (str): The UUID of the investigation.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/{uuid}/approve'
        return fortidlp_connection.post(url)

    def revoke_scoped_investigation_access(self, uuid: str) -> dict:
        '''
        Description: Revokes access to the specified scoped investigation.
        Args:
            uuid (str): The UUID of the investigation.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/scoped-investigations/{uuid}/revoke'
        return fortidlp_connection.post(url)
