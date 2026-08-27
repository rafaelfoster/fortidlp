from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class GlobalOperators:
    '''
    Class GlobalOperators
    Description: Manages global operators.
    '''

    def delete_global_operator(self, operator_id: str) -> dict:
        '''
        Description: Deletes the specified global operator.
        Args:
            operator_id (str): The ID of the global operator to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/global-operators/{operator_id}'
        return fortidlp_connection.delete(url)

    def get_global_operator(self, operator_id: str) -> dict:
        '''
        Description: Gets the specified global operator.
        Args:
            operator_id (str): The ID of the global operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/global-operators/{operator_id}'
        return fortidlp_connection.get(url)

    def search_global_operators(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Gets a list of global operators matching an optional filter.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/global-operators/search'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_global_operators_terms(self) -> dict:
        '''
        Description: Gets available search terms for filtering global operators.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/global-operators/terms'
        return fortidlp_connection.get(url)
