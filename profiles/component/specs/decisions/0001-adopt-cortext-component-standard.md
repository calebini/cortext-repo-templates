# 0001: Adopt Cortext Component Standard

## Status

Accepted

## Context

Cortext components need a shared repo shape so humans and agents can navigate design intent, implementation, interoperability contracts, and operational guidance consistently.

## Decision

This repo follows the Cortext component standard:

- `specs/` for normative human-readable design.
- `contracts/` for machine-readable public agreements.
- `docs/` for explanatory and operational guidance.
- `src/<package>/protocols/` for importable public interfaces.
- `tests/contract/` for interoperability expectations.

## Consequences

Public behavior changes should update specs, contracts, and contract tests together.
