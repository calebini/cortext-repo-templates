# Go Engineering Instructions

- Follow `specs/repo-standard.md` for Go engineering expectations and
  `docs/development.md` for setup and required checks. Start design at `specs/HLD.md`.
- Format changed Go code; run module consistency, vet, tests, build and vulnerability
  checks before completion. Exercise concurrent behavior with the race detector on
  a supported runner; record any unavailable checks in the implementation plan.
- Handle errors explicitly, preserve useful causes, and use `errors.Is`/`errors.As`
  when inspecting wrapped errors. Do not use panic for ordinary failures.
- Pass contexts explicitly where cancellation is needed, propagate cancellation,
  and call returned cancel functions. Cancellation does not wait for work to finish.
- Give goroutines an owner, an exit condition and an observable completion path.
  Make shared-state synchronization and channel-closing ownership explicit.
- Keep packages small. Add interfaces and directories for actual boundaries;
  avoid speculative abstractions and mandatory Python-style layouts.
- Use the operator's configured Git identity; keep personal configuration out of
  reusable repository content.
