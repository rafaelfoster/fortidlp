from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Search:
    '''
    Class Search
    Description: Gets available search parameters.
    '''

    def get_search_terms(self) -> dict:
        '''
        Description: Gets available search parameters.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/search/terms'
        return fortidlp_connection.get(url)
