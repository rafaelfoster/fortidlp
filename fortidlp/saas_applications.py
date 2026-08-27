from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class SaaSApplications:
    '''
    Class SaaSApplications
    Description: Manages SaaS applications.
    '''

    def aggregate_saas_applications(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Aggregates SaaS applications.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/aggregate'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def allow_domainless_login(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Configures SaaS applications matching an optional filter to treat domainless logins as corporate logins.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/allow_domainless_login'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def list_saas_application_categories(self) -> dict:
        '''
        Description: Lists SaaS application categories.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/categories'
        return fortidlp_connection.get(url)

    def get_saas_application_config(self) -> dict:
        '''
        Description: Gets the current SaaS application config.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/config'
        return fortidlp_connection.get(url)

    def update_saas_application_config(self, config: dict) -> dict:
        '''
        Description: Update the SaaS application config.
        Args:
            config (dict): The configuration for SaaS applications.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/config'
        return fortidlp_connection.post(url, json=config)

    def create_saas_application_entries(self, ids: List[str]) -> dict:
        '''
        Description: Adds SaaS application entries by ID.
        Args:
            ids (List[str]): List of SaaS application IDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/create'
        data = {"ids": ids}
        return fortidlp_connection.post(url, json=data)

    def create_custom_saas_application(self, name: str, domains: List[str], category: Optional[str] = None) -> dict:
        '''
        Description: Creates a new custom SaaS application.
        Args:
            name (str): The name of the custom SaaS application.
            domains (List[str]): List of domains associated with the application.
            category (str, optional): The category of the application.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/custom/create'
        data = {
            "name": name,
            "domains": domains
        }
        if category is not None:
            data["category"] = category
        return fortidlp_connection.post(url, json=data)

    def test_url_matching(self, url: str) -> dict:
        '''
        Description: Tests URL matching.
        Args:
            url (str): The URL to test.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/custom/test'
        data = {"url": url}
        return fortidlp_connection.post(url, json=data)

    def update_custom_saas_application(self, app_id: str, name: Optional[str] = None, domains: Optional[List[str]] = None, category: Optional[str] = None) -> dict:
        '''
        Description: Updates the specified custom SaaS application.
        Args:
            app_id (str): The ID of the custom SaaS application.
            name (str, optional): The new name for the application.
            domains (List[str], optional): The new list of domains.
            category (str, optional): The new category.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/saas-applications/custom/{app_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if domains is not None:
            data["domains"] = domains
        if category is not None:
            data["category"] = category
        return fortidlp_connection.patch(url, json=data)

    def delete_saas_application_icon(self, app_id: str) -> dict:
        '''
        Description: Deletes the SaaS application icon.
        Args:
            app_id (str): The ID of the SaaS application.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/saas-applications/custom/{app_id}/icon'
        return fortidlp_connection.delete(url)

    def update_saas_application_icon(self, app_id: str, icon_content: bytes, content_type: str) -> dict:
        '''
        Description: Updates the specified custom SaaS application icon.
        Args:
            app_id (str): The ID of the SaaS application.
            icon_content (bytes): The content of the icon file.
            content_type (str): The content type of the icon file.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/saas-applications/custom/{app_id}/icon'
        files = {'file': ('icon', icon_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def export_saas_applications_csv(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports SaaS applications search as CSV data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/export/csv'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def get_saas_application_export_fields(self) -> dict:
        '''
        Description: Returns all possible fields that can be exported for SaaS applications and whether each field is included by default.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/export/fields'
        return fortidlp_connection.get(url)

    def export_saas_applications_xlsx(self, filter: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> dict:
        '''
        Description: Exports SaaS applications search as XLSX data.
        Args:
            filter (list, optional): List of filters to apply.
            fields (list, optional): List of fields to export.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/export/xlsx'
        data = {}
        if filter is not None:
            data["filter"] = filter
        if fields is not None:
            data["fields"] = fields
        return fortidlp_connection.post(url, json=data)

    def override_saas_application_scores(self, scores: dict, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Overrides the risk scores for SaaS applications matching an optional filter.
        Args:
            scores (dict): The scores to apply.
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/scores'
        data = {"scores": scores}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def reset_saas_application_scores(self, all: Optional[bool] = None, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Resets the scores of all applications matching an optional filter to their defaults.
        Args:
            all (bool, optional): Whether to reset all applications.
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/scores/reset'
        data = {}
        if all is not None:
            data["all"] = all
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def search_saas_applications(self, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches SaaS applications.
        Args:
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def change_saas_application_state(self, state: str, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Changes the state of SaaS applications.
        Args:
            state (str): The new state for the applications.
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/state'
        data = {"state": state}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def search_saas_application_templates(self, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Searches SaaS applications which may be added to the inventory.
        Args:
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/templates'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def get_saas_application_templates_terms(self) -> dict:
        '''
        Description: Retrieves all terms for SaaS application templates.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/templates/terms'
        return fortidlp_connection.get(url)

    def get_saas_application_terms(self) -> dict:
        '''
        Description: Retrieves all terms for SaaS applications.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/terms'
        return fortidlp_connection.get(url)

    def change_saas_application_verdict(self, verdict: str, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Changes the verdict status of SaaS applications.
        Args:
            verdict (str): The new verdict status.
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v2/saas-applications/verdict'
        data = {"verdict": verdict}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)

    def get_single_saas_application(self, app_id: str) -> dict:
        '''
        Description: Gets a single SaaS application by ID.
        Args:
            app_id (str): The ID of the SaaS application.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/saas-applications/{app_id}'
        return fortidlp_connection.get(url)

    def get_saas_application_icon(self, app_id: str) -> dict:
        '''
        Description: Gets the icon for a SaaS application.
        Args:
            app_id (str): The ID of the SaaS application.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v2/saas-applications/{app_id}/icon'
        return fortidlp_connection.get(url)
