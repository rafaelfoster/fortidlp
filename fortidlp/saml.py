from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class SAML:
    '''
    Class SAML
    Description: Configures a SAML authentication provider.
    '''

    def delete_saml_config(self) -> dict:
        '''
        Description: Delete the SAML configuration for the operator's tenant.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/config'
        return fortidlp_connection.delete(url)

    def get_saml_config(self) -> dict:
        '''
        Description: Get the SAML configuration for the operator's tenant.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/config'
        return fortidlp_connection.get(url)

    def edit_saml_config(self, config: dict) -> dict:
        '''
        Description: Edit the SAML configuration for the operator's tenant.
        Args:
            config (dict): The SAML configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/config'
        return fortidlp_connection.put(url, json=config)

    def delete_cryptographic_keys(self) -> dict:
        '''
        Description: Delete cryptographic keys in use for SAML configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/cryptokeys'
        return fortidlp_connection.delete(url)

    def get_saml_certificate(self) -> dict:
        '''
        Description: Return the currently configured SAML certificate for the tenant.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/cryptokeys'
        return fortidlp_connection.get(url)

    def generate_cryptographic_keys(self) -> dict:
        '''
        Description: Generate cryptographic keys (self-signed RSA certificate).
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/cryptokeys'
        return fortidlp_connection.post(url)

    def upload_cryptographic_keys(self, certificate_content: bytes, content_type: str) -> dict:
        '''
        Description: Allows a cryptographic key and its corresponding certificate (with embedded public key) to be uploaded.
        Args:
            certificate_content (bytes): The content of the certificate file.
            content_type (str): The content type of the certificate file.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/cryptokeys'
        files = {'file': ('certificate', certificate_content, content_type)}
        return fortidlp_connection.put(url, files=files)

    def get_saml_info(self) -> dict:
        '''
        Description: Get basic information (ACS URL and audience URI) for the operator's tenant.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/saml/info'
        return fortidlp_connection.get(url)
