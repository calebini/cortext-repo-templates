# HLD and Roadmap Workflow

Status: accepted by operator direction, 2026-10-22.

## Context

The operator uses README for project context, AGENTS for agent rules, a design
entry point, an implementation plan with optional linked handoffs, and future ideas.
The profiles shared tracking conventions but lacked an HLD and called future work a backlog.

## Decision

Use `specs/HLD.md` as the authoritative high-level design entry point and
`docs/roadmap.md` for future ideas. Keep concrete current work and continuation context
in `docs/implementation-plan.md`, linking any separate active handoff. Keep supporting
specs and machine-readable contracts authoritative for their detailed promises.
Python specifications can grow as needed; all required mobile specs and safety and
qualification rules remain. Version the template workflow change as 0.2.0.

## Alternatives and consequences

Retaining separate overview and architecture documents as the only entry points
would leave the requested design navigation unresolved. Combining every mobile
specification into one HLD would weaken explicit required coverage. An HLD linking
supporting specs provides a single starting point while preserving that coverage.
Existing projects migrate deliberately using the README instructions; no automatic
updates or retroactive provenance changes occur.
