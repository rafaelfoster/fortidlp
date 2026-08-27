from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class SavedQueries:
    '''
    Class SavedQueries
    Description: Managed saved queries for the Investigate module.
    '''

    def list_saved_queries(self) -> dict:
        '''
        Description: Lists saved queries.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/search/queries'
        return fortidlp_connection.get(url)

    def create_saved_query(self, name: str, query: str, description: Optional[str] = None) -> dict:
        '''
        Description: Create a saved query.
        Args:
            name (str): The name of the saved query.
            query (str): The query string.
            description (str, optional): The description of the saved query.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/search/queries'
        data = {
            "name": name,
            "query": query
        }
        if description is not None:
            data["description"] = description
        return fortidlp_connection.post(url, json=data)

    def delete_saved_query(self, uuid: str) -> dict:
        '''
        Description: Delete a saved query.
        Args:
            uuid (str): The UUID of the saved query to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/search/queries/{uuid}'
        return fortidlp_connection.delete(url)

    def get_saved_query_by_uuid(self, uuid: str) -> dict:
        '''
        Description: Get a saved query by UUID.
        Args:
            uuid (str): The UUID of the saved query.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/search/queries/{uuid}'
        return fortidlp_connection.get(url)

    def update_saved_query(self, uuid: str, name: Optional[str] = None, query: Optional[str] = None, description: Optional[str] = None) -> dict:
        '''
        Description: Update a saved query.
        Args:
            uuid (str): The UUID of the saved query.
            name (str, optional): The new name for the saved query.
            query (str, optional): The new query string.
            description (str, optional): The new description for the saved query.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/search/queries/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if query is not None:
            data["query"] = query
        if description is not None:
            data["description"] = description
        return fortidlp_connection.put(url, json=data)
