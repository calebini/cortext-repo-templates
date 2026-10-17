# Cortext Component Repo Standard

This document defines the standard repo shape for Cortext ecosystem components.

## Intent

Cortext components should be independently understandable, testable, and releasable while remaining easy to compose into the larger `cortext1` agent system.

## Classification

- `README.md` is orientation.
- `specs/` is promises.
- `contracts/` is enforceable promises.
- `docs/` is help.
- `examples/` is working demonstrations.
- `tests/` is executable expectations.
- `notes/` is optional scratch thinking and should not define durable behavior.

## Required Spec Files

- `specs/overview.md`: what this component owns, who uses it, and explicit non-goals.
- `specs/architecture.md`: internal boundaries, dependency direction, lifecycle, and major components.
- `specs/interfaces.md`: public APIs, protocols, service boundaries, and imported/exported contracts.
- `specs/lifecycle.md`: state transitions, startup/shutdown behavior, and terminal states where relevant.
- `specs/invariants.md`: rules that must remain true across implementations.
- `specs/config.md`: configuration surface, defaults, environment variables, and precedence.
- `specs/compatibility.md`: cross-repo compatibility expectations, versioning, and migration rules.

## Required Implementation Shape

```txt
src/<package>/
  core/        pure domain logic
  protocols/  public interfaces, typed contracts, event types
  adapters/   integrations with external systems
  services/   orchestration around core and adapters
  models/     domain objects, DTOs, persistence models
  config.py
  errors.py
  logging.py
  cli.py
```

## Dependency Rules

- `core/` may depend on `models/`, package-local errors, and standard-library utilities.
- `core/` must not depend on `adapters/`.
- `protocols/` should stay stable and small because other repos may import it.
- `services/` composes `core/`, `protocols/`, and `adapters/`.
- `adapters/` owns framework, network, filesystem, database, and vendor coupling.

## Git Identity

Use the operator's configured Git identity. Contributor names, email addresses and
machine-local configuration are not part of the reusable repository standard.

## Interoperability

When another Cortext repo depends on this component, expose the promise in one of two places:

- Use `src/<package>/protocols/` for importable typed interfaces.
- Use `contracts/` for machine-readable schemas, events, API definitions, or compatibility fixtures.

Any compatibility change should update:

- `specs/compatibility.md`
- the relevant file in `contracts/`
- `tests/contract/`
- `CHANGELOG.md`

## Documentation Split

Shared work tracking follows [docs/work-tracking.md](../docs/work-tracking.md).

Use `specs/` for normative design. Use `docs/` for how-to material.

Examples:

- Event meaning and ordering guarantees: `specs/interfaces.md` or `specs/lifecycle.md`
- Exact event schema: `contracts/events/*.json`
- How to consume the event: `docs/examples.md`
- Deployment and observability: `docs/operations.md`
