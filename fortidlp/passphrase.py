from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Passphrase:
    '''
    Class Passphrase
    Description: Changes and resets operator passphrases.
    '''

    def get_forgotten_passphrase(self) -> dict:
        '''
        Description: Retrieves information about a forgotten passphrase.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/forgotten-passphrase'
        return fortidlp_connection.get(url)

    def invalidate_operator_passphrase(self, operator_id: str) -> dict:
        '''
        Description: Invalidates passphrase for operator.
        Args:
            operator_id (str): The ID of the operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}/passphrase'
        return fortidlp_connection.delete(url)

    def generate_passphrase_reset_link(self, operator_id: str) -> dict:
        '''
        Description: Generates passphrase reset link for operator.
        Args:
            operator_id (str): The ID of the operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}/passphrase/reset-link'
        return fortidlp_connection.post(url)

    def prompt_passphrase_reset_on_next_login(self, operator_id: str) -> dict:
        '''
        Description: Prompts the user to reset their passphrase on login.
        Args:
            operator_id (str): The ID of the operator.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/operators/{operator_id}/passphrase/reset-next-login'
        return fortidlp_connection.post(url)

    def set_passphrase(self, new_passphrase: str) -> dict:
        '''
        Description: Set passphrase for the operator (only callable with pw reset token).
        Args:
            new_passphrase (str): The new passphrase.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/passphrase'
        data = {"passphrase": new_passphrase}
        return fortidlp_connection.post(url, json=data)

    def change_passphrase(self, old_passphrase: str, new_passphrase: str) -> dict:
        '''
        Description: Change passphrase for the operator.
        Args:
            old_passphrase (str): The current passphrase.
            new_passphrase (str): The new passphrase.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/passphrase'
        data = {"old_passphrase": old_passphrase, "new_passphrase": new_passphrase}
        return fortidlp_connection.put(url, json=data)

    def get_passphrase_reset_info(self) -> dict:
        '''
        Description: Retrieves passphrase reset information.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/passphrase-reset'
        return fortidlp_connection.get(url)

    def test_passphrase(self, passphrase_to_test: str) -> dict:
        '''
        Description: Test passphrase for the operator.
        Args:
            passphrase_to_test (str): The passphrase to test.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/passphrase/test'
        data = {"passphrase": passphrase_to_test}
        return fortidlp_connection.post(url, json=data)
