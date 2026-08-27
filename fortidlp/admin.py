from fortidlp.fortidlp import fortidlp_connection
from typing import Optional, List

class Admin:
    '''
    Class Admin
    Description: Performs administrative and management tasks.
    '''

    def delete_archived_agents(self, agent_ids: List[str], archived_days: Optional[str] = None, inactive_days: Optional[int] = None, never_reported: Optional[bool] = None, revoked_days: Optional[str] = None) -> dict:
        '''
        Description: Deletes unused archived agents.
        Args:
            agent_ids (List[str]): List of agent IDs to delete.
            archived_days (str, optional): Agents archived for this many days.
            inactive_days (int, optional): Agents inactive for this many days.
            never_reported (bool, optional): Agents that have never reported.
            revoked_days (str, optional): Agents revoked for this many days.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/agents/archived/delete'
        data = {
            "agent_ids": agent_ids
        }
        if archived_days is not None:
            data["archived_days"] = archived_days
        if inactive_days is not None:
            data["inactive_days"] = inactive_days
        if never_reported is not None:
            data["never_reported"] = never_reported
        if revoked_days is not None:
            data["revoked_days"] = revoked_days
        return fortidlp_connection.send(url, params=data)

    def download_agent_binary(self, os_type: str, version: str) -> dict:
        '''
        Description: Downloads an agent binary.
        Args:
            os_type (str): The operating system type (e.g., "windows", "macos", "linux").
            version (str): The version of the agent binary.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/binaries?os_type={os_type}&version={version}'
        return fortidlp_connection.get(url)

    def delete_all_agent_crash_reports(self) -> dict:
        '''
        Description: Deletes all agent crash reports.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/agents/crashes'
        return fortidlp_connection.delete(url)

    def list_agent_crash_dumps(self) -> dict:
        '''
        Description: Lists agent crash dumps.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/agents/crashes'
        return fortidlp_connection.get(url)

    def assign_labels_to_agents(self, agent_ids: List[str], label_ids: List[str]) -> dict:
        '''
        Description: Assigns labels to a set of agents.
        Args:
            agent_ids (List[str]): List of agent IDs.
            label_ids (List[str]): List of label IDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/agents/labels/add'
        data = {
            "agent_ids": agent_ids,
            "label_ids": label_ids
        }
        return fortidlp_connection.send(url, params=data)

    def unassign_labels_from_agents(self, agent_ids: List[str], label_ids: List[str]) -> dict:
        '''
        Description: Unassigns labels from a set of agents.
        Args:
            agent_ids (List[str]): List of agent IDs.
            label_ids (List[str]): List of label IDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/agents/labels/remove'
        data = {
            "agent_ids": agent_ids,
            "label_ids": label_ids
        }
        return fortidlp_connection.send(url, params=data)

    def get_available_agent_upgrade_versions(self) -> dict:
        '''
        Description: Gets the available agent upgrade versions.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/agents/updates'
        return fortidlp_connection.get(url)

    def get_agent_classifications(self, agent_id: str) -> dict:
        '''
        Description: Gets classifications assigned to an agent.
        Args:
            agent_id (str): The ID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/classifications'
        return fortidlp_connection.get(url)

    def remove_agent_classification(self, agent_id: str, classification_id: str) -> dict:
        '''
        Description: Removes an agent classification.
        Args:
            agent_id (str): The ID of the agent.
            classification_id (str): The ID of the classification to remove.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/classifications/{classification_id}'
        return fortidlp_connection.delete(url)

    def assign_classification_to_agent(self, agent_id: str, classification_id: str) -> dict:
        '''
        Description: Assigns a classification to an agent.
        Args:
            agent_id (str): The ID of the agent.
            classification_id (str): The ID of the classification to assign.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/classifications/{classification_id}'
        return fortidlp_connection.post(url)

    def exclude_classification_from_agent(self, agent_id: str, classification_id: str) -> dict:
        '''
        Description: Remove and exclude a classification from an agent.
        Args:
            agent_id (str): The ID of the agent.
            classification_id (str): The ID of the classification to exclude.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/classifications/{classification_id}/exclude'
        return fortidlp_connection.post(url)

    def delete_agent_crash_reports(self, agent_id: str) -> dict:
        '''
        Description: Deletes all crash reports for an agent.
        Args:
            agent_id (str): The ID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/crashes'
        return fortidlp_connection.delete(url)

    def list_agent_crash_events(self, agent_id: str) -> dict:
        '''
        Description: Lists agent crash events for a given ID.
        Args:
            agent_id (str): The ID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/crashes'
        return fortidlp_connection.get(url)

    def download_agent_crash_report(self, agent_id: str, crash_id: str) -> dict:
        '''
        Description: Downloads an agent crash report.
        Args:
            agent_id (str): The ID of the agent.
            crash_id (str): The ID of the crash report.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/crashes/{crash_id}'
        return fortidlp_connection.get(url)

    def get_agent_labels(self, agent_id: str) -> dict:
        '''
        Description: Gets labels assigned to an agent.
        Args:
            agent_id (str): The ID of the agent.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/agents/{agent_id}/labels'
        return fortidlp_connection.get(url)

    def delete_login_banner_configuration(self) -> dict:
        '''
        Description: Deletes the login banner configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/login/banner'
        return fortidlp_connection.delete(url)

    def get_login_banner_configuration(self) -> dict:
        '''
        Description: Gets the login banner configuration.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/login/banner'
        return fortidlp_connection.get(url)

    def update_login_banner_configuration(self, banner_text: str, enabled: bool) -> dict:
        '''
        Description: Updates the login banner configuration.
        Args:
            banner_text (str): The text for the login banner.
            enabled (bool): Whether the login banner is enabled.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/login/banner'
        data = {
            "banner_text": banner_text,
            "enabled": enabled
        }
        return fortidlp_connection.put(url, json=data)

    def list_operator_sessions(self) -> dict:
        '''
        Description: Lists operator sessions.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/operator_sessions'
        return fortidlp_connection.get(url)

    def revoke_operator_session(self, session_id: str) -> dict:
        '''
        Description: Revokes an operator session.
        Args:
            session_id (str): The ID of the session to revoke.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/operator_sessions/{session_id}/revoke'
        return fortidlp_connection.post(url)

    def create_user(self, username: str, password: str, email: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, roles: Optional[List[str]] = None) -> dict:
        '''
        Description: Creates a user.
        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            email (str, optional): The email address of the new user.
            first_name (str, optional): The first name of the new user.
            last_name (str, optional): The last name of the new user.
            roles (list, optional): A list of roles for the new user.
        Returns:
            dict: The response from the API, containing the created user's details.
        '''
        url = '/api/v1/admin/users'
        data = {
            "username": username,
            "password": password
        }
        if email is not None:
            data["email"] = email
        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if roles is not None:
            data["roles"] = roles
        return fortidlp_connection.post(url, json=data)

    def bulk_create_users(self, users: List[dict]) -> dict:
        '''
        Description: Creates a set of users.
        Args:
            users (List[dict]): A list of user objects to create.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/users/bulk'
        data = {"users": users}
        return fortidlp_connection.post(url, json=data)

    def import_users_from_csv(self, csv_file_content: str) -> dict:
        '''
        Description: Import a set of users from csv.
        Args:
            csv_file_content (str): The content of the CSV file as a string.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/users/import'
        files = {'file': ('users.csv', csv_file_content, 'text/csv')}
        return fortidlp_connection.post(url, files=files)

    def assign_labels_to_users(self, user_ids: List[str], label_ids: List[str]) -> dict:
        '''
        Description: Assigns labels to a set of users.
        Args:
            user_ids (List[str]): List of user IDs.
            label_ids (List[str]): List of label IDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/users/labels/add'
        data = {
            "user_ids": user_ids,
            "label_ids": label_ids
        }
        return fortidlp_connection.put(url, json=data)

    def unassign_labels_from_users(self, user_ids: List[str], label_ids: List[str]) -> dict:
        '''
        Description: Unassigns labels from a set of users.
        Args:
            user_ids (List[str]): List of user IDs.
            label_ids (List[str]): List of label IDs.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/users/labels/remove'
        data = {
            "user_ids": user_ids,
            "label_ids": label_ids
        }
        return fortidlp_connection.put(url, json=data)

    def restore_user(self, user_id: str) -> dict:
        '''
        Description: Allows restoration of a user through user sync.
        Args:
            user_id (str): The ID of the user to restore.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/users/{user_id}/restore'
        return fortidlp_connection.post(url)

    def get_user_labels(self, user_id: str) -> dict:
        '''
        Description: Gets labels assigned to a user.
        Args:
            user_id (str): The ID of the user.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/users/{user_id}/labels'
        return fortidlp_connection.get(url)

    def add_user_photo(self, user_id: str, photo_content: bytes, content_type: str) -> dict:
        '''
        Description: Adds a user photo for the specified user.
        Args:
            user_id (str): The ID of the user.
            photo_content (bytes): The content of the photo as bytes.
            content_type (str): The content type of the photo (e.g., "image/jpeg").
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/users/{user_id}/photo'
        files = {'file': ('photo', photo_content, content_type)}
        return fortidlp_connection.post(url, files=files)

    def update_user_uris(self, user_id: str, user_uris: List[str]) -> dict:
        '''
        Description: Adds/removes user uris for the given user ID.
        Args:
            user_id (str): The ID of the user.
            user_uris (List[str]): List of user URIs.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/users/{user_id}/useruris'
        data = {"user_uris": user_uris}
        return fortidlp_connection.put(url, json=data)

    def delete_user_pii(self, user_uuid: str) -> dict:
        '''
        Description: Clears all Personally Identifiable Information (PII) pertaining to the specified user and marks them as deleted.
        Args:
            user_uuid (str): The UUID of the user.
        Returns:
            dict: The response from the API.
        '''
        url = f'/api/v1/admin/users/{user_uuid}'
        return fortidlp_connection.delete(url)

    def get_stack_version(self) -> dict:
        '''
        Description: Retrieves the stack version.
        Returns:
            dict: The response from the API.
        '''
        url = '/api/v1/admin/version'
        return fortidlp_connection.get(url)
