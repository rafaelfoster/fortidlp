from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class EntitiesSearch:
    '''
    Class EntitiesSearch
    Description: Searches or aggregates over a set of entities.
    '''

    def aggregate_agents(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Aggregate agents.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/aggregate'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_agent_archive_config(self) -> dict:
        '''
        Description: Retrieve configuration for agent archivation rules.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/archive/config'
        return fortidlp_connection.get(url)

    def update_agent_archive_config(self, config: dict) -> dict:
        '''
        Description: Updates configuration for tenant.
        Args:
            config (dict): The configuration for agent archiving.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/archive/config'
        return fortidlp_connection.put(url, json=config)

    def get_agent_components(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Gets a list of agent components for agents matching the filter.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/components'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_agent_components_faults(self) -> dict:
        '''
        Description: Lists faulty components grouped by agent operating system, component and state.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/components/faults'
        return fortidlp_connection.get(url)

    def suppress_agent_components(self, filter: Optional[List[str]] = None, components: Optional[List[str]] = None) -> dict:
        '''
        Description: Suppresses the specified components for agents matching a filter.
        Args:
            filter (list, optional): List of filters to apply.
            components (list, optional): List of components to suppress.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/components/suppress'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if components is not None:
            data["components"] = components
        return fortidlp_connection.post(url, json=data)

    def get_agent_components_terms(self) -> dict:
        '''
        Description: Retrieves all terms for agent components.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/components/terms'
        return fortidlp_connection.get(url)

    def unsuppress_agent_components(self, filter: Optional[List[str]] = None, components: Optional[List[str]] = None) -> dict:
        '''
        Description: Unsuppresses the specified components for agents matching a filter.
        Args:
            filter (list, optional): List of filters to apply.
            components (list, optional): List of components to unsuppress.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/components/unsuppress'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if components is not None:
            data["components"] = components
        return fortidlp_connection.post(url, json=data)

    def export_agents_csv(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports agents search as CSV data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/export/csv'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def get_agent_export_fields(self) -> dict:
        '''
        Description: Returns all possible fields that can be exported for agents and whether each field is included by default.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/export/fields'
        return fortidlp_connection.get(url)

    def export_agents_xlsx(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports agents search as XLSX data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/export/xlsx'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def add_labels_to_agents(self, filter: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Add labels to agents.
        Args:
            filter (list, optional): List of filters to apply.
            labels (list, optional): List of labels to add.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/labels/add'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if labels is not None:
            data["labels"] = labels
        return fortidlp_connection.post(url, json=data)

    def remove_labels_from_agents(self, filter: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Remove labels from agents.
        Args:
            filter (list, optional): List of filters to apply.
            labels (list, optional): List of labels to remove.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/labels/remove'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if labels is not None:
            data["labels"] = labels
        return fortidlp_connection.post(url, json=data)

    def revoke_agent_licenses(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Revokes the licenses of agents that match the provided filter.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/revoke'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def search_agents(self, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches agents.
        Args:
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def change_agent_state(self, state: str, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Changes agent state to specified in request state.
        Args:
            state (str): The new state for the agents.
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/state'
        data = {"state": state}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_agent_terms(self) -> dict:
        '''
        Description: Retrieves all terms for agents.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/agents/terms'
        return fortidlp_connection.get(url)

    def get_target_agent(self, uuid: str) -> dict:
        '''
        Description: Get a target agent.
        Args:
            uuid (str): The UUID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/agents/{uuid}'
        return fortidlp_connection.get(url)

    def get_agent_components_health(self, uuid: str) -> dict:
        '''
        Description: Gets the health for the agent's components.
        Args:
            uuid (str): The UUID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/agents/{uuid}/components'
        return fortidlp_connection.get(url)

    def suppress_agent_components_by_uuid(self, uuid: str, components: Optional[List[str]] = None) -> dict:
        '''
        Description: Suppresses the specified components for the agent.
        Args:
            uuid (str): The UUID of the agent.
            components (list, optional): List of components to suppress.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/agents/{uuid}/components/suppress'
        data = {}
        if components is not None:
            data["components"] = components
        return fortidlp_connection.post(url, json=data)

    def unsuppress_agent_components_by_uuid(self, uuid: str, components: Optional[List[str]] = None) -> dict:
        '''
        Description: Unsuppresses the specified components for the agent.
        Args:
            uuid (str): The UUID of the agent.
            components (list, optional): List of components to unsuppress.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/agents/{uuid}/components/unsuppress'
        data = {}
        if components is not None:
            data["components"] = components
        return fortidlp_connection.post(url, json=data)

    def search_agent_users(self, uuid: str, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches users of a specific agent.
        Args:
            uuid (str): The UUID of the agent.
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/agents/{uuid}/users/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def aggregate_users(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Aggregate users.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/aggregate'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_user_archive_config(self) -> dict:
        '''
        Description: Gets configuration for user archiving.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/archive/config'
        return fortidlp_connection.get(url)

    def update_user_archive_config(self, config: dict) -> dict:
        '''
        Description: Updates configuration for tenant.
        Args:
            config (dict): The configuration for user archiving.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/archive/config'
        return fortidlp_connection.put(url, json=config)

    def bulk_assign_user_uris(self, user_uris: List[dict]) -> dict:
        '''
        Description: Bulk assign useruris.
        Args:
            user_uris (List[dict]): List of user URIs to assign.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/bulk/useruri'
        data = {"user_uris": user_uris}
        return fortidlp_connection.post(url, json=data)

    def export_users_csv(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports users search as CSV data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/export/csv'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def get_user_export_fields(self) -> dict:
        '''
        Description: Returns all possible fields that can be exported for users and whether each field is included by default.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/export/fields'
        return fortidlp_connection.get(url)

    def export_users_xlsx(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports users search as XLSX data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/export/xlsx'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def add_labels_to_users(self, filter: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Add labels to users.
        Args:
            filter (list, optional): List of filters to apply.
            labels (list, optional): List of labels to add.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/labels/add'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if labels is not None:
            data["labels"] = labels
        return fortidlp_connection.post(url, json=data)

    def remove_labels_from_users(self, filter: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Remove labels from users.
        Args:
            filter (list, optional): List of filters to apply.
            labels (list, optional): List of labels to remove.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/labels/remove'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if labels is not None:
            data["labels"] = labels
        return fortidlp_connection.post(url, json=data)

    def search_users(self, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches users.
        Args:
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def change_user_state(self, state: str, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Changes the state of users matching the filter to the requested state.
        Args:
            state (str): The new state for the users.
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/state'
        data = {"state": state}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_user_terms(self) -> dict:
        '''
        Description: Retrieves all terms for users.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/terms'
        return fortidlp_connection.get(url)

    def export_user_uris_csv(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports user URIs as CSV data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/users/useruri/export/csv'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def get_single_user(self, uuid: str) -> dict:
        '''
        Description: Gets a single user.
        Args:
            uuid (str): The UUID of the user.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/users/{uuid}'
        return fortidlp_connection.get(url)

    def search_user_agents(self, uuid: str, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches agents of a specific user.
        Args:
            uuid (str): The UUID of the user.
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/users/{uuid}/agents/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def get_user_photo(self, uuid: str) -> dict:
        '''
        Description: Gets the photo for a user by UUID.
        Args:
            uuid (str): The UUID of the user.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/users/{uuid}/photo'
        return fortidlp_connection.get(url)

    def get_user_uris(self, uuid: str) -> dict:
        '''
        Description: Gets the user URIs of a user by UUID.
        Args:
            uuid (str): The UUID of the user.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/users/{uuid}/useruri'
        return fortidlp_connection.get(url)

    def add_user_uri(self, uuid: str, user_uri: str) -> dict:
        '''
        Description: Add useruri to user by UUID.
        Args:
            uuid (str): The UUID of the user.
            user_uri (str): The user URI to add.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/users/{uuid}/useruri/add'
        data = {"user_uri": user_uri}
        return fortidlp_connection.post(url, json=data)

    def remove_user_uri(self, uuid: str, user_uri: str) -> dict:
        '''
        Description: Remove user URI from user by UUID.
        Args:
            uuid (str): The UUID of the user.
            user_uri (str): The user URI to remove.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/users/{uuid}/useruri/remove'
        data = {"user_uri": user_uri}
        return fortidlp_connection.post(url, json=data)
