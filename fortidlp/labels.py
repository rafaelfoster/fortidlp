from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Labels:
    '''
    Class Labels
    Description: Manages labels.
    '''

    def create_label(self, name: str, description: Optional[str] = None, category: Optional[str] = None, anonymise: Optional[bool] = None, flagged: Optional[bool] = None) -> dict:
        '''
        Description: Create a label.
        Args:
            name (str): The name of the label.
            description (str, optional): The description of the label.
            category (str, optional): The category of the label.
            anonymise (bool, optional): Whether to anonymise the label.
            flagged (bool, optional): Whether the label is flagged.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/labels'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if category is not None:
            data["category"] = category
        if anonymise is not None:
            data["anonymise"] = anonymise
        if flagged is not None:
            data["flagged"] = flagged
        return fortidlp_connection.post(url, json=data)

    def search_labels(self, filter: Optional[List[str]] = None, results_per_page: int = 100, sort_order: str = "asc", cursor: Optional[str] = None) -> dict:
        '''
        Description: Return a list of labels.
        Args:
            filter (list, optional): List of filters to apply.
            results_per_page (int): Number of results per page.
            sort_order (str): Sort order for the results, either "asc" or "desc".
            cursor (str, optional): Cursor for pagination.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/labels/search'
        parameters = {}
        if filter:
            parameters["filter"] = filter if isinstance(filter, list) else [filter]
        if cursor:
            parameters["cursor"] = cursor

        url = f"{url}?results_per_page={results_per_page}&sort_order={sort_order}"
        
        return fortidlp_connection.send(url, params=parameters)

    def delete_label_by_id(self, label_id: str) -> dict:
        '''
        Description: Delete label by id.
        Args:
            label_id (str): The ID of the label to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/labels/{label_id}'
        return fortidlp_connection.delete(url)

    def get_label_by_id(self, label_id: str) -> dict:
        '''
        Description: Return label by id.
        Args:
            label_id (str): The ID of the label.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/labels/{label_id}'
        return fortidlp_connection.get(url)

    def update_label(self, label_id: str, name: Optional[str] = None, description: Optional[str] = None, category: Optional[str] = None, anonymise: Optional[bool] = None, flagged: Optional[bool] = None) -> dict:
        '''
        Description: Updates a label.
        Args:
            label_id (str): The ID of the label.
            name (str, optional): The new name for the label.
            description (str, optional): The new description for the label.
            category (str, optional): The new category for the label.
            anonymise (bool, optional): Whether to anonymise the label.
            flagged (bool, optional): Whether the label is flagged.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/labels/{label_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if category is not None:
            data["category"] = category
        if anonymise is not None:
            data["anonymise"] = anonymise
        if flagged is not None:
            data["flagged"] = flagged
        return fortidlp_connection.patch(url, json=data)
