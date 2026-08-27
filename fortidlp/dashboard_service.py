from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class DashboardService:
    '''
    Class DashboardService
    Description: Manages dashboards.
    '''

    def get_dashboards(self) -> dict:
        '''
        Description: Lists dashboards.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/dashboards'
        return fortidlp_connection.get(url)

    def create_dashboard(self, name: str, description: Optional[str] = None, config: Optional[dict] = None) -> dict:
        '''
        Description: Creates a new dashboard.
        Args:
            name (str): The name of the dashboard.
            description (str, optional): The description of the dashboard.
            config (dict, optional): The configuration of the dashboard.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/dashboards'
        data = {
            "name": name,
            "description": description,
            "config": config
        }
        return fortidlp_connection.post(url, json=data)

    def get_dashboard_templates(self) -> dict:
        '''
        Description: Lists dashboard templates.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/dashboards/templates'
        return fortidlp_connection.get(url)

    def delete_dashboard(self, uuid: str) -> dict:
        '''
        Description: Deletes a dashboard.
        Args:
            uuid (str): The UUID of the dashboard to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/dashboards/{uuid}'
        return fortidlp_connection.delete(url)

    def get_dashboard_by_uuid(self, uuid: str) -> dict:
        '''
        Description: Gets a dashboard by UUID.
        Args:
            uuid (str): The UUID of the dashboard.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/dashboards/{uuid}'
        return fortidlp_connection.get(url)

    def update_dashboard(self, uuid: str, name: Optional[str] = None, description: Optional[str] = None, config: Optional[dict] = None) -> dict:
        '''
        Description: Updates a dashboard.
        Args:
            uuid (str): The UUID of the dashboard.
            name (str, optional): The new name for the dashboard.
            description (str, optional): The new description for the dashboard.
            config (dict, optional): The new configuration for the dashboard.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/dashboards/{uuid}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if config is not None:
            data["config"] = config
        return fortidlp_connection.put(url, json=data)
