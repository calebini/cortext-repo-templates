# Shared Cortext Working Conventions

- Read `README.md` for project context, usage and navigation, then follow `AGENTS.md`
  for agent ground rules and the selected profile's engineering expectations.
- Start design work at `specs/HLD.md`. Keep it current as the authoritative high-level
  design and link supporting specifications and contracts without duplicating them.
- `docs/roadmap.md` holds future ideas, intended outcomes and tentative priorities.
  Link selected work to the implementation plan; maintain execution status there.
- `docs/implementation-plan.md` owns current implementation steps, acceptance criteria,
  progress, blockers, next steps and completion evidence. Maintain it as work advances.
- `specs/decisions/` holds meaningful choices, alternatives, rationale, status and
  consequences. Link decisions from the HLD or plan where relevant.
- Handoff notes are transient. Keep continuation context in the implementation plan
  or link a separate companion from it while active. Preserve lasting decisions and
  evidence in their durable homes before retiring the handoff.
- Avoid competing status copies. Specs and contracts retain behavioral authority;
  plans, roadmaps and handoffs do not change it. Retain required audit evidence separately.

See `docs/work-tracking.md` for artifact responsibilities and
`specs/repo-standard.md` for the selected profile's engineering standard.
