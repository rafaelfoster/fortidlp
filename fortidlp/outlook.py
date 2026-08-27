from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Outlook:
    '''
    Class Outlook
    Description: Manages Outlook add-in configuration.
    '''

    def delete_outlook_certificate(self) -> dict:
        '''
        Description: Deletes the Outlook certificate.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/outloook/certificate'
        return fortidlp_connection.delete(url)

    def get_outlook_certificate(self) -> dict:
        '''
        Description: Gets the Outlook certificate.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/outloook/certificate'
        return fortidlp_connection.get(url)

    def upload_outlook_certificate(self, certificate_content: bytes, content_type: str) -> dict:
        '''
        Description: Uploads the Outlook certificate.
        Args:
            certificate_content (bytes): The content of the certificate file.
            content_type (str): The content type of the certificate file.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/outloook/certificate'
        files = {'file': ('certificate', certificate_content, content_type)}
        return fortidlp_connection.post(url, files=files)
