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

- [Overview](overview.md): ownership, users and non-goals.
- [Architecture](architecture.md): detailed boundaries and dependency direction.
- [Interfaces](interfaces.md): public APIs and importable protocols.
- [Lifecycle](lifecycle.md): state transitions and failure behavior.
- [Invariants](invariants.md): rules that must remain true.
- [Configuration](config.md): sources, defaults and precedence.
- [Compatibility](compatibility.md): versioning and migration guarantees.
- [Decisions](decisions/): accepted design choices and rationale.
- [Repository standard](repo-standard.md): engineering expectations.
