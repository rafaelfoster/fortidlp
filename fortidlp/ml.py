from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class ML:
    '''
    Class ML
    Description: Configures agent offline config.
    '''

    def get_agent_offline_config(self) -> dict:
        '''
        Description: Gets agent offline config.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/ml/agentoffline/config'
        return fortidlp_connection.get(url)

    def update_agent_offline_config(self, config: dict) -> dict:
        '''
        Description: Updates agent offline config.
        Args:
            config (dict): The configuration for agent offline.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/ml/agentoffline/config'
        return fortidlp_connection.put(url, json=config)
