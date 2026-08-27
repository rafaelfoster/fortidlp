from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Emails:
    '''
    Class Emails
    Description: Configures email notifications.
    '''

    def list_all_email_notifications(self) -> dict:
        '''
        Description: Lists all email notifications.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/emails'
        return fortidlp_connection.get(url)

    def register_new_email_notification(self, name: str, to_address: str, subject: str, body: str) -> dict:
        '''
        Description: Registers a new email notification.
        Args:
            name (str): The name of the email notification.
            to_address (str): The recipient email address.
            subject (str): The subject of the email.
            body (str): The body of the email.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/emails'
        data = {
            "name": name,
            "to_address": to_address,
            "subject": subject,
            "body": body
        }
        return fortidlp_connection.post(url, json=data)

    def verify_emails(self) -> dict:
        '''
        Description: Verifies emails.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/emails-verify'
        return fortidlp_connection.get(url)

    def delete_email_notification(self, email_id: str) -> dict:
        '''
        Description: Deletes the email notification.
        Args:
            email_id (str): The ID of the email notification.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/emails/{email_id}'
        return fortidlp_connection.delete(url)

    def retrieve_email_notification_configuration(self, email_id: str) -> dict:
        '''
        Description: Retrieves the email notification configuration.
        Args:
            email_id (str): The ID of the email notification.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/emails/{email_id}'
        return fortidlp_connection.get(url)

    def update_email_notification_configuration(self, email_id: str, name: Optional[str] = None, to_address: Optional[str] = None, subject: Optional[str] = None, body: Optional[str] = None) -> dict:
        '''
        Description: Updates the email notification configuration.
        Args:
            email_id (str): The ID of the email notification.
            name (str, optional): The new name for the email notification.
            to_address (str, optional): The new recipient email address.
            subject (str, optional): The new subject of the email.
            body (str, optional): The new body of the email.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/emails/{email_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if to_address is not None:
            data["to_address"] = to_address
        if subject is not None:
            data["subject"] = subject
        if body is not None:
            data["body"] = body
        return fortidlp_connection.put(url, json=data)

    def send_verification_email(self, email_id: str) -> dict:
        '''
        Description: Sends a verification email to the to_address of the email notification.
        Args:
            email_id (str): The ID of the email notification.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/emails/{email_id}/verify'
        return fortidlp_connection.post(url)
