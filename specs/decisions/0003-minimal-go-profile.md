# Minimal Go Profile

Status: accepted by operator direction, 2026-10-25.

## Context

A Go backend needs the common Cortext workflow, but the existing component profile
generates Python packaging, Python interfaces and a Python source hierarchy.
Language differences do not justify another repository containing shared policy.

## Decision

Add a small sibling `profiles/go/` composed with the unchanged shared base by the
existing generator. Keep root-level command source, Go engineering guidance,
toolchain selection and quality checks in this profile. Leave module initialization
to `go mod init` with the actual repository import path, without generator network
access or language-tooling dependencies. Generated CI requires that initialization.

Use adjacent Go tests; grow `internal/`, `cmd/`, detailed specs and contracts only
when justified. Keep common tracking and authority rules in `base/`; preserve
explicit AGENTS composition, collision rejection and snapshot provenance.

## Alternatives and consequences

A separate Go template repository would duplicate workflow maintenance. Overlaying
the Python profile would require deleting or replacing Python artifacts. A general
multi-axis profile framework would add machinery beyond the current need. The
sibling profile keeps existing profile behavior and names compatible.

Go guidance covers modules, checks, errors, contexts and goroutine ownership.
Long-running service guidance is explicitly conditional; concrete queue limits,
health semantics, shutdown guarantees and deployment settings belong to each
service. Phaselock room coordination, WebRTC signaling, managed TURN credentials,
restart/rejoin behavior and Render configuration are not template requirements.

Generated projects install the exact supported patch in `.go-version`; their
`go.mod` records the minimum. Toolchain and vulnerability-tool pins are reviewed
updates, not floating CI dependencies. Existing projects adopt changes deliberately;
this profile addition does not migrate them or rewrite their provenance.
