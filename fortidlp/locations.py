from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Locations:
    '''
    Class Locations
    Description: Manages custom geo-locations and subnets.
    '''

    def get_locations(self) -> dict:
        '''
        Description: Lists all locations.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/locations'
        return fortidlp_connection.get(url)

    def create_location(self, name: str, description: Optional[str] = None) -> dict:
        '''
        Description: Creates a new location.
        Args:
            name (str): The name of the location.
            description (str, optional): The description of the location.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/locations'
        data = {
            "name": name,
            "description": description
        }
        return fortidlp_connection.post(url, json=data)

    def query_locations(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Queries locations.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/locations/query'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def delete_location(self, location_id: str) -> dict:
        '''
        Description: Deletes a location.
        Args:
            location_id (str): The ID of the location to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}'
        return fortidlp_connection.delete(url)

    def get_location_by_id(self, location_id: str) -> dict:
        '''
        Description: Gets a location by ID.
        Args:
            location_id (str): The ID of the location.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}'
        return fortidlp_connection.get(url)

    def update_location(self, location_id: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        '''
        Description: Updates a location.
        Args:
            location_id (str): The ID of the location.
            name (str, optional): The new name for the location.
            description (str, optional): The new description for the location.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return fortidlp_connection.put(url, json=data)

    def get_location_subnets(self, location_id: str) -> dict:
        '''
        Description: Gets subnets for a location.
        Args:
            location_id (str): The ID of the location.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}/subnets'
        return fortidlp_connection.get(url)

    def create_location_subnet(self, location_id: str, subnet: str) -> dict:
        '''
        Description: Creates a new subnet for a location.
        Args:
            location_id (str): The ID of the location.
            subnet (str): The subnet to add.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}/subnets'
        data = {"subnet": subnet}
        return fortidlp_connection.post(url, json=data)

    def delete_location_subnet(self, location_id: str, subnet_id: str) -> dict:
        '''
        Description: Deletes a subnet from a location.
        Args:
            location_id (str): The ID of the location.
            subnet_id (str): The ID of the subnet to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}/subnets/{subnet_id}'
        return fortidlp_connection.delete(url)

    def get_location_subnet_by_id(self, location_id: str, subnet_id: str) -> dict:
        '''
        Description: Gets a subnet by ID for a location.
        Args:
            location_id (str): The ID of the location.
            subnet_id (str): The ID of the subnet.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/locations/{location_id}/subnets/{subnet_id}'
        return fortidlp_connection.get(url)
