# High-Level Design

## Purpose, scope and non-goals

TODO: Define the problem, users, ownership, intended outcomes and explicit non-goals.

## System context

TODO: Identify callers, external systems, dependencies and trust boundaries.

## Architecture and state ownership

TODO: Define the main components, dependency direction and authoritative, derived,
cached and transient state. Keep domain logic independent of external adapters.

## Major flows and lifecycle

TODO: Describe primary interactions, state transitions, startup, failures and terminal
behavior. Link detailed lifecycle and interface specifications where needed.

## Constraints and guarantees

TODO: Define invariants, security, configuration, compatibility and migration promises.
Link machine-readable agreements in `../contracts/` and their executable expectations.

## Supporting specifications and decisions

Keep detailed promises in one authoritative place. The following starter documents
can be expanded when needed; summarize and link them here without duplicating content.

Mobile design must cover supported OS/device targets, launch and restoration,
background suspension and retry, offline synchronization, permissions, authentication,
secure storage, data collection and retention, accessibility, localization and release
qualification. Keep the required mobile specifications below current.

- [Overview](overview.md): users, ownership, supported targets and non-goals.
- [Architecture](architecture.md): UI, domain, adapter and state boundaries.
- [Interfaces](interfaces.md): APIs, deep links, notifications and exported data.
- [Lifecycle](lifecycle.md): background, restoration, offline and terminal behavior.
- [Security and privacy](security-privacy.md): identity, permissions, storage and retention.
- [Testing](testing.md): device matrix and qualification evidence.
- [Release](release.md): signing, rollout, rollback and stores.
- [Accessibility and localization](accessibility-localization.md): assistive behavior and locales.
- [Compatibility](compatibility.md): services, OS support and data migrations.
- [Decisions](decisions/): accepted design choices and rationale.
- [Repository standard](repo-standard.md): engineering expectations and release gates.
