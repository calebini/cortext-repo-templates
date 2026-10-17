# Cortext Component Template

Canonical scaffold for Cortext ecosystem repos such as `kinflow`, `foreman`, and other interoperable agent components.

Use this template when creating a new component repo. The standard is defined in [specs/repo-standard.md](specs/repo-standard.md), and agent-facing rules live in [AGENTS.md](AGENTS.md).

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
3. Fill in `specs/overview.md`, `specs/architecture.md`, and `specs/interfaces.md` before implementation expands.
4. Add contract tests for any cross-repo promises.
