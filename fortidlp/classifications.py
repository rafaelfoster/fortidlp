from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Classifications:
    '''
    Class Classifications
    Description: Gets agent classification categories.
    '''

    def get_all_classifications(self) -> dict:
        '''
        Description: Return all classifications.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/classifications'
        return fortidlp_connection.get(url)

    def get_classification_by_id(self, classification_id: str) -> dict:
        '''
        Description: Return classification by id.
        Args:
            classification_id (str): The ID of the classification.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/classifications/{classification_id}'
        return fortidlp_connection.get(url)
