from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class DriveLabelsScheduledSync:
    '''
    Class DriveLabelsScheduledSync
    Description: Manages scheduled synchronization of Google Drive and Microsoft OneDrive labels.
    '''

    def schedule_google_drive_labels_sync(self, name: str, schedule: str) -> dict:
        '''
        Description: Schedules a synchronization for Google Drive labels.
        Args:
            name (str): The name of the sync schedule.
            schedule (str): The schedule for the sync (e.g., cron expression).
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/google/drive/labels/schedule-sync'
        data = {
            "name": name,
            "schedule": schedule
        }
        return fortidlp_connection.post(url, json=data)

    def list_google_drive_labels_sync_schedules(self) -> dict:
        '''
        Description: Lists scheduled synchronizations for Google Drive labels.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/google/drive/labels/schedule-sync/list'
        return fortidlp_connection.get(url)

    def delete_google_drive_labels_sync_schedule(self, uuid: str) -> dict:
        '''
        Description: Deletes a scheduled synchronization for Google Drive labels.
        Args:
            uuid (str): The UUID of the sync schedule to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/drive/labels/schedule-sync/{uuid}'
        return fortidlp_connection.delete(url)

    def get_google_drive_labels_sync_schedule(self, uuid: str) -> dict:
        '''
        Description: Gets a scheduled synchronization for Google Drive labels by UUID.
        Args:
            uuid (str): The UUID of the sync schedule.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/drive/labels/schedule-sync/{uuid}'
        return fortidlp_connection.get(url)

    def update_google_drive_labels_sync_schedule(self, uuid: str, name: Optional[str] = None, schedule: Optional[str] = None) -> dict:
        '''
        Description: Updates a scheduled synchronization for Google Drive labels.
        Args:
            uuid (str): The UUID of the sync schedule.
            name (str, optional): The new name for the sync schedule.
            schedule (str, optional): The new schedule for the sync.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/google/drive/labels/schedule-sync/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if schedule is not None:
            data["schedule"] = schedule
        return fortidlp_connection.put(url, json=data)

    def schedule_microsoft_onedrive_labels_sync(self, name: str, schedule: str) -> dict:
        '''
        Description: Schedules a synchronization for Microsoft OneDrive labels.
        Args:
            name (str): The name of the sync schedule.
            schedule (str): The schedule for the sync (e.g., cron expression).
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/onedrive/labels/schedule-sync'
        data = {
            "name": name,
            "schedule": schedule
        }
        return fortidlp_connection.post(url, json=data)

    def list_microsoft_onedrive_labels_sync_schedules(self) -> dict:
        '''
        Description: Lists scheduled synchronizations for Microsoft OneDrive labels.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/microsoft/onedrive/labels/schedule-sync/list'
        return fortidlp_connection.get(url)

    def delete_microsoft_onedrive_labels_sync_schedule(self, uuid: str) -> dict:
        '''
        Description: Deletes a scheduled synchronization for Microsoft OneDrive labels.
        Args:
            uuid (str): The UUID of the sync schedule to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/labels/schedule-sync/{uuid}'
        return fortidlp_connection.delete(url)

    def get_microsoft_onedrive_labels_sync_schedule(self, uuid: str) -> dict:
        '''
        Description: Gets a scheduled synchronization for Microsoft OneDrive labels by UUID.
        Args:
            uuid (str): The UUID of the sync schedule.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/labels/schedule-sync/{uuid}'
        return fortidlp_connection.get(url)

    def update_microsoft_onedrive_labels_sync_schedule(self, uuid: str, name: Optional[str] = None, schedule: Optional[str] = None) -> dict:
        '''
        Description: Updates a scheduled synchronization for Microsoft OneDrive labels.
        Args:
            uuid (str): The UUID of the sync schedule.
            name (str, optional): The new name for the sync schedule.
            schedule (str, optional): The new schedule for the sync.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/microsoft/onedrive/labels/schedule-sync/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if schedule is not None:
            data["schedule"] = schedule
        return fortidlp_connection.put(url, json=data)
