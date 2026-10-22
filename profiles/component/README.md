# Cortext Component Template

Canonical scaffold for Cortext ecosystem repos such as `kinflow`, `foreman`, and other interoperable agent components.

Use this template when creating a new component repo. The standard is defined in [specs/repo-standard.md](specs/repo-standard.md), and agent-facing rules live in [AGENTS.md](AGENTS.md).

## Project context and guidance

TODO: Explain the project's purpose, users, scope, current state and main dependencies.
Add usage, setup and development entry points as they become available. Follow
`AGENTS.md` for agent expectations and begin design work at `specs/HLD.md`.

## Layout

```txt
specs/       human-readable normative design and compatibility promises
contracts/   machine-readable public agreements
docs/        explanatory, operational, and developer guidance
src/         implementation
tests/       executable expectations
examples/    working demonstrations
scripts/     repo-local automation
```

## Quick Start

1. This repository was generated from the Cortext component profile.
2. Review its rendered project names and configuration.
3. Start design in `specs/HLD.md`; expand supporting specifications as needed.
4. Add contract tests for any cross-repo promises.
