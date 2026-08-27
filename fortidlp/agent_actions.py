from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class AgentActions:
    '''
    Class AgentActions
    Description: Requests and monitors agent actions.
    '''

    def request_action(self, agent_ids: List[str], action_type: str, parameters: Optional[dict] = None) -> dict:
        '''
        Description: Request an agent to perform an action (Prior to agent version 10.5.3).
        Args:
            agent_ids (List[str]): List of agent IDs to perform the action on.
            action_type (str): The type of action to perform.
            parameters (dict, optional): Additional parameters for the action.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/actions'
        data = {
            "agent_ids": agent_ids,
            "action_type": action_type,
            "parameters": parameters
        }
        return fortidlp_connection.post(url, json=data)

    def unset_active_actions(self) -> dict:
        '''
        Description: Unset active actions.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/actions/active'
        return fortidlp_connection.delete(url)

    def query_active_actions(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Query active actions.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/actions/active'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def list_available_action_types(self) -> dict:
        '''
        Description: List available action types.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/actions/available'
        return fortidlp_connection.get(url)

    def query_supported_action_types(self, agent_ids: Optional[List[str]] = None) -> dict:
        '''
        Description: Query supported action types for one or more agents.
        Args:
            agent_ids (list, optional): List of agent IDs to query.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/actions/available'
        data = {}
        if agent_ids is not None:
            data["agent_ids"] = agent_ids
        return fortidlp_connection.post(url, json=data)

    def delete_debug_bundle(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Deletes the debug bundles taken as the result of an action on an agent.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the debug bundle.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/debug-bundles/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.delete(url)

    def get_debug_bundle(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Gets a debug bundle taken as the result of an action on an agent.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the debug bundle.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/debug-bundles/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.get(url)

    def delete_performance_report(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Deletes the performance report taken as the result of an action on an agent.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the performance report.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/performance-reports/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.delete(url)

    def get_performance_report(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Gets a performance report uploaded as the result of an action on an agent.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the performance report.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/performance-reports/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.get(url)

    def delete_screenshot(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Deletes the screenshot taken as the result of an action on an agent.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the screenshot.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/screenshots/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.delete(url)

    def get_screenshot(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Gets a screenshot taken as the result of an action on an agent.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the screenshot.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/screenshots/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.get(url)

    def trigger_action(self, agent_ids: List[str], action_type: str, parameters: Optional[dict] = None) -> dict:
        '''
        Description: Request an agent to perform an action. (Agent version 10.5.3 onwards).
        Args:
            agent_ids (List[str]): List of agent IDs to perform the action on.
            action_type (str): The type of action to perform.
            parameters (dict, optional): Additional parameters for the action.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/actions/trigger'
        data = {
            "agent_ids": agent_ids,
            "action_type": action_type,
            "parameters": parameters
        }
        return fortidlp_connection.post(url, json=data)

    def list_in_flight_actions(self, agent_uuid: str) -> dict:
        '''
        Description: List in-flight actions that have been triggered but are not yet complete.
        Args:
            agent_uuid (str): The UUID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/{agent_uuid}/in-flight'
        return fortidlp_connection.get(url)

    def delete_action_content(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Deletes action content.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the action content.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.delete(url)

    def get_action_content(self, agent_uuid: str, action_uuid: str, filename: str) -> dict:
        '''
        Description: Gets action content.
        Args:
            agent_uuid (str): The UUID of the agent.
            action_uuid (str): The UUID of the action.
            filename (str): The filename of the action content.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/actions/{agent_uuid}/{action_uuid}/{filename}'
        return fortidlp_connection.get(url)
