# Changelog

## Unreleased

### Added

- Added SDK coverage for all endpoints present in `api_docs/fortidlp-cloud-20260630.json`.
- Added new endpoint groups for access tokens, agent actions, admin operations, cloud integrations, dashboards, saved queries, scoped investigations, timeline search, webhooks, and other previously missing FortiDLP API areas.
- Added timeline search methods, including generic event stream search, aggregation, count, export, saved searches, streams, and activity feed endpoints.

### Changed

- Expanded existing SDK classes such as `Cases`, `Policies`, `SaaS`, and related entity classes with missing API methods while preserving the existing `fortidlp_connection` request style.
- Used `**kwargs` for complex or variable request bodies to match the existing flexible SDK method pattern.

### Validation

- Confirmed API path coverage against `fortidlp-cloud-20260630.json`: `363/363` paths represented.
- Confirmed `fortidlp/fortidlp.py` passes Python syntax validation with `py_compile`.
