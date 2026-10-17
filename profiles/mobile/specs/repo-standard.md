# Cortext Mobile Application Repository Standard

## Intent

Mobile applications must be independently understandable, testable, and releasable
while interoperating safely with Cortext services. This standard is platform-neutral;
the selected profile defines the native layout and toolchain.

## Authority

- `README.md` is orientation.
- `specs/` contains normative product and engineering promises.
- `contracts/` contains machine-readable public agreements.
- `docs/` contains development and operational help.
- `app/` contains application composition and platform UI.
- `core/` contains framework-light domain behavior where practical.
- `tests/` contains cross-boundary and acceptance expectations.

## Required specifications

Shared work tracking follows [docs/work-tracking.md](../docs/work-tracking.md).

- `overview.md`: ownership, users, supported platforms, and non-goals.
- `architecture.md`: dependency direction, boundaries, and state ownership.
- `interfaces.md`: APIs, deep links, notifications, and exported data.
- `lifecycle.md`: launch, background, restoration, offline, and terminal behavior.
- `security-privacy.md`: identity, storage, permissions, collection, and retention.
- `testing.md`: supported test and device matrix.
- `release.md`: signing, versioning, rollout, rollback, and stores.
- `accessibility-localization.md`: assistive behavior, locales, and content rules.
- `compatibility.md`: service, data, OS, and migration guarantees.

## Dependency rules

- Domain behavior must not depend directly on screens, platform views, or vendor SDKs.
- Network, persistence, analytics, notification, identity, and hardware integrations
  belong behind explicit adapter boundaries.
- Public wire behavior belongs in `contracts/`; generated clients are not authoritative.

## Mobile safety rules

- Keep credentials and signing material outside Git and ordinary app configuration.
- Permission requests must be purpose-bound and documented.
- Sensitive values use platform secure storage.
- Background work must tolerate suspension, duplicate delivery, expiration, and retry.
- Offline writes require an explicit synchronization and conflict policy.
- Deep links and notification payloads are untrusted inputs.
- Telemetry must minimize personal data and document retention and user controls.

## Release gates

A release candidate requires clean builds, unit and contract tests, critical UI tests,
accessibility and privacy checks, upgrade evidence, representative device smoke tests,
controlled signing, and documented rollout and rollback.

Create only the implementation boundaries the app currently needs. Do not add empty
architecture merely to mirror the full standard.
