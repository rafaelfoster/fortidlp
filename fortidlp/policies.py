from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Policies:
    '''
    Class Policies
    Description: Manages agent policies.
    '''

    def get_all_data_objects(self) -> dict:
        '''
        Description: Return all data objects.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/data'
        return fortidlp_connection.get(url)

    def create_data_object(self, ref: str, name: str, description: Optional[str] = None, tags: Optional[List[str]] = None) -> dict:
        '''
        Description: Create a data object using an existing ref.
        Args:
            ref (str): The reference to the existing data.
            name (str): The name of the data object.
            description (str, optional): The description of the data object.
            tags (List[str], optional): List of tags for the data object.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/data'
        data = {
            "ref": ref,
            "name": name,
            "description": description,
            "tags": tags
        }
        return fortidlp_connection.post(url, json=data)

    def upload_data_object_blob(self, file_content: bytes, content_type: str) -> dict:
        '''
        Description: Upload a data object blob.
        Args:
            file_content (bytes): The content of the file.
            content_type (str): The content type of the file.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/data/upload'
        files = {'file': ('blob', file_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def delete_data_object_by_id(self, data_id: str) -> dict:
        '''
        Description: Delete data object by id.
        Args:
            data_id (str): The ID of the data object to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/data/{data_id}'
        return fortidlp_connection.delete(url)

    def get_data_object_by_id(self, data_id: str) -> dict:
        '''
        Description: Return data object by id.
        Args:
            data_id (str): The ID of the data object.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/data/{data_id}'
        return fortidlp_connection.get(url)

    def update_data_object(self, data_id: str, name: Optional[str] = None, description: Optional[str] = None, tags: Optional[List[str]] = None) -> dict:
        '''
        Description: Update a data object - can update `name`, `description`, `tags`.
        Args:
            data_id (str): The ID of the data object.
            name (str, optional): The new name for the data object.
            description (str, optional): The new description for the data object.
            tags (List[str], optional): The new list of tags for the data object.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/data/{data_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if tags is not None:
            data["tags"] = tags
        return fortidlp_connection.patch(url, json=data)

    def download_data_object(self, data_id: str) -> dict:
        '''
        Description: Downloads the data object specified in the request.
        Args:
            data_id (str): The ID of the data object.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/data/{data_id}/download'
        return fortidlp_connection.get(url)

    def export_policy_groups(self, group_ids: List[str], include_data_objects: Optional[bool] = None, include_labels: Optional[bool] = None) -> dict:
        '''
        Description: Export the policy groups specified in the request.
        Args:
            group_ids (List[str]): List of policy group IDs to export.
            include_data_objects (bool, optional): Whether to include data objects.
            include_labels (bool, optional): Whether to include labels.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/export'
        data = {"group_ids": group_ids}
        if include_data_objects is not None:
            data["include_data_objects"] = include_data_objects
        if include_labels is not None:
            data["include_labels"] = include_labels
        return fortidlp_connection.post(url, json=data)

    def fetch_all_group_templates(self) -> dict:
        '''
        Description: Fetch all group templates.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/group-templates'
        return fortidlp_connection.get(url)

    def fetch_policy_templates_by_group_template_id(self, group_template_id: str) -> dict:
        '''
        Description: Fetch all Policy Templates belonging to a particular group template.
        Args:
            group_template_id (str): The ID of the group template.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/group-templates/{group_template_id}/templates'
        return fortidlp_connection.get(url)

    def fetch_all_policy_groups(self) -> dict:
        '''
        Description: Fetch all Policy Groups.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/groups'
        return fortidlp_connection.get(url)

    def create_policy_group(self, name: str, description: Optional[str] = None, enabled: Optional[bool] = None, match: Optional[str] = None, exclude_match: Optional[str] = None, include_labels: Optional[List[str]] = None, exclude_labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Create a Policy Group.
        Args:
            name (str): The name of the policy group.
            description (str, optional): The description of the policy group.
            enabled (bool, optional): Whether the policy group is enabled.
            match (str, optional): The match criteria.
            exclude_match (str, optional): The exclude match criteria.
            include_labels (List[str], optional): List of labels to include.
            exclude_labels (List[str], optional): List of labels to exclude.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/groups'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if enabled is not None:
            data["enabled"] = enabled
        if match is not None:
            data["match"] = match
        if exclude_match is not None:
            data["exclude_match"] = exclude_match
        if include_labels is not None:
            data["include_labels"] = include_labels
        if exclude_labels is not None:
            data["exclude_labels"] = exclude_labels
        return fortidlp_connection.post(url, json=data)

    def publish_policy_groups(self, group_ids: List[str]) -> dict:
        '''
        Description: Publish Policy Groups.
        Args:
            group_ids (List[str]): List of policy group IDs to publish.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/groups/publish'
        data = {"group_ids": group_ids}
        return fortidlp_connection.post(url, json=data)

    def test_policy_groups(self, label_uuids: List[str]) -> dict:
        '''
        Description: Returns policy groups that apply for given labels.
        Args:
            label_uuids (List[str]): List of label UUIDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/groups/test'
        data = {"label_uuids": label_uuids}
        return fortidlp_connection.post(url, json=data)

    def create_policy_within_group(self, group_id: str, name: str, description: Optional[str] = None, enabled: Optional[bool] = None, parameter_values: Optional[dict] = None, clustering_rules: Optional[List[str]] = None) -> dict:
        '''
        Description: Create a Policy within a Policy Group.
        Args:
            group_id (str): The ID of the policy group.
            name (str): The name of the policy.
            description (str, optional): The description of the policy.
            enabled (bool, optional): Whether the policy is enabled.
            parameter_values (dict, optional): Parameter values for the policy.
            clustering_rules (List[str], optional): Clustering rules for the policy.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/policies'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if enabled is not None:
            data["enabled"] = enabled
        if parameter_values is not None:
            data["parameter_values"] = parameter_values
        if clustering_rules is not None:
            data["clustering_rules"] = clustering_rules
        return fortidlp_connection.post(url, json=data)

    def fetch_policy(self, group_id: str, policy_id: str) -> dict:
        '''
        Description: Fetch a Policy.
        Args:
            group_id (str): The ID of the policy group.
            policy_id (str): The ID of the policy.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/policies/{policy_id}'
        return fortidlp_connection.get(url)

    def update_partial_policy(self, group_id: str, policy_id: str, name: Optional[str] = None, description: Optional[str] = None, enabled: Optional[bool] = None, parameter_values: Optional[dict] = None, clustering_rules: Optional[List[str]] = None) -> dict:
        '''
        Description: Update part of a Policy - can update `name`, `description`, `enabled`, `parameter_values`, `clustering_rules`.
        Args:
            group_id (str): The ID of the policy group.
            policy_id (str): The ID of the policy.
            name (str, optional): The new name for the policy.
            description (str, optional): The new description for the policy.
            enabled (bool, optional): Whether the policy is enabled.
            parameter_values (dict, optional): New parameter values for the policy.
            clustering_rules (List[str], optional): New clustering rules for the policy.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/policies/{policy_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if enabled is not None:
            data["enabled"] = enabled
        if parameter_values is not None:
            data["parameter_values"] = parameter_values
        if clustering_rules is not None:
            data["clustering_rules"] = clustering_rules
        return fortidlp_connection.patch(url, json=data)

    def update_complete_policy(self, group_id: str, policy_id: str, name: str, description: Optional[str] = None, enabled: Optional[bool] = None, parameter_values: Optional[dict] = None, clustering_rules: Optional[List[str]] = None) -> dict:
        '''
        Description: Complete update of a Policy - can update `name`, `description`, `enabled`, `parameter_values`, `clustering_rules`.
        Args:
            group_id (str): The ID of the policy group.
            policy_id (str): The ID of the policy.
            name (str): The new name for the policy.
            description (str, optional): The new description for the policy.
            enabled (bool, optional): Whether the policy is enabled.
            parameter_values (dict, optional): New parameter values for the policy.
            clustering_rules (List[str], optional): New clustering rules for the policy.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/policies/{policy_id}'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if enabled is not None:
            data["enabled"] = enabled
        if parameter_values is not None:
            data["parameter_values"] = parameter_values
        if clustering_rules is not None:
            data["clustering_rules"] = clustering_rules
        return fortidlp_connection.put(url, json=data)

    def get_policy_defaults(self, group_id: str, policy_id: str) -> dict:
        '''
        Description: Gets the Policy updated to use the template defaults.
        Args:
            group_id (str): The ID of the policy group.
            policy_id (str): The ID of the policy.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/policies/{policy_id}/defaults'
        return fortidlp_connection.get(url)

    def delete_policy(self, group_id: str, policy_id: str) -> dict:
        '''
        Description: Delete a Policy.
        Args:
            group_id (str): The ID of the policy group.
            policy_id (str): The ID of the policy.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/policies/{policy_id}'
        return fortidlp_connection.delete(url)

    def delete_policy_group(self, group_id: str) -> dict:
        '''
        Description: Delete a Policy Group.
        Args:
            group_id (str): The ID of the policy group.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}'
        return fortidlp_connection.delete(url)

    def get_policy_group(self, group_id: str) -> dict:
        '''
        Description: Fetch a Policy Group.
        Args:
            group_id (str): The ID of the policy group.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}'
        return fortidlp_connection.get(url)

    def update_partial_policy_group(self, group_id: str, name: Optional[str] = None, description: Optional[str] = None, enabled: Optional[bool] = None, match: Optional[str] = None, exclude_match: Optional[str] = None, include_labels: Optional[List[str]] = None, exclude_labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Update part of a Policy Group - can update `name`, `description`, `enabled`, `match`. `exclude_match`, `include_labels` and `exclude_labels`.
        Args:
            group_id (str): The ID of the policy group.
            name (str, optional): The new name for the policy group.
            description (str, optional): The new description for the policy group.
            enabled (bool, optional): Whether the policy group is enabled.
            match (str, optional): The new match criteria.
            exclude_match (str, optional): The new exclude match criteria.
            include_labels (List[str], optional): New list of labels to include.
            exclude_labels (List[str], optional): New list of labels to exclude.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}'
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if enabled is not None:
            data["enabled"] = enabled
        if match is not None:
            data["match"] = match
        if exclude_match is not None:
            data["exclude_match"] = exclude_match
        if include_labels is not None:
            data["include_labels"] = include_labels
        if exclude_labels is not None:
            data["exclude_labels"] = exclude_labels
        return fortidlp_connection.patch(url, json=data)

    def update_complete_policy_group(self, group_id: str, name: str, description: Optional[str] = None, enabled: Optional[bool] = None, match: Optional[str] = None, exclude_match: Optional[str] = None, include_labels: Optional[List[str]] = None, exclude_labels: Optional[List[str]] = None) -> dict:
        '''
        Description: Complete update of a Policy Group - can update `name`, `description`, `enabled`, `match`. `exclude_match`.
        Args:
            group_id (str): The ID of the policy group.
            name (str): The new name for the policy group.
            description (str, optional): The new description for the policy group.
            enabled (bool, optional): Whether the policy group is enabled.
            match (str, optional): The new match criteria.
            exclude_match (str, optional): The new exclude match criteria.
            include_labels (List[str], optional): New list of labels to include.
            exclude_labels (List[str], optional): New list of labels to exclude.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}'
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if enabled is not None:
            data["enabled"] = enabled
        if match is not None:
            data["match"] = match
        if exclude_match is not None:
            data["exclude_match"] = exclude_match
        if include_labels is not None:
            data["include_labels"] = include_labels
        if exclude_labels is not None:
            data["exclude_labels"] = exclude_labels
        return fortidlp_connection.put(url, json=data)

    def clone_policy_group(self, group_id: str) -> dict:
        '''
        Description: Copy a Policy Group.
        Args:
            group_id (str): The ID of the policy group to clone.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/clone'
        return fortidlp_connection.post(url)

    def unassign_exclude_label_from_agent_policy_group(self, group_id: str, label_id: str) -> dict:
        '''
        Description: Unassign exclude label from agent policy group.
        Args:
            group_id (str): The ID of the policy group.
            label_id (str): The ID of the label to unassign.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/exclude-labels/{label_id}'
        return fortidlp_connection.delete(url)

    def assign_exclude_label_to_agent_policy_group(self, group_id: str, label_id: str) -> dict:
        '''
        Description: Assign exclude label to agent policy group.
        Args:
            group_id (str): The ID of the policy group.
            label_id (str): The ID of the label to assign.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/exclude-labels/{label_id}'
        return fortidlp_connection.post(url)

    def get_policy_group_labels(self, group_id: str) -> dict:
        '''
        Description: Deprecated in favour of using /api/v1/policies/groups/{id}.
        Args:
            group_id (str): The ID of the policy group.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/labels'
        return fortidlp_connection.get(url)

    def unassign_label_from_agent_policy_group(self, group_id: str, label_id: str) -> dict:
        '''
        Description: Unassign label from agent policy group.
        Args:
            group_id (str): The ID of the policy group.
            label_id (str): The ID of the label to unassign.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/labels/{label_id}'
        return fortidlp_connection.delete(url)

    def assign_label_to_agent_policy_group(self, group_id: str, label_id: str) -> dict:
        '''
        Description: Assign label to agent policy group.
        Args:
            group_id (str): The ID of the policy group.
            label_id (str): The ID of the label to assign.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/labels/{label_id}'
        return fortidlp_connection.post(url)

    def publish_policy_group(self, group_id: str) -> dict:
        '''
        Description: Publish a Policy Group.
        Args:
            group_id (str): The ID of the policy group to publish.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/groups/{group_id}/publish'
        return fortidlp_connection.post(url)

    def import_agent_policy_groups(self, file_content: bytes, content_type: str) -> dict:
        '''
        Description: Import agent policy groups together with their policies and data objects.
        Args:
            file_content (bytes): The content of the file.
            content_type (str): The content type of the file.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/import'
        files = {'file': ('policies', file_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def fetch_all_policy_packs(self) -> dict:
        '''
        Description: Fetch all Policy Packs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/packs'
        return fortidlp_connection.get(url)

    def upload_all_policy_packs(self, file_content: bytes, content_type: str) -> dict:
        '''
        Description: Upload all Policy Packs.
        Args:
            file_content (bytes): The content of the file.
            content_type (str): The content type of the file.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/packs/upload'
        files = {'file': ('packs', file_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def delete_policy_pack(self, pack_id: str) -> dict:
        '''
        Description: Delete a Policy Pack.
        Args:
            pack_id (str): The ID of the policy pack to delete.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/packs/{pack_id}'
        return fortidlp_connection.delete(url)

    def fetch_policy_pack(self, pack_id: str) -> dict:
        '''
        Description: Fetch a Policy Pack.
        Args:
            pack_id (str): The ID of the policy pack.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/packs/{pack_id}'
        return fortidlp_connection.get(url)

    def fetch_policy_templates_by_policy_pack_id(self, pack_id: str) -> dict:
        '''
        Description: Fetch all Policy Templates belonging to a particular Policy Pack.
        Args:
            pack_id (str): The ID of the policy pack.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/packs/{pack_id}/templates'
        return fortidlp_connection.get(url)

    def fetch_policy_template(self, pack_id: str, template_id: str) -> dict:
        '''
        Description: Fetch a Policy Template.
        Args:
            pack_id (str): The ID of the policy pack.
            template_id (str): The ID of the policy template.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/policies/packs/{pack_id}/templates/{template_id}'
        return fortidlp_connection.get(url)

    def search_policies(self, filter: Optional[List[str]] = None) -> dict:
        '''
        Description: Searches policies.
        Args:
            filter (list, optional): List of filters to apply.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/policies/search'
        data = {}
        if filter is not None:
            data["filter"] = filter
        return fortidlp_connection.post(url, json=data)
