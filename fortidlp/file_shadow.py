from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class FileShadow:
    '''
    Class FileShadow
    Description: Manages file shadow configurations and evidence.
    '''

    def delete_file_shadow_config(self) -> dict:
        '''
        Description: Deletes the file shadow configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/fileshadow/config'
        return fortidlp_connection.delete(url)

    def get_file_shadow_config(self) -> dict:
        '''
        Description: Gets the file shadow configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/fileshadow/config'
        return fortidlp_connection.get(url)

    def update_file_shadow_config(self, config: dict) -> dict:
        '''
        Description: Updates the file shadow configuration.
        Args:
            config (dict): The file shadow configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/fileshadow/config'
        return fortidlp_connection.put(url, json=config)

    def test_file_shadow_config(self) -> dict:
        '''
        Description: Tests the file shadow configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/fileshadow/config/test'
        return fortidlp_connection.get(url)

    def get_file_shadow_decryption_tool(self) -> dict:
        '''
        Description: Gets the file shadow decryption tool.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/fileshadow/decryption-tool'
        return fortidlp_connection.get(url)

    def get_file_shadow_evidence_by_action_uuid(self, action_uuid: str) -> dict:
        '''
        Description: Redirects the user to download a file shadow evidence file.
        Args:
            action_uuid (str): The UUID of the action.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/fileshadow/evidence/{action_uuid}'
        return fortidlp_connection.get(url)

    def get_file_shadow_evidence_by_agent_action_uuid(self, agent_uuid: str, action_uuid: str) -> dict:
        '''
        Description: Redirects the user to download a file shadow evidence file.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/fileshadow/evidence/{agent_uuid}/{action_uuid}'
        return fortidlp_connection.get(url)

    def get_file_shadow_recipients(self) -> dict:
        '''
        Description: Gets file shadow recipients.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/fileshadow/recipients'
        return fortidlp_connection.get(url)

    def delete_file_shadow_recipient(self, name: str) -> dict:
        '''
        Description: Deletes a file shadow recipient.
        Args:
            name (str): The name of the recipient to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/fileshadow/recipients/{name}'
        return fortidlp_connection.delete(url)

    def get_file_shadow_recipient(self, name: str) -> dict:
        '''
        Description: Gets a file shadow recipient.
        Args:
            name (str): The name of the recipient.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/fileshadow/recipients/{name}'
        return fortidlp_connection.get(url)

    def update_file_shadow_recipient(self, name: str, recipient_data: dict) -> dict:
        '''
        Description: Updates a file shadow recipient.
        Args:
            name (str): The name of the recipient to update.
            recipient_data (dict): The updated recipient data.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/fileshadow/recipients/{name}'
        return fortidlp_connection.put(url, json=recipient_data)

    def get_clipboard_evidence(self, agent_uuid: str, action_uuid: str) -> dict:
        '''
        Description: Redirects the user to download a clipboard evidence file.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/forensic-evidence/clipboard/{agent_uuid}/{action_uuid}'
        return fortidlp_connection.get(url)

    def get_file_shadow_forensic_evidence(self, agent_uuid: str, action_uuid: str) -> dict:
        '''
        Description: Redirects the user to download a file shadow evidence file.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/forensic-evidence/fileshadow/{agent_uuid}/{action_uuid}'
        return fortidlp_connection.get(url)

    def get_screenshot_evidence(self, agent_uuid: str, action_uuid: str) -> dict:
        '''
        Description: Redirects the user to download a screenshot evidence file.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/forensic-evidence/screenshot/{agent_uuid}/{action_uuid}'
        return fortidlp_connection.get(url)
