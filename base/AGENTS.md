# Shared Cortext Working Conventions

- `docs/backlog.md` holds future ideas and pipeline work.
- `docs/implementation-plan.md` owns selected work, delivery sequence, progress,
  blockers, next steps and completion evidence. Maintain it durably as work advances.
- `specs/decisions/` holds meaningful choices, alternatives, rationale, status and
  consequences. Link decisions from the plan rather than duplicating them.
- Handoff notes are transient. Prefer updating the plan's current state. Link an
  optional companion when needed, preserve lasting decisions and evidence in their
  durable homes, then retire the handoff as work advances.
- Avoid competing status copies. Specs and contracts retain behavioral authority;
  plans and notes do not change it. Required audit evidence is retained separately.

See `docs/work-tracking.md` for the shared convention and `specs/repo-standard.md`
for the selected profile's engineering standard.
