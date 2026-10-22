# Repository Templates High-Level Design

## Purpose and scope

Compose portable Cortext Python component and mobile repository starters from one
shared workflow base and specialized profiles. Existing repositories adopt changes
deliberately; automatic retrofit and native mobile project generation are out of scope.

## Architecture and flow

`base/` owns common agent guidance and workflow documents. `profiles/component/`
owns Python layout and engineering expectations. `profiles/mobile/` owns mobile
specifications, structural verification and selectable platform guidance.
`scripts/scaffold.py` validates input, composes base with a profile, renders tokens,
records version and source digest, and writes to an absent or empty destination.
Shared files cannot be silently overridden; AGENTS instructions merge explicitly.

## Workflow contract

Generated repositories use README for context, AGENTS for agent rules,
`specs/HLD.md` for design, `docs/implementation-plan.md` for current work and linked
handoffs, and `docs/roadmap.md` for future ideas. Supporting specs refine the HLD
without duplicating promises. Mobile requirements and release gates remain mandatory.
See [the shared convention](../base/docs/work-tracking.md).

## Constraints and validation

Keep output free of host paths, credentials and signing material. Refuse to overwrite
existing work. Preserve profile boundaries and portable provenance. Generator tests
exercise all four variants, workflow links and required mobile document verification.
These checks qualify scaffolding, not mobile releases.

## Decisions

- [Shared base and profiles](decisions/0001-shared-base-and-profiles.md).
- [HLD and roadmap workflow](decisions/0002-hld-and-roadmap-workflow.md).
