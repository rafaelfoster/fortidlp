import json
import os
from typing import Optional
from urllib.parse import urlencode

from fortidlp.auth import AuthenticationHandler
from fortidlp.connector import APIHandler

version = '0.2'

fortidlp_connection = APIHandler()


def _as_list(value):
    if value is None:
        return None
    if isinstance(value, list):
        return value
    return [value]


def _build_url(url: str, **query) -> str:
    query = {key: value for key, value in query.items() if value is not None}
    if not query:
        return url
    return f"{url}?{urlencode(query, doseq=True)}"


def _download(url: str, params: Optional[dict] = None, method: str = 'GET', file_format: str = 'zip', download_folder: str = '') -> dict:
    return fortidlp_connection._exec(
        method,
        url,
        params=params,
        download_file=True,
        file_format=file_format,
        request_type=None,
    )


class Audit:
    '''Class Audit
    Description: Return and manage audit logs.
    '''

    def get_audit_logs(
        self,
        filter: list = None,
        start_time: str = None,
        end_time: str = None,
        operation_types: list[str] = None,
        results_per_page: int = 100,
        sort_order: str = 'desc',
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
    ) -> dict:
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        if start_time or end_time:
            parameters['time_range'] = {}
        if start_time:
            parameters['time_range']['from'] = start_time
        if end_time:
            parameters['time_range']['to'] = end_time
        if operation_types:
            parameters['types'] = _as_list(operation_types)

        url = _build_url(
            '/api/v1/audit/search',
            cursor=cursor,
            results_per_page=results_per_page,
            sort_order=sort_order,
            sort=sort,
        )
        return fortidlp_connection.send(url, params=parameters)

    def clear_audit_logs(self) -> dict:
        return fortidlp_connection.delete('/api/v1/audit')

    def export_audit_logs(
        self,
        filter: list = None,
        start_time: str = None,
        end_time: str = None,
        operation_types: list[str] = None,
        signed: bool = False,
        file_format: str = 'txt',
        download_folder: str = '',
    ) -> dict:
        query = {}
        if filter:
            query['filter'] = _as_list(filter)
        if start_time or end_time:
            query['time_range'] = {}
        if start_time:
            query['time_range']['from'] = start_time
        if end_time:
            query['time_range']['to'] = end_time
        if operation_types:
            query['types'] = _as_list(operation_types)

        return _download(
            '/api/v1/audit/export',
            params={'query': query, 'signed': signed},
            method='POST',
            file_format=file_format,
            download_folder=download_folder,
        )

    def get_audit_public_key(self) -> dict:
        return fortidlp_connection.get('/api/v1/audit/key')

    def verify_audit_export(self, checksum_sha256: str, signature_jws: str) -> dict:
        parameters = {
            'checksum_sha256': checksum_sha256,
            'signature_jws': signature_jws,
        }
        return fortidlp_connection.send('/api/v1/audit/verify', params=parameters)


class Cases:
    '''Class Cases
    Description: Manage FortiDLP cases.
    '''

    def list_cases(self, content_event_uri: Optional[str] = None, content_operated_by: Optional[str] = None, created_by: Optional[str] = None, entries: Optional[int] = None) -> dict:
        url = _build_url('/api/v1/cases', entries=entries)
        parameters = {}
        if content_event_uri:
            parameters['content_event_uri'] = content_event_uri
        if content_operated_by:
            parameters['content_operated_by'] = content_operated_by
        if created_by:
            parameters['created_by'] = created_by
        return fortidlp_connection.get(url, params=parameters)

    def get_case(self, case_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/cases/{case_id}')

    def create_case(self, title: str, description: Optional[str] = None, content_uris: Optional[list[str]] = None, image_content: Optional[str] = None, assigned_to: Optional[str] = None, severity: Optional[str] = None, status: Optional[str] = None) -> dict:
        parameters = {'title': title}
        if description:
            parameters['description'] = description
        if content_uris:
            parameters['content_uris'] = _as_list(content_uris)
        if image_content:
            parameters['image_content'] = image_content
        if assigned_to:
            parameters['assigned_to'] = assigned_to
        if severity:
            parameters['severity'] = severity
        if status:
            parameters['status'] = status
        return fortidlp_connection.send('/api/v1/cases', params=parameters)

    def update_case(self, case_id: str, title: Optional[str] = None, description: Optional[str] = None, assigned_to: Optional[str] = None, severity: Optional[str] = None, status: Optional[str] = None) -> dict:
        parameters = {}
        if title:
            parameters['title'] = title
        if description:
            parameters['description'] = description
        if assigned_to:
            parameters['assigned_to'] = assigned_to
        if severity:
            parameters['severity'] = severity
        if status:
            parameters['status'] = status
        return fortidlp_connection.insert(f'/api/v1/cases/{case_id}', params=parameters)

    def delete_case(self, case_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/cases/{case_id}')

    def assign_case(self, case_id: str, operator_uri: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/cases/{case_id}/assign', params={'operator_uri': operator_uri})

    def unassign_case(self, case_id: str, operator_uri: Optional[str] = None) -> dict:
        parameters = {}
        if operator_uri:
            parameters['operator_uri'] = operator_uri
        return fortidlp_connection.send(f'/api/v1/cases/{case_id}/unassign', params=parameters)

    def get_case_content(self, case_id: str, time: Optional[str] = None, paging: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v1/cases/{case_id}/content', time=time, paging=paging)
        return fortidlp_connection.get(url)

    def add_case_content(self, case_id: str, contents: list[dict]) -> dict:
        return fortidlp_connection.send(f'/api/v1/cases/{case_id}/content', params={'contents': contents})

    def update_case_content(self, case_id: str, filename: str, content_uuid: str, description: Optional[str] = None, title: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v1/cases/{case_id}/content/{filename}', content_uuid=content_uuid)
        parameters = {}
        if description:
            parameters['description'] = description
        if title:
            parameters['title'] = title
        return fortidlp_connection.insert(url, params=parameters)

    def delete_case_content(self, case_id: str, filename: str, content_uuid: str) -> dict:
        url = _build_url(f'/api/v1/cases/{case_id}/content/{filename}', content_uuid=content_uuid)
        return fortidlp_connection.delete(url)

    def download_case_content(self, case_id: str, filename: str, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/cases/{case_id}/content/{filename}', method='GET', file_format=file_format, download_folder=download_folder)

    def add_case_image(self, case_id: str, image_content: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/cases/{case_id}/image', params={'image_content': image_content})
    def case_analysis_credit_allocation(self) -> dict:
        return fortidlp_connection.get('/api/v1/cases/analysis/credit-allocation')

    def case_analysis(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/cases/id/analysis', params=kwargs)

    def case_analysis_history(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/cases/{id}/analysis/history', params=kwargs)


class Operators:
    '''Class Operators
    Description: Manage operators.
    '''

    def list_operators(self) -> dict:
        return fortidlp_connection.get('/api/v1/operators')

    def get_operator(self, operator_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/operators/{operator_id}')

    def create_operator(self, username: str, name: str, email: str, company: str, password: str, role, link_expiration: int = 1, password_reset_on_login: bool = True, pseudonymized: Optional[bool] = None) -> dict:
        data = {
            'operator': {
                'company': company,
                'display_name': name,
                'email': email,
                'name': username,
                'roles': _as_list(role),
            },
            'passphrase': password,
            'passphrase_reset_link_expiry_duration': link_expiration,
            'passphrase_reset_on_login': password_reset_on_login,
        }
        if pseudonymized is not None:
            data['operator']['pseudonymized'] = pseudonymized
        return fortidlp_connection.send('/api/v1/operators', params=data)

    def update_operator(self, operator_id: str, username: Optional[str] = None, display_name: Optional[str] = None, email: Optional[str] = None, company: Optional[str] = None, roles: Optional[list[str]] = None, pseudonymized: Optional[bool] = None) -> dict:
        data = {}
        if username:
            data['name'] = username
        if display_name:
            data['display_name'] = display_name
        if email:
            data['email'] = email
        if company:
            data['company'] = company
        if roles:
            data['roles'] = _as_list(roles)
        if pseudonymized is not None:
            data['pseudonymized'] = pseudonymized
        return fortidlp_connection.insert(f'/api/v1/operators/{operator_id}', params=data)

    def delete_operator(self, operator_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/operators/{operator_id}')

    def reset_operator_mfa(self, operator_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/operators/{operator_id}/mfa')

    def invalidate_operator_passphrase(self, operator_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/operators/{operator_id}/passphrase')

    def generate_passphrase_reset_link(self, operator_id: str, expiry_duration: Optional[int] = None) -> dict:
        parameters = {}
        if expiry_duration is not None:
            parameters['expiry_duration'] = expiry_duration
        return fortidlp_connection.send(f'/api/v1/operators/{operator_id}/passphrase/reset-link', params=parameters)

    def require_passphrase_reset_on_next_login(self, operator_id: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/operators/{operator_id}/passphrase/reset-next-login', params={})
    def list_authentication_logs(self) -> dict:
        return fortidlp_connection.get('/api/v1/authentication-log')

    def get_tenant_region(self) -> dict:
        return fortidlp_connection.get('/api/v1/tenant-region')


class Users:
    '''Class Users
    Description: Manage users and user search.
    '''

    def get_users(self) -> dict:
        return fortidlp_connection.get('/api/v1/users')

    def create_user(self, address_home: str = None, address_office: str = None, department: str = None, description: str = None, directory_labels: Optional[list[dict]] = None, name: str = None, email: str = None, image_content: str = None, juid: str = None, manager: str = None, manager_unique_id: str = None, phone_number_mobile: str = None, phone_number_office: str = None, sync_invocation_id: str = None, sync_source: str = None, title: str = None, unique_data: str = None, unique_id: str = None, user_uri: Optional[list[str]] = None) -> dict:
        user = {
            'address_home': address_home,
            'address_office': address_office,
            'department': department,
            'description': description,
            'directory_labels': directory_labels,
            'email': email,
            'image_content': image_content,
            'juid': juid,
            'manager': manager,
            'manager_unique_id': manager_unique_id,
            'name': name,
            'phone_number_mobile': phone_number_mobile,
            'phone_number_office': phone_number_office,
            'title': title,
            'unique_data': unique_data,
            'unique_id': unique_id,
            'user_uri': _as_list(user_uri),
        }
        if sync_invocation_id or sync_source:
            user['sync_info'] = {
                'sync_invocation_id': sync_invocation_id,
                'sync_source': sync_source,
            }
        return fortidlp_connection.send('/api/v1/admin/users', params=user)

    def create_users_bulk(self, users: list[dict]) -> dict:
        return fortidlp_connection.send('/api/v1/admin/users/bulk', params={'users': users})

    def import_users(self, blob: str) -> dict:
        return fortidlp_connection.send('/api/v1/admin/users/import', params={'blob': blob})

    def restore_user(self, juid: Optional[str] = None, unique_data: Optional[str] = None) -> dict:
        parameters = {}
        if juid:
            parameters['juid'] = juid
        if unique_data:
            parameters['unique_data'] = unique_data
        return fortidlp_connection.send('/api/v1/admin/users/restore', params=parameters)

    def delete_user(self, user_uuid: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/admin/users/{user_uuid}')

    def get_user_labels(self, user_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/admin/users/{user_id}/labels')

    def add_user_photo(self, user_id: str, blob: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/admin/users/{user_id}/photo', params={'blob': blob})

    def update_user_uris(self, user_id: str, add: Optional[list[str]] = None, remove: Optional[list[str]] = None) -> dict:
        parameters = {}
        if add:
            parameters['add'] = _as_list(add)
        if remove:
            parameters['remove'] = _as_list(remove)
        return fortidlp_connection.insert(f'/api/v1/admin/users/{user_id}/useruris', params=parameters)

    def assign_labels(self, filter: list[str], labels: list[str]) -> dict:
        return fortidlp_connection.send('/api/v2/users/labels/add', params={'filter': _as_list(filter), 'labels': _as_list(labels)})

    def unassign_labels(self, filter: list[str], labels: list[str]) -> dict:
        return fortidlp_connection.send('/api/v2/users/labels/remove', params={'filter': _as_list(filter), 'labels': _as_list(labels)})

    def assign_labels_admin(self, user_ids: list[str], label_ids: list[str]) -> dict:
        return fortidlp_connection.insert('/api/v1/admin/users/labels/add', params={'user_ids': _as_list(user_ids), 'label_ids': _as_list(label_ids)})

    def unassign_labels_admin(self, user_ids: list[str], label_ids: list[str]) -> dict:
        return fortidlp_connection.insert('/api/v1/admin/users/labels/remove', params={'user_ids': _as_list(user_ids), 'label_ids': _as_list(label_ids)})

    def search_users(self, filter: list = None, include_agents: Optional[bool] = None, include_labels: Optional[bool] = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/users/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        if include_agents is not None:
            parameters['include_agents'] = include_agents
        if include_labels is not None:
            parameters['include_labels'] = include_labels
        return fortidlp_connection.send(url, params=parameters)

    def get_user(self, user_uuid: str, include_labels: Optional[bool] = None, include_agents: Optional[bool] = None) -> dict:
        return fortidlp_connection.get(_build_url(f'/api/v2/users/{user_uuid}', include_labels=include_labels, include_agents=include_agents))

    def aggregate_users(self, aggregations: list[dict], filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/users/aggregate', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {'aggregations': aggregations}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_user_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/users/terms')

    def get_user_archive_config(self) -> dict:
        return fortidlp_connection.get('/api/v2/users/archive/config')

    def update_user_archive_config(self, inactive_archive_enabled: Optional[bool] = None, inactive_archive_threshold: Optional[int] = None, archive_pending_enrollment_enabled: Optional[bool] = None, archived_pending_enrollment_threshold: Optional[int] = None) -> dict:
        parameters = {}
        if inactive_archive_enabled is not None:
            parameters['inactive_archive_enabled'] = inactive_archive_enabled
        if inactive_archive_threshold is not None:
            parameters['inactive_archive_threshold'] = inactive_archive_threshold
        if archive_pending_enrollment_enabled is not None:
            parameters['archive_pending_enrollment_enabled'] = archive_pending_enrollment_enabled
        if archived_pending_enrollment_threshold is not None:
            parameters['archived_pending_enrollment_threshold'] = archived_pending_enrollment_threshold
        return fortidlp_connection.insert('/api/v2/users/archive/config', params=parameters)

    def change_user_state(self, new_state: str, filter: list[str], reason: Optional[str] = None) -> dict:
        parameters = {'filter': _as_list(filter), 'new_state': new_state}
        if reason:
            parameters['reason'] = reason
        return fortidlp_connection.send('/api/v2/users/state', params=parameters)

    def get_user_agents(self, user_uuid: str, filter: list = None, include_actions: Optional[bool] = None, include_health: Optional[bool] = None, include_labels: Optional[bool] = None, include_licensed: Optional[bool] = None, include_users: Optional[bool] = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v2/users/{user_uuid}/agents/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        if include_actions is not None:
            parameters['include_actions'] = include_actions
        if include_health is not None:
            parameters['include_health'] = include_health
        if include_labels is not None:
            parameters['include_labels'] = include_labels
        if include_licensed is not None:
            parameters['include_licensed'] = include_licensed
        if include_users is not None:
            parameters['include_users'] = include_users
        return fortidlp_connection.send(url, params=parameters)

    def get_user_photo(self, user_uuid: str, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v2/users/{user_uuid}/photo', method='GET', file_format=file_format, download_folder=download_folder)

    def get_user_uris_v2(self, user_uuid: str) -> dict:
        return fortidlp_connection.get(f'/api/v2/users/{user_uuid}/useruri')

    def add_user_uri(self, user_uuid: str, uris: list[str]) -> dict:
        return fortidlp_connection.send(f'/api/v2/users/{user_uuid}/useruri/add', params={'uris': _as_list(uris)})

    def remove_user_uri(self, user_uuid: str, uris: list[str]) -> dict:
        return fortidlp_connection.send(f'/api/v2/users/{user_uuid}/useruri/remove', params={'uris': _as_list(uris)})

    def bulk_assign_user_uris(self, mappings: list[dict]) -> dict:
        return fortidlp_connection.send('/api/v2/users/bulk/useruri', params={'mappings': mappings})

    def export_users_csv(self, fields: Optional[list[str]] = None, filter: list = None, header: bool = True, download_folder: str = '') -> dict:
        parameters = {'header': header}
        if fields:
            parameters['fields'] = _as_list(fields)
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/users/export/csv', params=parameters, method='POST', file_format='csv', download_folder=download_folder)

    def export_users_xlsx(self, fields: Optional[list[str]] = None, filter: list = None, header: bool = True, download_folder: str = '') -> dict:
        parameters = {'header': header}
        if fields:
            parameters['fields'] = _as_list(fields)
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/users/export/xlsx', params=parameters, method='POST', file_format='xlsx', download_folder=download_folder)

    def get_exportable_user_fields(self) -> dict:
        return fortidlp_connection.get('/api/v2/users/export/fields')

    def export_user_uris_csv(self, filter: list = None, header: bool = True, include_juid: bool = False, download_folder: str = '') -> dict:
        parameters = {'header': header, 'include_juid': include_juid}
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/users/useruri/export/csv', params=parameters, method='POST', file_format='csv', download_folder=download_folder)


class Policies:
    '''Class Policies
    Description: Manage policy groups, policies, packs and data objects.
    '''

    def create_policies_groups(self, description: str, exclude_labels: list[str], include_labels: list[str], match: str, name: str, enabled: Optional[bool] = None, exclude_match: Optional[str] = None) -> dict:
        data = {
            'description': description,
            'exclude_labels': _as_list(exclude_labels),
            'include_labels': _as_list(include_labels),
            'match': match,
            'name': name,
        }
        if enabled is not None:
            data['enabled'] = enabled
        if exclude_match:
            data['exclude_match'] = exclude_match
        return fortidlp_connection.send('/api/v1/policies/groups', params=data)

    def list_policies_groups(self) -> dict:
        return fortidlp_connection.get('/api/v1/policies/groups')

    def get_policy_group(self, group_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/groups/{group_id}')

    def update_policy_group(self, group_id: str, **kwargs) -> dict:
        return fortidlp_connection.update(f'/api/v1/policies/groups/{group_id}', params=kwargs)

    def replace_policy_group(self, group_id: str, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/policies/groups/{group_id}', params=kwargs)

    def delete_policy_group(self, group_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/groups/{group_id}')

    def clone_policy_group(self, group_id: str, name: Optional[str] = None) -> dict:
        parameters = {}
        if name:
            parameters['name'] = name
        return fortidlp_connection.send(f'/api/v1/policies/groups/{group_id}/clone', params=parameters)

    def publish_policy_group(self, group_id: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/policies/groups/{group_id}/publish', params={})

    def publish_policy_groups(self, group_ids: list[str]) -> dict:
        return fortidlp_connection.send('/api/v1/policies/groups/publish', params={'group_ids': _as_list(group_ids)})

    def test_policies_groups(self, label_ids: list[str]) -> dict:
        return fortidlp_connection.send('/api/v1/policies/groups/test', params={'label_ids': _as_list(label_ids)})

    def assign_policy_group_label(self, group_id: str, label_id: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/policies/groups/{group_id}/labels/{label_id}', params={})

    def unassign_policy_group_label(self, group_id: str, label_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/groups/{group_id}/labels/{label_id}')

    def get_policy_group_labels(self, group_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/groups/{group_id}/labels')

    def assign_policy_group_exclude_label(self, group_id: str, label_id: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/policies/groups/{group_id}/exclude-labels/{label_id}', params={})

    def unassign_policy_group_exclude_label(self, group_id: str, label_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/groups/{group_id}/exclude-labels/{label_id}')

    def create_policy(self, group_id: str, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/policies/groups/{group_id}/policies', params=kwargs)

    def get_policy(self, group_id: str, policy_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}')

    def update_policy(self, group_id: str, policy_id: str, **kwargs) -> dict:
        return fortidlp_connection.update(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}', params=kwargs)

    def replace_policy(self, group_id: str, policy_id: str, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}', params=kwargs)

    def delete_policy(self, group_id: str, policy_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}')

    def get_policy_defaults(self, group_id: str, policy_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}/defaults')

    def assign_policy_exclude_label(self, group_id: str, policy_id: str, label_id: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}/exclude-labels/{label_id}', params={})

    def unassign_policy_exclude_label(self, group_id: str, policy_id: str, label_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/groups/{group_id}/policies/{policy_id}/exclude-labels/{label_id}')

    def fetch_policies(self, group_id: str) -> dict:
        return fortidlp_connection.send('/api/v1/policies/fetch', params={'group_id': group_id})

    def search_policies(self, filter: list = None, results_per_page: int = 100, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v1/policies/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_policy_terms(self) -> dict:
        return fortidlp_connection.get('/api/v1/policies/terms')

    def test_policies(self, label_ids: list[str]) -> dict:
        return fortidlp_connection.send('/api/v1/policies/test', params={'label_ids': _as_list(label_ids)})

    def export_policy_groups(self, group_ids: list[str], include_data_objects: bool = True, include_labels: bool = True, download_folder: str = '') -> dict:
        data = {'group_ids': _as_list(group_ids), 'include_data_objects': include_data_objects, 'include_labels': include_labels}
        return _download('/api/v1/policies/export', params=data, method='POST', file_format='zip', download_folder=download_folder)

    def list_policy_group_templates(self) -> dict:
        return fortidlp_connection.get('/api/v1/policies/group-templates')

    def list_policy_group_template_templates(self, template_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/group-templates/{template_id}/templates')

    def list_policy_packs(self, pack_type: Optional[str] = None) -> dict:
        return fortidlp_connection.get(_build_url('/api/v1/policies/packs', pack_type=pack_type))

    def get_policy_pack(self, pack_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/packs/{pack_id}')

    def delete_policy_pack(self, pack_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/packs/{pack_id}')

    def list_policy_pack_templates(self, pack_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/packs/{pack_id}/templates')

    def get_policy_pack_template(self, pack_id: str, template_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/packs/{pack_id}/templates/{template_id}')

    def upload_policy_packs(self, blob: str) -> dict:
        return fortidlp_connection.send('/api/v1/policies/packs/upload', params={'blob': blob})

    def list_policies_data(self, data_type: Optional[str] = None) -> dict:
        return fortidlp_connection.get(_build_url('/api/v1/policies/data', data_type=data_type))

    def create_policy_data(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/policies/data', params=kwargs)

    def upload_policy_data(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/policies/data/upload', params=kwargs)

    def get_policy_data(self, policy_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/data/{policy_id}')

    def update_policy_data(self, policy_id: str, **kwargs) -> dict:
        return fortidlp_connection.update(f'/api/v1/policies/data/{policy_id}', params=kwargs)

    def delete_policy_asset(self, asset_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/data/{asset_id}')

    def download_policy_data(self, policy_id: str, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/policies/data/{policy_id}/download', method='GET', file_format=file_format, download_folder=download_folder)
    def import_policy_groups(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/policies/import', params=kwargs)


class PoliciesData:
    '''Class PoliciesData
    Description: Compatibility wrapper for policy data endpoints.
    '''

    def list_policies_data(self, filter: list = None, results_per_page: int = 100, data_type: Optional[str] = None) -> dict:
        url = _build_url('/api/v1/policies/data', data_type=data_type)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        if results_per_page:
            parameters['results_per_page'] = results_per_page
        return fortidlp_connection.get(url, params=parameters)

    def create_policy_data(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/policies/data', params=kwargs)

    def upload_policy_data(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/policies/data/upload', params=kwargs)

    def get_policy_data(self, policy_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/policies/data/{policy_id}')

    def update_policy_data(self, policy_id: str, **kwargs) -> dict:
        return fortidlp_connection.update(f'/api/v1/policies/data/{policy_id}', params=kwargs)

    def delete_policy_data(self, policy_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/policies/data/{policy_id}')

    def download_policy_data(self, policy_id: str, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/policies/data/{policy_id}/download', method='GET', file_format=file_format, download_folder=download_folder)


class Incidents:
    '''Class Incidents
    Description: Search and manage incidents.
    '''

    def search_incidents(self, filter: list = None, include_agents: Optional[bool] = True, include_cluster_data: Optional[bool] = True, include_labels: Optional[bool] = True, include_users: Optional[bool] = True, results_per_page: int = 100, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/incidents/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        if include_agents is not None:
            parameters['include_agents'] = include_agents
        if include_cluster_data is not None:
            parameters['include_cluster_data'] = include_cluster_data
        if include_labels is not None:
            parameters['include_labels'] = include_labels
        if include_users is not None:
            parameters['include_users'] = include_users
        return fortidlp_connection.send(url, params=parameters)

    def get_incident(self, incident_id: str, include_labels: Optional[bool] = None, include_users: Optional[bool] = None, include_agents: Optional[bool] = None, include_cluster_data: Optional[bool] = None) -> dict:
        url = _build_url(f'/api/v2/incidents/{incident_id}', include_labels=include_labels, include_users=include_users, include_agents=include_agents, include_cluster_data=include_cluster_data)
        return fortidlp_connection.get(url)

    def aggregate_incidents(self, aggregations: list[dict], filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/incidents/aggregate', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {'aggregations': aggregations}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_incident_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/incidents/terms')

    def count_incident_agents(self, filter: list = None) -> dict:
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/incidents/agents/count', params=parameters)

    def count_incident_users(self, filter: list = None) -> dict:
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/incidents/users/count', params=parameters)

    def get_bounded_rule_entity_count(self, filter: list = None) -> dict:
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/incidents/bounded-rule-entity-count', params=parameters)

    def update_status(self, status: str, all: Optional[bool] = None, filter: Optional[list] = None, reason: Optional[str] = None) -> dict:
        parameters = {'status': status}
        if filter and not all:
            parameters['filter'] = _as_list(filter)
        if all and not filter:
            parameters['all'] = all
        if reason:
            parameters['reason'] = reason
        return fortidlp_connection.send('/api/v2/incidents/status', params=parameters)

    def get_incident_agents(self, incident_id: str, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v2/incidents/{incident_id}/agents/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_incident_users(self, incident_id: str, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v2/incidents/{incident_id}/users/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_incident_labels(self, incident_id: str, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v2/incidents/{incident_id}/labels/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)


class SaaS:
    '''Class SaaS
    Description: Manage SaaS applications.
    '''

    def search_applications(self, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/saas-applications/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def aggregate_applications(self, aggregations: list[dict], filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/saas-applications/aggregate', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {'aggregations': aggregations}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_application(self, application_id: str, include_login_counts: Optional[bool] = None) -> dict:
        return fortidlp_connection.get(_build_url(f'/api/v2/saas-applications/{application_id}', include_login_counts=include_login_counts))

    def get_application_icon(self, application_id: str, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v2/saas-applications/{application_id}/icon', method='GET', file_format=file_format, download_folder=download_folder)

    def get_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/saas-applications/terms')

    def get_template_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/saas-applications/templates/terms')

    def get_categories(self) -> dict:
        return fortidlp_connection.get('/api/v2/saas-applications/categories')

    def search_templates(self, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/saas-applications/templates', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def export_csv(self, fields: Optional[list[str]] = None, filter: list = None, header: bool = True, download_folder: str = '') -> dict:
        parameters = {'header': header}
        if fields:
            parameters['fields'] = _as_list(fields)
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/saas-applications/export/csv', params=parameters, method='POST', file_format='csv', download_folder=download_folder)

    def export_xlsx(self, fields: Optional[list[str]] = None, filter: list = None, header: bool = True, download_folder: str = '') -> dict:
        parameters = {'header': header}
        if fields:
            parameters['fields'] = _as_list(fields)
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/saas-applications/export/xlsx', params=parameters, method='POST', file_format='xlsx', download_folder=download_folder)

    def get_exportable_fields(self) -> dict:
        return fortidlp_connection.get('/api/v2/saas-applications/export/fields')

    def get_config(self) -> dict:
        return fortidlp_connection.get('/api/v2/saas-applications/config')

    def update_config(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/saas-applications/config', params=kwargs)

    def create_applications(self, application_ids: list[str]) -> dict:
        return fortidlp_connection.send('/api/v2/saas-applications/create', params={'application_ids': _as_list(application_ids)})

    def create_custom_application(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/saas-applications/custom/create', params=kwargs)

    def test_custom_application(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/saas-applications/custom/test', params=kwargs)

    def update_custom_application(self, application_id: str, **kwargs) -> dict:
        return fortidlp_connection.update(f'/api/v2/saas-applications/custom/{application_id}', params=kwargs)

    def upload_custom_application_icon(self, application_id: str, blob: str) -> dict:
        return fortidlp_connection.send(f'/api/v2/saas-applications/custom/{application_id}/icon', params={'blob': blob})

    def delete_custom_application_icon(self, application_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v2/saas-applications/custom/{application_id}/icon')

    def set_scores(self, score: int, all: Optional[bool] = None, filter: Optional[list] = None) -> dict:
        parameters = {'score': score}
        if all and not filter:
            parameters['all'] = all
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/saas-applications/scores', params=parameters)

    def reset_scores(self, all: Optional[bool] = None, filter: Optional[list] = None) -> dict:
        parameters = {}
        if all and not filter:
            parameters['all'] = all
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/saas-applications/scores/reset', params=parameters)

    def set_verdict(self, verdict: str, all: Optional[bool] = None, filter: Optional[list] = None) -> dict:
        parameters = {'verdict': verdict}
        if all and not filter:
            parameters['all'] = all
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/saas-applications/verdict', params=parameters)

    def allow_domainless_login(self, allow_domainless_login: bool, all: Optional[bool] = None, filter: Optional[list] = None) -> dict:
        parameters = {'allow_domainless_login': allow_domainless_login}
        if all and not filter:
            parameters['all'] = all
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/saas-applications/allow_domainless_login', params=parameters)

    def change_state(self, state: str, reason: str, all: Optional[bool] = None, filter: Optional[list] = None) -> dict:
        parameters = {'state': state, 'reason': reason}
        if all and not filter:
            parameters['all'] = all
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/saas-applications/state', params=parameters)

class Agents:
    '''Class Agents
    Description: Manage agent search and admin operations.
    '''

    def get_agents(self, filter: list = None, include_actions: Optional[bool] = None, include_health: Optional[bool] = None, include_labels: Optional[bool] = None, include_licensed: Optional[bool] = None, include_users: Optional[bool] = None, results_per_page: int = 100, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/agents/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        if include_actions is not None:
            parameters['include_actions'] = include_actions
        if include_health is not None:
            parameters['include_health'] = include_health
        if include_labels is not None:
            parameters['include_labels'] = include_labels
        if include_licensed is not None:
            parameters['include_licensed'] = include_licensed
        if include_users is not None:
            parameters['include_users'] = include_users
        return fortidlp_connection.send(url, params=parameters)

    def get_agent(self, agent_uuid: str, include_labels: Optional[bool] = None, include_users: Optional[bool] = None, include_actions: Optional[bool] = None, include_health: Optional[bool] = None, include_licensed: Optional[bool] = None) -> dict:
        url = _build_url(f'/api/v2/agents/{agent_uuid}', include_labels=include_labels, include_users=include_users, include_actions=include_actions, include_health=include_health, include_licensed=include_licensed)
        return fortidlp_connection.get(url)

    def aggregate_agents(self, aggregations: list[dict], filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/agents/aggregate', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {'aggregations': aggregations}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_agent_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/agents/terms')

    def get_enrolled_count(self) -> dict:
        return fortidlp_connection.get('/api/v2/agents/enrolled-count')

    def update_status(self, filter: Optional[list], new_state: Optional[str], reason: Optional[str]) -> dict:
        data = {'new_state': new_state, 'reason': reason}
        if filter:
            data['filter'] = _as_list(filter)
        return fortidlp_connection.send('/api/v2/agents/state', params=data)

    def revoke_agents(self, filter: list[str], reason: Optional[str] = None) -> dict:
        data = {'filter': _as_list(filter)}
        if reason:
            data['reason'] = reason
        return fortidlp_connection.send('/api/v2/agents/revoke', params=data)

    def export_agents_csv(self, fields: Optional[list[str]] = None, filter: list = None, header: bool = True, download_folder: str = '') -> dict:
        parameters = {'header': header}
        if fields:
            parameters['fields'] = _as_list(fields)
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/agents/export/csv', params=parameters, method='POST', file_format='csv', download_folder=download_folder)

    def export_agents_xlsx(self, fields: Optional[list[str]] = None, filter: list = None, header: bool = True, download_folder: str = '') -> dict:
        parameters = {'header': header}
        if fields:
            parameters['fields'] = _as_list(fields)
        if filter:
            parameters['filter'] = _as_list(filter)
        return _download('/api/v2/agents/export/xlsx', params=parameters, method='POST', file_format='xlsx', download_folder=download_folder)

    def get_exportable_agent_fields(self) -> dict:
        return fortidlp_connection.get('/api/v2/agents/export/fields')

    def get_agent_archive_config(self) -> dict:
        return fortidlp_connection.get('/api/v2/agents/archive/config')

    def update_agent_archive_config(self, inactive_archive_enabled: Optional[bool] = None, inactive_archive_threshold: Optional[int] = None, hardware_id_archive_enabled: Optional[bool] = None) -> dict:
        parameters = {}
        if inactive_archive_enabled is not None:
            parameters['inactive_archive_enabled'] = inactive_archive_enabled
        if inactive_archive_threshold is not None:
            parameters['inactive_archive_threshold'] = inactive_archive_threshold
        if hardware_id_archive_enabled is not None:
            parameters['hardware_id_archive_enabled'] = hardware_id_archive_enabled
        return fortidlp_connection.insert('/api/v2/agents/archive/config', params=parameters)

    def get_agent_components(self, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/agents/components', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_agent_component_faults(self, include_suppressed: Optional[bool] = None, include_archived: Optional[bool] = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v2/agents/components/faults', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort, include_suppressed=include_suppressed, include_archived=include_archived)
        return fortidlp_connection.get(url)

    def get_agent_component_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/agents/components/terms')

    def suppress_components(self, component_ids: list[str], filter: Optional[list] = None, all: Optional[bool] = None) -> dict:
        parameters = {'component_ids': _as_list(component_ids)}
        if filter:
            parameters['filter'] = _as_list(filter)
        if all is not None:
            parameters['all'] = all
        return fortidlp_connection.send('/api/v2/agents/components/suppress', params=parameters)

    def unsuppress_components(self, component_ids: list[str], filter: Optional[list] = None, all: Optional[bool] = None) -> dict:
        parameters = {'component_ids': _as_list(component_ids)}
        if filter:
            parameters['filter'] = _as_list(filter)
        if all is not None:
            parameters['all'] = all
        return fortidlp_connection.send('/api/v2/agents/components/unsuppress', params=parameters)

    def get_agent_components_by_agent(self, agent_uuid: str) -> dict:
        return fortidlp_connection.get(f'/api/v2/agents/{agent_uuid}/components')

    def suppress_components_by_agent(self, agent_uuid: str, component_ids: list[str]) -> dict:
        return fortidlp_connection.send(f'/api/v2/agents/{agent_uuid}/components/suppress', params={'component_ids': _as_list(component_ids)})

    def unsuppress_components_by_agent(self, agent_uuid: str, component_ids: list[str]) -> dict:
        return fortidlp_connection.send(f'/api/v2/agents/{agent_uuid}/components/unsuppress', params={'component_ids': _as_list(component_ids)})

    def get_agent_users(self, agent_uuid: str, filter: list = None, results_per_page: int = 20, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url(f'/api/v2/agents/{agent_uuid}/users/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def delete_archived_agents(self, agent_ids: list, archived_days: Optional[str] = None, inactive_days: Optional[int] = None, never_reported: Optional[bool] = None, revoked_days: Optional[str] = None) -> dict:
        data = {'agent_ids': _as_list(agent_ids)}
        if archived_days:
            data['archived_days'] = archived_days
        if inactive_days is not None:
            data['inactive_days'] = inactive_days
        if never_reported is not None:
            data['never_reported'] = never_reported
        if revoked_days:
            data['revoked_days'] = revoked_days
        return fortidlp_connection.insert('/api/v1/admin/agents/archived/delete', params=data)

    def assign_labels(self, agent_ids: list[str], label_ids: list[str]) -> dict:
        return fortidlp_connection.insert('/api/v1/admin/agents/labels/add', params={'agent_ids': _as_list(agent_ids), 'label_ids': _as_list(label_ids)})

    def unassign_labels(self, agent_ids: list[str], label_ids: list[str]) -> dict:
        return fortidlp_connection.insert('/api/v1/admin/agents/labels/remove', params={'agent_ids': _as_list(agent_ids), 'label_ids': _as_list(label_ids)})

    def add_labels(self, filter: list[str], labels: list[str]) -> dict:
        return fortidlp_connection.send('/api/v2/agents/labels/add', params={'filter': _as_list(filter), 'labels': _as_list(labels)})

    def remove_labels(self, filter: list[str], labels: list[str]) -> dict:
        return fortidlp_connection.send('/api/v2/agents/labels/remove', params={'filter': _as_list(filter), 'labels': _as_list(labels)})

    def get_agent_updates(self) -> dict:
        return fortidlp_connection.get('/api/v1/admin/agents/updates')

    def download_agent_binary(self, version: str, operating_system: str, variant: str, file_format: str = 'bin', download_folder: str = '') -> dict:
        url = _build_url('/api/v1/admin/agents/binaries', version=version, operating_system=operating_system, variant=variant)
        return _download(url, method='GET', file_format=file_format, download_folder=download_folder)

    def create_agent_enrollment_bundle(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/admin/agents/enroll', params=kwargs)

    def get_agent_crashes(self, agent_id: Optional[str] = None) -> dict:
        if agent_id:
            return fortidlp_connection.get(f'/api/v1/admin/agents/{agent_id}/crashes')
        return fortidlp_connection.get('/api/v1/admin/agents/crashes')

    def delete_agent_crashes(self, agent_id: Optional[str] = None) -> dict:
        if agent_id:
            return fortidlp_connection.delete(f'/api/v1/admin/agents/{agent_id}/crashes')
        return fortidlp_connection.delete('/api/v1/admin/agents/crashes')

    def download_agent_crash(self, agent_id: str, crash_id: str, file_format: str = 'zip', download_folder: str = '') -> dict:
        return _download(f'/api/v1/admin/agents/{agent_id}/crashes/{crash_id}', method='GET', file_format=file_format, download_folder=download_folder)

    def delete_agent_crash(self, agent_id: str, crash_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/admin/agents/{agent_id}/crashes/{crash_id}')

    def get_agent_labels(self, agent_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/admin/agents/{agent_id}/labels')

    def get_agent_classifications(self, agent_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/admin/agents/{agent_id}/classifications')

    def assign_agent_classification(self, agent_id: str, classification_id: str, reason: Optional[str] = None) -> dict:
        parameters = {}
        if reason:
            parameters['reason'] = reason
        return fortidlp_connection.send(f'/api/v1/admin/agents/{agent_id}/classifications/{classification_id}', params=parameters)

    def remove_agent_classification(self, agent_id: str, classification_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/admin/agents/{agent_id}/classifications/{classification_id}')

    def exclude_agent_classification(self, agent_id: str, classification_id: str, reason: Optional[str] = None) -> dict:
        parameters = {}
        if reason:
            parameters['reason'] = reason
        return fortidlp_connection.send(f'/api/v1/admin/agents/{agent_id}/classifications/{classification_id}/exclude', params=parameters)


class AgentConfigs:
    '''Class AgentConfigs
    Description: Manage agent configurations.
    '''

    def get_agent_configs(self) -> dict:
        return fortidlp_connection.get('/api/v1/agent-configs')

    def create_agent_config(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/agent-configs', params=kwargs)

    def get_agent_config(self, config_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/agent-configs/{config_id}')

    def update_agent_config(self, config_id: str, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/agent-configs/{config_id}', params=kwargs)

    def delete_agent_config(self, config_id: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/agent-configs/{config_id}')

    def export_agent_configs(self, config_ids: list[str], include_labels: Optional[bool] = None, download_folder: str = '') -> dict:
        parameters = {'config_ids': _as_list(config_ids)}
        if include_labels is not None:
            parameters['include_labels'] = include_labels
        return _download('/api/v1/agent-configs/export', params=parameters, method='POST', file_format='zip', download_folder=download_folder)

    def import_agent_configs(self, blob: str, include_labels: Optional[bool] = None) -> dict:
        url = _build_url('/api/v1/agent-configs/import', include_labels=include_labels)
        return fortidlp_connection.send(url, params={'blob': blob})

    def test_agent_configs(self, label_uuids: list[str]) -> dict:
        return fortidlp_connection.send('/api/v1/agent-configs/test', params={'label_uuids': _as_list(label_uuids)})

    def get_agent_config_key(self, config_id: str, key: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/agent-configs/{config_id}/keys/{key}')

    def set_agent_config_key(self, config_id: str, key: str, value) -> dict:
        return fortidlp_connection.send(f'/api/v1/agent-configs/{config_id}/keys/{key}', params={'value': value})

    def delete_agent_config_key(self, config_id: str, key: str) -> dict:
        return fortidlp_connection.delete(f'/api/v1/agent-configs/{config_id}/keys/{key}')

    def get_agent_config_labels(self, config_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/agent-configs/{config_id}/labels')

    def assign_agent_config_labels(self, config_id: str, label_ids: list[str]) -> dict:
        return fortidlp_connection.insert(f'/api/v1/agent-configs/{config_id}/labels', params={'label_ids': _as_list(label_ids)})

    def unassign_agent_config_labels(self, config_id: str, label_ids: list[str]) -> dict:
        return fortidlp_connection.delete(f'/api/v1/agent-configs/{config_id}/labels', params={'label_ids': _as_list(label_ids)})


class AgentEnrollment:
    '''Class AgentEnrollment
    Description: Manage agent enrollment tokens.
    '''

    def get_bootstrap_token(self) -> dict:
        return fortidlp_connection.get('/api/v1/enrollment/bootstrap-token')

    def get_tokens(self) -> dict:
        return fortidlp_connection.get('/api/v1/enrollment/tokens')

    def create_token(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/enrollment/tokens', params=kwargs)

    def get_token(self, token_id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/enrollment/tokens/{token_id}')

    def update_token(self, token_id: str, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/enrollment/tokens/{token_id}', params=kwargs)

    def download_token_bundle(self, token_id: str, file_format: str = 'zip', download_folder: str = '') -> dict:
        return _download(f'/api/v1/enrollment/tokens/{token_id}/bundle', method='GET', file_format=file_format, download_folder=download_folder)

    def revoke_token(self, token_id: str) -> dict:
        return fortidlp_connection.send(f'/api/v1/enrollment/tokens/{token_id}/revoke', params={})


class Labels:
    '''Class Labels
    Description: Manage labels.
    '''

    def create(self, name: str, description: Optional[str] = None, category: Optional[str] = None, anonymise: Optional[bool] = False, flagged: Optional[bool] = False) -> dict:
        data = {'name': name}
        if description:
            data['description'] = description
        if category:
            data['category'] = category
        if anonymise is not None:
            data['anonymise'] = anonymise
        if flagged is not None:
            data['flagged'] = flagged
        return fortidlp_connection.send('/api/v1/labels', params=data)

    def get(self, id: str) -> dict:
        return fortidlp_connection.get(f'/api/v1/labels/{id}')

    def update(self, id: str, name: Optional[str] = None, description: Optional[str] = None, category: Optional[str] = None, anonymise: Optional[bool] = None, flagged: Optional[bool] = None) -> dict:
        data = {}
        if name:
            data['name'] = name
        if description:
            data['description'] = description
        if category:
            data['category'] = category
        if anonymise is not None:
            data['anonymise'] = anonymise
        if flagged is not None:
            data['flagged'] = flagged
        return fortidlp_connection.update(f'/api/v1/labels/{id}', params=data)

    def delete(self, id: str, force: Optional[bool] = False) -> dict:
        return fortidlp_connection.delete(_build_url(f'/api/v1/labels/{id}', force=force if force else None))

    def get_labels(self, filter: list = None, results_per_page: int = 100, sort_order: str = 'asc', sort: Optional[str] = None, cursor: Optional[str] = None) -> dict:
        url = _build_url('/api/v1/labels/search', cursor=cursor, results_per_page=results_per_page, sort_order=sort_order, sort=sort)
        parameters = {}
        if filter:
            parameters['filter'] = _as_list(filter)
        return fortidlp_connection.send(url, params=parameters)

    def get_label_terms(self) -> dict:
        return fortidlp_connection.get('/api/v1/labels/terms')


class AccessTokens:
    '''Class AccessTokens
    Description: Manage AccessTokens endpoints.
    '''

    def get_access_tokens(self) -> dict:
        return fortidlp_connection.get('/api/v1/access-tokens')

    def create_access_token(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/access-tokens', params=kwargs)

    def get_access_token(self, jti) -> dict:
        return fortidlp_connection.get(f'/api/v1/access-tokens/{jti}')

    def revoke_access_token(self, jti) -> dict:
        return fortidlp_connection.send(f'/api/v1/access-tokens/{jti}/revoke', params={})


class Admin:
    '''Class Admin
    Description: Manage Admin endpoints.
    '''

    def delete_login_banner_info(self) -> dict:
        return fortidlp_connection.delete('/api/v1/admin/login/banner')

    def get_login_banner_info(self) -> dict:
        return fortidlp_connection.get('/api/v1/admin/login/banner')

    def update_login_banner_info(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/admin/login/banner', params=kwargs)

    def get_operator_sessions(self) -> dict:
        return fortidlp_connection.get('/api/v1/admin/operator_sessions')

    def revoke_operator_session(self, id) -> dict:
        return fortidlp_connection.send(f'/api/v1/admin/operator_sessions/{id}/revoke', params={})

    def get_version(self) -> dict:
        return fortidlp_connection.get('/api/v1/admin/version')


class AgentActions:
    '''Class AgentActions
    Description: Manage AgentActions endpoints.
    '''

    def post_action(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/actions', params=kwargs)

    def delete_active_actions(self, **kwargs) -> dict:
        return fortidlp_connection.delete('/api/v1/actions/active', params=kwargs)

    def post_active_actions(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/actions/active', params=kwargs)

    def get_available_actions(self) -> dict:
        return fortidlp_connection.get('/api/v1/actions/available')

    def post_available_actions(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/actions/available', params=kwargs)

    def delete_debug_bundle(self, agent_uuid, action_uuid, filename) -> dict:
        return fortidlp_connection.delete(f'/api/v1/actions/debug-bundles/{agent_uuid}/{action_uuid}/{filename}')

    def get_debug_bundle(self, agent_uuid, action_uuid, filename, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/actions/debug-bundles/{agent_uuid}/{action_uuid}/{filename}', params=None, method='GET', file_format=file_format, download_folder=download_folder)

    def delete_performance_report(self, agent_uuid, action_uuid, filename) -> dict:
        return fortidlp_connection.delete(f'/api/v1/actions/performance-reports/{agent_uuid}/{action_uuid}/{filename}')

    def get_performance_report(self, agent_uuid, action_uuid, filename, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/actions/performance-reports/{agent_uuid}/{action_uuid}/{filename}', params=None, method='GET', file_format=file_format, download_folder=download_folder)

    def delete_screenshot(self, agent_uuid, action_uuid, filename) -> dict:
        return fortidlp_connection.delete(f'/api/v1/actions/screenshots/{agent_uuid}/{action_uuid}/{filename}')

    def get_screenshot(self, agent_uuid, action_uuid, filename, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/actions/screenshots/{agent_uuid}/{action_uuid}/{filename}', params=None, method='GET', file_format=file_format, download_folder=download_folder)

    def trigger_action(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/actions/trigger', params=kwargs)

    def get_in_flight_actions(self, agent_uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/actions/{agent_uuid}/in-flight')

    def delete_action_content(self, agent_uuid, action_uuid, filename) -> dict:
        return fortidlp_connection.delete(f'/api/v1/actions/{agent_uuid}/{action_uuid}/{filename}')

    def get_action_content(self, agent_uuid, action_uuid, filename, file_format: str = 'bin', download_folder: str = '') -> dict:
        return _download(f'/api/v1/actions/{agent_uuid}/{action_uuid}/{filename}', params=None, method='GET', file_format=file_format, download_folder=download_folder)


class AgentOfflineConfig:
    '''Class AgentOfflineConfig
    Description: Manage AgentOfflineConfig endpoints.
    '''

    def get_agent_offline_config(self) -> dict:
        return fortidlp_connection.get('/api/v1/agentoffline/config')

    def update_agent_offline_config(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/agentoffline/config', params=kwargs)


class Box:
    '''Class Box
    Description: Manage Box endpoints.
    '''

    def box_service_list_credentials(self) -> dict:
        return fortidlp_connection.get('/api/v1/box/credentials')

    def box_service_create_credentials(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/box/credentials', params=kwargs)

    def box_service_verify_credentials(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/box/credentials/verify', params=kwargs)

    def box_service_delete_credentials(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/box/credentials/{uuid}')

    def box_service_get_credentials(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/box/credentials/{uuid}')

    def box_service_update_credentials(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/box/credentials/{uuid}', params=kwargs)

    def box_service_verify_saved_credentials(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/box/credentials/{uuid}/verify')

    def list_saas_box_subscriptions(self) -> dict:
        return fortidlp_connection.get('/api/v1/box/drive')

    def create_saas_box_subscription(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/box/drive', params=kwargs)

    def cancel_saas_box_subscription(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/box/drive/{id}')

    def get_saas_box_subscription(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/box/drive/{id}')

    def update_saas_box_subscription(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/box/drive/{id}', params=kwargs)


class BoxDirectory:
    '''Class BoxDirectory
    Description: Manage BoxDirectory endpoints.
    '''

    def get_box_directory_configs(self) -> dict:
        return fortidlp_connection.get('/api/v1/box/directory/configs')

    def add_box_directory_config(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/box/directory/configs', params=kwargs)

    def delete_box_directory_config(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/box/directory/configs/{id}')

    def get_box_directory_config(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/box/directory/configs/{id}')

    def update_box_directory_config(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/box/directory/configs/{id}', params=kwargs)

    def sync_box_directory(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/box/directory/configs/{id}/sync', params=kwargs)

    def sync_box_directory_groups(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/box/directory/configs/{id}/sync/groups', params=kwargs)

    def list_box_directory_groups(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/box/directory/groups', params=kwargs)


class Classifications:
    '''Class Classifications
    Description: Manage Classifications endpoints.
    '''

    def get_classifications(self) -> dict:
        return fortidlp_connection.get('/api/v1/classifications')

    def get_classification(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/classifications/{id}')


class CloudActions:
    '''Class CloudActions
    Description: Manage CloudActions endpoints.
    '''

    def get_available_cloud_actions(self) -> dict:
        return fortidlp_connection.get('/api/v1/cloud-actions/available')

    def delete_cloud_message_platform_defaults(self, **kwargs) -> dict:
        return fortidlp_connection.delete('/api/v1/cloud-actions/messages/platform-defaults', params=kwargs)

    def get_cloud_message_platform_defaults(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/cloud-actions/messages/platform-defaults', params=kwargs)

    def update_cloud_message_platform_defaults(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/cloud-actions/messages/platform-defaults', params=kwargs)


class Dashboards:
    '''Class Dashboards
    Description: Manage Dashboards endpoints.
    '''

    def get_dashboards(self) -> dict:
        return fortidlp_connection.get('/api/v2/dashboards')

    def create_dashboard(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/dashboards', params=kwargs)

    def get_widget_templates(self) -> dict:
        return fortidlp_connection.get('/api/v2/dashboards/templates')

    def delete_dashboard(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v2/dashboards/{uuid}')

    def get_dashboard(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v2/dashboards/{uuid}')

    def update_dashboard(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v2/dashboards/{uuid}', params=kwargs)


class DriveLabelsScheduledSync:
    '''Class DriveLabelsScheduledSync
    Description: Manage DriveLabelsScheduledSync endpoints.
    '''

    def create_scheduled_sync_google_drive_labels(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/google/drive/labels/schedule-sync', params=kwargs)

    def list_scheduled_sync_google_drive_labels(self) -> dict:
        return fortidlp_connection.get('/api/v1/google/drive/labels/schedule-sync/list')

    def remove_scheduled_sync_google_drive_labels(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/google/drive/labels/schedule-sync/{uuid}')

    def get_scheduled_sync_google_drive_labels(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/google/drive/labels/schedule-sync/{uuid}')

    def update_scheduled_sync_google_drive_labels(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/google/drive/labels/schedule-sync/{uuid}', params=kwargs)

    def create_scheduled_sync_information_protection_labels(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/onedrive/labels/schedule-sync', params=kwargs)

    def list_scheduled_sync_information_protection_labels(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/onedrive/labels/schedule-sync/list')

    def remove_scheduled_sync_information_protection_labels(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/microsoft/onedrive/labels/schedule-sync/{uuid}')

    def get_scheduled_sync_information_protection_labels(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/microsoft/onedrive/labels/schedule-sync/{uuid}')

    def update_scheduled_sync_information_protection_labels(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/microsoft/onedrive/labels/schedule-sync/{uuid}', params=kwargs)


class Emails:
    '''Class Emails
    Description: Manage Emails endpoints.
    '''

    def list_email_notifications(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/emails', params=kwargs)

    def create_email_notification(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/emails', params=kwargs)

    def email_verify_link_handler(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/emails-verify', params=kwargs)

    def delete_email_notification(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/emails/{id}')

    def get_email_notification(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/emails/{id}')

    def update_email_notification(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/emails/{id}', params=kwargs)

    def verify_email_address(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/emails/{id}/verify', params=kwargs)


class EntraID:
    '''Class EntraID
    Description: Manage EntraID endpoints.
    '''

    def get_entra_id_configs(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/entraid/configs')

    def add_entra_id_config(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/entraid/configs', params=kwargs)

    def delete_entra_id_config(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/microsoft/entraid/configs/{id}')

    def get_entra_id_config(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/microsoft/entraid/configs/{id}')

    def update_entra_id_config(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/microsoft/entraid/configs/{id}', params=kwargs)

    def sync_entra_id(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/microsoft/entraid/configs/{id}/sync', params=kwargs)

    def sync_entra_id_groups(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/microsoft/entraid/configs/{id}/sync/groups', params=kwargs)

    def count_entra_id_users(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/entraid/count', params=kwargs)

    def list_entra_id_groups(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/entraid/groups', params=kwargs)


class Events:
    '''Class Events
    Description: Manage Events endpoints.
    '''

    def get_event(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/events', params=kwargs)

    def get_events(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/events', params=kwargs)


class FileShadow:
    '''Class FileShadow
    Description: Manage FileShadow endpoints.
    '''

    def delete_file_shadow_storage_config(self, **kwargs) -> dict:
        return fortidlp_connection.delete('/api/v1/fileshadow/config', params=kwargs)

    def get_file_shadow_storage_config(self) -> dict:
        return fortidlp_connection.get('/api/v1/fileshadow/config')

    def put_file_shadow_storage_config(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/fileshadow/config', params=kwargs)

    def get_file_shadow_test_config(self) -> dict:
        return fortidlp_connection.get('/api/v1/fileshadow/config/test')

    def get_decryption_tool_versions(self) -> dict:
        return fortidlp_connection.get('/api/v1/fileshadow/decryption-tool')

    def get_file_shadow_evidence(self, action_uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/fileshadow/evidence/{action_uuid}')

    def get_file_shadow_evidence_for_agent(self, agent_uuid, action_uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/fileshadow/evidence/{agent_uuid}/{action_uuid}')

    def get_file_shadow_recipients(self) -> dict:
        return fortidlp_connection.get('/api/v1/fileshadow/recipients')

    def delete_file_shadow_recipient(self, name) -> dict:
        return fortidlp_connection.delete(f'/api/v1/fileshadow/recipients/{name}')

    def get_file_shadow_recipient(self, name) -> dict:
        return fortidlp_connection.get(f'/api/v1/fileshadow/recipients/{name}')

    def put_file_shadow_recipient(self, name, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/fileshadow/recipients/{name}', params=kwargs)

    def get_clipboard_forensic_evidence_for_agent(self, agent_uuid, action_uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/forensic-evidence/clipboard/{agent_uuid}/{action_uuid}')

    def get_fileshadow_forensic_evidence_for_agent(self, agent_uuid, action_uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/forensic-evidence/fileshadow/{agent_uuid}/{action_uuid}')

    def get_screenshot_forensic_evidence_for_agent(self, agent_uuid, action_uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/forensic-evidence/screenshot/{agent_uuid}/{action_uuid}')


class GlobalOperators:
    '''Class GlobalOperators
    Description: Manage GlobalOperators endpoints.
    '''

    def delete_global_operator(self, **kwargs) -> dict:
        return fortidlp_connection.delete('/api/v2/global-operators', params=kwargs)

    def get_global_operator(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v2/global-operators', params=kwargs)

    def get_global_operators(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/global-operators/search', params=kwargs)

    def global_operator_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/global-operators/terms')


class Google:
    '''Class Google
    Description: Manage Google endpoints.
    '''

    def google_service_list_credentials(self) -> dict:
        return fortidlp_connection.get('/api/v1/google/credentials')

    def google_service_create_credentials(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/google/credentials', params=kwargs)

    def google_service_verify_credentials(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/google/credentials/verify', params=kwargs)

    def google_service_delete_credentials(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/google/credentials/{uuid}')

    def google_service_get_credentials(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/google/credentials/{uuid}')

    def google_service_update_credentials(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/google/credentials/{uuid}', params=kwargs)

    def google_service_verify_saved_credentials(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/google/credentials/{uuid}/verify')

    def list_saas_google_drive_subscriptions(self) -> dict:
        return fortidlp_connection.get('/api/v1/google/drive')

    def create_saas_google_drive_subscription(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/google/drive', params=kwargs)

    def list_google_drive_labels(self) -> dict:
        return fortidlp_connection.get('/api/v1/google/drive-labels')

    def sync_google_drive_labels(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/google/drive-labels/sync', params=kwargs)

    def get_google_drive_label(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/google/drive-labels/{id}')

    def cancel_saas_google_drive_subscription(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/google/drive/{id}')

    def get_saas_google_drive_subscription(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/google/drive/{id}')

    def update_saas_google_drive_subscription(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/google/drive/{id}', params=kwargs)


class GoogleDirectory:
    '''Class GoogleDirectory
    Description: Manage GoogleDirectory endpoints.
    '''

    def get_google_directory_configs(self) -> dict:
        return fortidlp_connection.get('/api/v1/google/directory/configs')

    def add_google_directory_config(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/google/directory/configs', params=kwargs)

    def delete_google_directory_config(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/google/directory/configs/{id}')

    def get_google_directory_config(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/google/directory/configs/{id}')

    def update_google_directory_config(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/google/directory/configs/{id}', params=kwargs)

    def sync_google_directory(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/google/directory/configs/{id}/sync', params=kwargs)

    def sync_google_directory_groups(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/google/directory/configs/{id}/sync/groups', params=kwargs)

    def list_google_directory_groups(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/google/directory/groups', params=kwargs)


class Indicators:
    '''Class Indicators
    Description: Manage Indicators endpoints.
    '''

    def get_indicators(self) -> dict:
        return fortidlp_connection.get('/api/v1/indicators')

    def get_tactics(self) -> dict:
        return fortidlp_connection.get('/api/v1/indicators/tactics')

    def get_techniques(self) -> dict:
        return fortidlp_connection.get('/api/v1/indicators/techniques')


class Ldap:
    '''Class Ldap
    Description: Manage Ldap endpoints.
    '''

    def get_ldap_configs(self) -> dict:
        return fortidlp_connection.get('/api/v1/admin/ldap/config')

    def add_ldap_config(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/admin/ldap/config', params=kwargs)

    def delete_ldap_config(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/admin/ldap/config/{id}')

    def get_ldap_config(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/admin/ldap/config/{id}')

    def update_ldap_config(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/admin/ldap/config/{id}', params=kwargs)

    def get_ldap_sync_status(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/admin/ldap/config/{id}/status')

    def update_ldap_sync_status(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/admin/ldap/config/{id}/status', params=kwargs)

    def get_ldap_sync_tool_versions(self) -> dict:
        return fortidlp_connection.get('/api/v1/admin/ldap/sync-tool')

    def sync_ldap(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/admin/ldap/sync/{id}', params=kwargs)


class Locations:
    '''Class Locations
    Description: Manage Locations endpoints.
    '''

    def get_locations(self) -> dict:
        return fortidlp_connection.get('/api/v1/locations')

    def add_location(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/locations', params=kwargs)

    def query_locations(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/locations/query', params=kwargs)

    def delete_location(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/locations/{id}')

    def get_location(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/locations/{id}')

    def update_location(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/locations/{id}', params=kwargs)

    def get_subnets(self, id, location_id) -> dict:
        return fortidlp_connection.get(f'/api/v1/locations/{location_id}/subnets')

    def add_subnet(self, location_id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/locations/{location_id}/subnets', params=kwargs)

    def delete_subnet(self, location_id, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/locations/{location_id}/subnets/{id}')

    def get_subnet(self, location_id, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/locations/{location_id}/subnets/{id}')


class MFA:
    '''Class MFA
    Description: Manage MFA endpoints.
    '''

    def mfa_service_get_info(self) -> dict:
        return fortidlp_connection.get('/api/v1/authentication/mfa')

    def delete_totp(self) -> dict:
        return fortidlp_connection.delete('/api/v1/authentication/mfa/totp')

    def start_register_totp(self) -> dict:
        return fortidlp_connection.get('/api/v1/authentication/mfa/totp/register')

    def finish_register_totp(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/authentication/mfa/totp/register', params=kwargs)

    def start_register_webauthn(self) -> dict:
        return fortidlp_connection.get('/api/v1/authentication/mfa/webauthn/register')

    def finish_register_webauthn(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/authentication/mfa/webauthn/register', params=kwargs)

    def delete_webauthn(self, name) -> dict:
        return fortidlp_connection.delete(f'/api/v1/authentication/mfa/webauthn/{name}')


class ManagedServiceReports:
    '''Class ManagedServiceReports
    Description: Manage ManagedServiceReports endpoints.
    '''

    def list_reports(self) -> dict:
        return fortidlp_connection.get('/api/v1/managed-service-reports')

    def download_report(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/managed-service-reports/{uuid}')


class Microsoft:
    '''Class Microsoft
    Description: Manage Microsoft endpoints.
    '''

    def microsoft_service_list_credentials(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/credentials')

    def microsoft_service_create_credentials(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/credentials', params=kwargs)

    def microsoft_service_verify_credentials(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/credentials/verify', params=kwargs)

    def microsoft_service_delete_credentials(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/microsoft/credentials/{uuid}')

    def microsoft_service_get_credentials(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/microsoft/credentials/{uuid}')

    def microsoft_service_update_credentials(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/microsoft/credentials/{uuid}', params=kwargs)

    def microsoft_service_verify_saved_credentials(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/microsoft/credentials/{uuid}/verify')

    def list_saas_microsoft_onedrive_subscriptions(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/onedrive')

    def create_saas_microsoft_onedrive_subscription(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/onedrive', params=kwargs)

    def list_microsoft_information_protection_labels(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/onedrive/labels')

    def sync_information_protection_labels(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/microsoft/onedrive/labels/sync', params=kwargs)

    def get_microsoft_information_protection_label(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/microsoft/onedrive/labels/{id}')

    def cancel_saas_microsoft_onedrive_subscription(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/microsoft/onedrive/{id}')

    def get_saas_microsoft_onedrive_subscription(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/microsoft/onedrive/{id}')

    def update_saas_microsoft_onedrive_subscription(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/microsoft/onedrive/{id}', params=kwargs)

    def set_teams_enabled(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/microsoft/teams/enable', params=kwargs)

    def get_teams_enabled(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/teams/enabled')

    def teams_health(self) -> dict:
        return fortidlp_connection.get('/api/v1/microsoft/teams/health')


class OperatorPreferences:
    '''Class OperatorPreferences
    Description: Manage OperatorPreferences endpoints.
    '''

    def reset_operator_preferences(self) -> dict:
        return fortidlp_connection.delete('/api/v1/operator-preferences')

    def list_operator_preferences(self) -> dict:
        return fortidlp_connection.get('/api/v1/operator-preferences')

    def set_operator_preference(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/operator-preferences', params=kwargs)

    def delete_operator_preference(self, key) -> dict:
        return fortidlp_connection.delete(f'/api/v1/operator-preferences/{key}')

    def get_operator_preference(self, key) -> dict:
        return fortidlp_connection.get(f'/api/v1/operator-preferences/{key}')


class Outlook:
    '''Class Outlook
    Description: Manage Outlook endpoints.
    '''

    def delete_certificate(self) -> dict:
        return fortidlp_connection.delete('/api/v1/outloook/certificate')

    def outlook_service_get_certificate(self) -> dict:
        return fortidlp_connection.get('/api/v1/outloook/certificate')

    def renew_certificate(self) -> dict:
        return fortidlp_connection.send('/api/v1/outloook/certificate', params={})


class Passphrase:
    '''Class Passphrase
    Description: Manage Passphrase endpoints.
    '''

    def handle_forgotten_passphrase(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/forgotten-passphrase', params=kwargs)

    def set_passphrase(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/passphrase', params=kwargs)

    def change_passphrase(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/passphrase', params=kwargs)

    def passphrase_reset_link_handler(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/passphrase-reset', params=kwargs)

    def test_passphrase(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/passphrase/test', params=kwargs)


class Permissions:
    '''Class Permissions
    Description: Manage Permissions endpoints.
    '''

    def get_permissions(self) -> dict:
        return fortidlp_connection.get('/api/v1/permissions')


class Perspectives:
    '''Class Perspectives
    Description: Manage Perspectives endpoints.
    '''

    def get_perspectives(self) -> dict:
        return fortidlp_connection.get('/api/v1/perspectives')

    def create_perspective(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/perspectives', params=kwargs)

    def delete_perspective(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v1/perspectives/{id}')

    def get_perspective(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/perspectives/{id}')


class Quota:
    '''Class Quota
    Description: Manage Quota endpoints.
    '''

    def get_license(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/license', params=kwargs)

    def refresh_license_status(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/license/refresh', params=kwargs)

    def get_license_status(self) -> dict:
        return fortidlp_connection.get('/api/v1/license/status')


class Roles:
    '''Class Roles
    Description: Manage Roles endpoints.
    '''

    def get_roles(self) -> dict:
        return fortidlp_connection.get('/api/v1/roles')

    def create_role(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/roles', params=kwargs)

    def delete_role(self, id, **kwargs) -> dict:
        return fortidlp_connection.delete(f'/api/v1/roles/{id}', params=kwargs)

    def get_role(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/roles/{id}')

    def update_role(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/roles/{id}', params=kwargs)


class SAML:
    '''Class SAML
    Description: Manage SAML endpoints.
    '''

    def delete_config(self) -> dict:
        return fortidlp_connection.delete('/api/v1/saml/config')

    def get_config_2(self) -> dict:
        return fortidlp_connection.get('/api/v1/saml/config')

    def edit_config(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/saml/config', params=kwargs)

    def delete_crypto_keys(self) -> dict:
        return fortidlp_connection.delete('/api/v1/saml/cryptokeys')

    def saml_service_get_certificate(self) -> dict:
        return fortidlp_connection.get('/api/v1/saml/cryptokeys')

    def create_crypto_keys(self) -> dict:
        return fortidlp_connection.send('/api/v1/saml/cryptokeys', params={})

    def edit_crypto_keys(self, **kwargs) -> dict:
        return fortidlp_connection.insert('/api/v1/saml/cryptokeys', params=kwargs)

    def saml_service_get_info(self) -> dict:
        return fortidlp_connection.get('/api/v1/saml/info')


class SavedQueries:
    '''Class SavedQueries
    Description: Manage SavedQueries endpoints.
    '''

    def get_saved_queries(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v2/search/queries', params=kwargs)

    def create_saved_query(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/search/queries', params=kwargs)

    def delete_saved_query(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v2/search/queries/{uuid}')

    def get_saved_query(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v2/search/queries/{uuid}')

    def update_saved_query(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v2/search/queries/{uuid}', params=kwargs)


class ScopedInvestigations:
    '''Class ScopedInvestigations
    Description: Manage ScopedInvestigations endpoints.
    '''

    def list_scoped_investigations(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v2/scoped-investigations', params=kwargs)

    def assign_scoped_investigation(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/scoped-investigations', params=kwargs)

    def clear_active_scoped_investigation(self) -> dict:
        return fortidlp_connection.delete('/api/v2/scoped-investigations/active')

    def scoped_investigation_aggregation(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/scoped-investigations/aggregate', params=kwargs)

    def list_scoped_investigation_requests(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v2/scoped-investigations/requests', params=kwargs)

    def request_scoped_investigation(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/scoped-investigations/requests', params=kwargs)

    def scoped_investigation_request_aggregation(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/scoped-investigations/requests/aggregate', params=kwargs)

    def get_scoped_investigation_request(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v2/scoped-investigations/requests/{uuid}')

    def update_scoped_investigation_request(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/scoped-investigations/requests/{uuid}', params=kwargs)

    def activate_scoped_investigation(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/scoped-investigations/requests/{uuid}/activate', params=kwargs)

    def cancel_scoped_investigation_request(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/scoped-investigations/requests/{uuid}/cancel', params=kwargs)

    def get_scoped_investigation_terms(self) -> dict:
        return fortidlp_connection.get('/api/v2/scoped-investigations/terms')

    def get_scoped_investigation(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v2/scoped-investigations/{uuid}')

    def update_scoped_investigation(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/scoped-investigations/{uuid}', params=kwargs)

    def approve_scoped_investigation(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/scoped-investigations/{uuid}/approve', params=kwargs)

    def revoke_scoped_investigation(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/scoped-investigations/{uuid}/revoke', params=kwargs)


class Search:
    '''Class Search
    Description: Manage Search endpoints.
    '''

    def get_search_terms(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v1/search/terms', params=kwargs)


class SequenceDetection:
    '''Class SequenceDetection
    Description: Manage SequenceDetection endpoints.
    '''

    def list_bounded_definition_uuids(self) -> dict:
        return fortidlp_connection.get('/api/v1/sequence-detections/bounded-definitions')

    def get_bounded_entity_count(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/sequence-detections/bounded-definitions/{uuid}/entity-count')

    def list_definitions(self) -> dict:
        return fortidlp_connection.get('/api/v1/sequence-detections/definitions')

    def create_definition(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/sequence-detections/definitions', params=kwargs)

    def delete_definition(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/sequence-detections/definitions/{uuid}')

    def get_definition(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/sequence-detections/definitions/{uuid}')

    def update_definition(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/sequence-detections/definitions/{uuid}', params=kwargs)

    def publish_definition(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/sequence-detections/definitions/{uuid}/publish', params=kwargs)


class Siem:
    '''Class Siem
    Description: Manage Siem endpoints.
    '''

    def list_streams(self) -> dict:
        return fortidlp_connection.get('/api/v1/siem')

    def create_stream(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/siem', params=kwargs)

    def stream_health(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/siem/health/{uuid}')

    def delete_stream(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/siem/{uuid}')

    def get_stream(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/siem/{uuid}')

    def update_stream(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/siem/{uuid}', params=kwargs)


class Slack:
    '''Class Slack
    Description: Manage Slack endpoints.
    '''

    def delete_slack_auth(self) -> dict:
        return fortidlp_connection.delete('/api/v1/slack/auth')

    def slack_auth(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/slack/auth', params=kwargs)

    def slack_health(self) -> dict:
        return fortidlp_connection.get('/api/v1/slack/health')

    def slack_o_auth_url(self) -> dict:
        return fortidlp_connection.get('/api/v1/slack/oauth-url')


class StackFederation:
    '''Class StackFederation
    Description: Manage StackFederation endpoints.
    '''

    def create_enrollment_token(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/federation/enroll', params=kwargs)

    def get_agent_routing_rules(self) -> dict:
        return fortidlp_connection.get('/api/v1/federation/routing-rules')

    def set_agent_routing_rules(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/federation/routing-rules', params=kwargs)

    def get_unrouted_agent_default(self) -> dict:
        return fortidlp_connection.get('/api/v1/federation/routing-rules/default')

    def set_unrouted_agent_default(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/federation/routing-rules/default', params=kwargs)

    def export_agent_routing_rules(self, file_format: str = 'bin', download_folder: str = '', **kwargs) -> dict:
        return _download('/api/v1/federation/routing-rules/export', params=kwargs, method='POST', file_format=file_format, download_folder=download_folder)

    def import_agent_routing_rules(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/federation/routing-rules/import', params=kwargs)

    def get_target_stack_by_labels(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/federation/routing-rules/test', params=kwargs)

    def get_agent_routing_rule(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v1/federation/routing-rules/{id}')

    def stack_federation_service_revoke_enroll_token(self, token_id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/federation/token/{token_id}/revoke', params=kwargs)


class SupportingOperators:
    '''Class SupportingOperators
    Description: Manage SupportingOperators endpoints.
    '''

    def list_supporting_operator_grants(self) -> dict:
        return fortidlp_connection.get('/api/v1/supporting-operators/grants')

    def revoke_supporting_operator_grant(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/supporting-operators/grants/{uuid}')

    def get_supporting_operator_grant(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/supporting-operators/grants/{uuid}')

    def list_supporting_operator_requests(self) -> dict:
        return fortidlp_connection.get('/api/v1/supporting-operators/requests')

    def deny_supporting_operator_request(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/supporting-operators/requests/{uuid}')

    def get_supporting_operator_request(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/supporting-operators/requests/{uuid}')

    def approve_supporting_operator_request(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v1/supporting-operators/requests/{uuid}/approve', params=kwargs)

    def create_support_access(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/supporting-operators/support-access', params=kwargs)


class TenantPreferences:
    '''Class TenantPreferences
    Description: Manage TenantPreferences endpoints.
    '''

    def list_tenant_preferences(self) -> dict:
        return fortidlp_connection.get('/api/v1/tenant-preferences')

    def set_tenant_preference(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/tenant-preferences', params=kwargs)

    def delete_tenant_preference(self, key) -> dict:
        return fortidlp_connection.delete(f'/api/v1/tenant-preferences/{key}')

    def get_tenant_preference(self, key) -> dict:
        return fortidlp_connection.get(f'/api/v1/tenant-preferences/{key}')


class Tenants:
    '''Class Tenants
    Description: Manage Tenants endpoints.
    '''

    def get_tenant_forticloud_attributes(self) -> dict:
        return fortidlp_connection.get('/api/v1/tenants/forticloud')


class TimelineSearch:
    '''Class TimelineSearch
    Description: Manage TimelineSearch endpoints.
    '''

    def post_timeline_action_events_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/action_events', params=kwargs)

    def post_timeline_action_events_aggregation_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/action_events/aggregate', params=kwargs)

    def post_timeline_count_action_events_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/action_events/count', params=kwargs)

    def post_timeline_actions_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/actions', params=kwargs)

    def post_timeline_actions_aggregation_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/actions/aggregate', params=kwargs)

    def post_timeline_count_actions_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/actions/count', params=kwargs)

    def timeline_activity_feed(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v2/timeline/activity', params=kwargs)

    def post_timeline_incidents_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/incident_sensors', params=kwargs)

    def post_timeline_incidents_aggregation_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/incident_sensors/aggregate', params=kwargs)

    def post_timeline_count_incidents_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/incident_sensors/count', params=kwargs)

    def timeline_incident_event_scope(self, id, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/timeline/incident_sensors/{id}/scope', params=kwargs)

    def get_timeline_saved_searches(self, **kwargs) -> dict:
        return fortidlp_connection.get('/api/v2/timeline/savedsearches', params=kwargs)

    def create_timeline_saved_search(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v2/timeline/savedsearches', params=kwargs)

    def delete_timeline_saved_search(self, id) -> dict:
        return fortidlp_connection.delete(f'/api/v2/timeline/savedsearches/{id}')

    def get_timeline_saved_search(self, id) -> dict:
        return fortidlp_connection.get(f'/api/v2/timeline/savedsearches/{id}')

    def update_timeline_saved_search(self, id, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v2/timeline/savedsearches/{id}', params=kwargs)

    def get_timeline_event_streams(self) -> dict:
        return fortidlp_connection.get('/api/v2/timeline/streams')

    def exportable_timeline_fields(self, event_stream) -> dict:
        return fortidlp_connection.get(f'/api/v2/timeline/{event_stream}/export/fields')

    def get_timeline_event_by_id(self, event_stream, id) -> dict:
        return fortidlp_connection.get(f'/api/v2/timeline/{event_stream}/{id}')

    def post_timeline_request(self, query_event_stream, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/timeline/{query_event_stream}', params=kwargs)

    def post_timeline_aggregation_request(self, query_event_stream, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/timeline/{query_event_stream}/aggregate', params=kwargs)

    def post_timeline_count_request(self, query_event_stream, **kwargs) -> dict:
        return fortidlp_connection.send(f'/api/v2/timeline/{query_event_stream}/count', params=kwargs)

    def export_timeline_csv(self, query_event_stream, file_format: str = 'bin', download_folder: str = '', **kwargs) -> dict:
        return _download(f'/api/v2/timeline/{query_event_stream}/export/csv', params=kwargs, method='POST', file_format=file_format, download_folder=download_folder)

    def export_timeline_xlsx(self, query_event_stream, file_format: str = 'bin', download_folder: str = '', **kwargs) -> dict:
        return _download(f'/api/v2/timeline/{query_event_stream}/export/xlsx', params=kwargs, method='POST', file_format=file_format, download_folder=download_folder)


class UsageStatistics:
    '''Class UsageStatistics
    Description: Manage UsageStatistics endpoints.
    '''

    def post_event_count_request(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/usage', params=kwargs)


class Webhooks:
    '''Class Webhooks
    Description: Manage Webhooks endpoints.
    '''

    def get_webhooks(self) -> dict:
        return fortidlp_connection.get('/api/v1/webhooks')

    def create_webhook(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/webhooks', params=kwargs)

    def validate_webhook_custom_payload(self, **kwargs) -> dict:
        return fortidlp_connection.send('/api/v1/webhooks/custom/validate', params=kwargs)

    def delete_webhook(self, uuid) -> dict:
        return fortidlp_connection.delete(f'/api/v1/webhooks/{uuid}')

    def get_webhook(self, uuid) -> dict:
        return fortidlp_connection.get(f'/api/v1/webhooks/{uuid}')

    def update_webhook(self, uuid, **kwargs) -> dict:
        return fortidlp_connection.insert(f'/api/v1/webhooks/{uuid}', params=kwargs)

    def test_webhook(self, uuid) -> dict:
        return fortidlp_connection.send(f'/api/v1/webhooks/{uuid}/test', params={})

debug = False
ssl_verification = True


def ignore_certificate():
    global ssl_verification
    ssl_verification = False
    print('[!] - We strongly advise you to enable SSL validations. Use this at your own risk!')


def enable_debug():
    global debug
    debug = True


def auth(host: str, access_token: str):
    global debug
    global fortidlp_connection

    login = AuthenticationHandler()
    headers, host_result = login.get_headers(
        fdlp_host=host,
        access_token=access_token,
    )

    if headers is None or not isinstance(host_result, str):
        status = False
        data = host_result
    else:
        status = True
        data = 'AUTHENTICATION_SUCCEEDED'
        fortidlp_connection = APIHandler()
        fortidlp_connection.conn(headers, host_result, debug, ssl_verification)
        cur_dir = os.path.dirname(__file__)

    return {
        'status': status,
        'data': data,
    }
