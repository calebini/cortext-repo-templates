# Cortext Component Repo Standard

This repository follows the Cortext component scaffold.

## Required Layout

- `specs/` contains normative human-readable design and compatibility promises.
- `contracts/` contains machine-readable public agreements.
- `docs/` contains explanatory, operational, and developer-facing guidance.
- `src/` contains implementation.
- `tests/contract/` validates public contracts and interoperability assumptions.
- `examples/` contains working usage examples.
- `scripts/` contains repo-local automation.

## Rules

- Put stable design intent in `specs/`, not `docs/`.
- Put schemas, event definitions, OpenAPI files, and compatibility contracts in `contracts/`.
- Put tutorials, setup, operations, and troubleshooting in `docs/`.
- Public importable interfaces should live in `src/<package>/protocols/`.
- Core domain logic must not depend on adapters.
- Adapters may depend on protocols and core logic, but core logic must remain framework- and vendor-light.
- Cross-repo compatibility changes require updates to `specs/compatibility.md`, relevant `contracts/`, and contract tests.
- Prefer small, explicit modules over broad framework abstractions.

## Git Identity

Use the operator's configured Git identity. Do not embed contributor-specific
names, email addresses or local configuration in reusable templates.

## Standard Reference

The normative repo standard is [specs/repo-standard.md](specs/repo-standard.md).
