from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Siem:
    '''
    Class Siem
    Description: Configures SIEM export streams.
    '''

    def list_siem_streams(self) -> dict:
        '''
        Description: Lists all configured SIEM streams.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/siem'
        return fortidlp_connection.get(url)
