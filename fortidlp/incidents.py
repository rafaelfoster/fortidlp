from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Incidents:
    '''
    Class Incidents
    Description: Handles Incidents.
    '''

    def count_agents_in_incidents(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Counts agents involved in incidents.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/agents/count'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def aggregate_incidents(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Aggregate incidents.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/aggregate'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_bounded_rule_entity_count(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Returns the number of bounded (rule, entity) pairs for the given incident filter.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/bounded-rule-entity-count'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def search_incidents(self, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "desc") -> dict:
        '''
        Description: Searches incidents.
        Args:
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def set_incident_status(self, status: str, all: Optional[bool] = None, filter: Optional[List[str]] = None, reason: Optional[str] = None) -> dict:
        '''
        Description: Sets the status of all the specified incidents to the chosen status (open/resolved).
        Args:
            status (str): The new status for the incidents.
            all (bool, optional): Whether to apply to all incidents.
            filter (list, optional): List of filters to apply.
            reason (str, optional): The reason for the status change.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/status'
        data = {"status": status}
        if all is not None:
            data["all"] = all
        if filter is not None:
            data["filter"] = filter
        if reason is not None:
            data["reason"] = reason
        return fortidlp_connection.post(url, json=data)

    def get_incident_terms(self) -> dict:
        '''
        Description: Retrieves all terms for incidents.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/terms'
        return fortidlp_connection.get(url)

    def count_users_in_incidents(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Counts users involved in incidents.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/incidents/users/count'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_single_incident(self, incident_id: str) -> dict:
        '''
        Description: Gets a single incident.
        Args:
            incident_id (str): The ID of the incident.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/incidents/{incident_id}'
        return fortidlp_connection.get(url)

    def search_incident_agents(self, incident_id: str, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches agents of a specific incident.
        Args:
            incident_id (str): The ID of the incident.
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/incidents/{incident_id}/agents/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def search_incident_labels(self, incident_id: str, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches labels of a specific incident.
        Args:
            incident_id (str): The ID of the incident.
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/incidents/{incident_id}/labels/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def search_incident_users(self, incident_id: str, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches users of a specific incident.
        Args:
            incident_id (str): The ID of the incident.
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/incidents/{incident_id}/users/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)
