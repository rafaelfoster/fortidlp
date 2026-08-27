from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Quota:
    '''
    Class Quota
    Description: Manages tenant usage quotas.
    '''

    def get_license_status(self) -> dict:
        '''
        Description: Get tenant's maximum number of enrolled agents.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/license/status'
        return fortidlp_connection.get(url)
