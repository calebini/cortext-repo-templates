# Go Repository Standard

## Scope and authority

Use `specs/HLD.md` as the authoritative design entry point. Shared artifact roles,
execution tracking and transient handoffs follow
[the common workflow](../docs/work-tracking.md). This profile adds Go conventions;
it does not prescribe a network service or a particular application architecture.

## Modules and toolchains

Start with one module initialized with `go mod init` and the real import path.
Commit `go.mod` and `go.sum` when generated; an application using only the standard
library may have no `go.sum`. Add or update dependencies deliberately with
`go get <module>@<version>` and reconcile them with `go mod tidy`.
Do not add vendoring, multiple modules or `go.work` without a concrete need.

The `go` directive records the module's minimum Go version. `.go-version` selects
the exact supported patch release used by development, CI and deployment builds.
Review and update that pin deliberately, including security patches. Keep the pin
at least as new as the module minimum and all dependency requirements. Add a
`toolchain` directive only if a preferred development toolchain differs from the
minimum; it is a suggestion, not an exact build pin. CI uses `GOTOOLCHAIN=local`
with the explicitly installed release to prevent automatic toolchain switching.

## Packages and executable expectations

Root-level implementation is sufficient initially. Put tests beside code in
`*_test.go` files, and reusable fixtures in `testdata/` when needed. Use `internal/`
for private implementation packages and `cmd/<name>/` when multiple executables,
mixed library/command code or server navigation justify it. No `src/`, `pkg/` or
layer hierarchy is mandatory. Define small interfaces at real consumer boundaries.
Keep domain logic independent of external integrations without requiring directories
named `core` or `adapters`.

Public wire agreements belong in `contracts/`; their meaning belongs in specs.
Compatibility changes must update affected specs, contracts and executable contract
tests together. Go contract tests may live beside the relevant package; a top-level
`tests/contract/` directory is not required.

## Quality and concurrency

Use gofmt, module consistency checks, go vet, behavior tests, builds and govulncheck
as documented in [development](../docs/development.md). Use race detection on a
supported runner and write meaningful concurrent tests when concurrency is present.
Do not add tests solely to mirror a trivial generated greeting.

Handle errors and preserve causes when wrapping. Propagate contexts through
cancellable operations and release cancellation resources. Own every goroutine's
lifetime and completion; document synchronization and channel closure ownership.
Prefer simple concurrency over abstractions with unclear lifetimes.

## Conditional service requirements

Only projects implementing long-running network services need service lifecycle
specs: validated startup configuration and secret handling, request and outbound
deadlines, bounded queues and overflow behavior, connection/resource limits,
health/readiness semantics, structured logging with redaction, and bounded graceful
shutdown. Define their values and guarantees in that project's HLD or supporting
specs; explain execution in operations docs. `net/http` and `log/slog` are reasonable
starting points. HTTP shutdown does not close or wait for WebSocket connections;
services using them must own connection shutdown separately.

Containers and provider configuration are optional. If needed, use a multistage
build, non-root runtime, required CA trust and exec-form startup. Disable cgo only
after verifying dependency and runtime support. Hosting choices, persistence,
distributed state and application-specific coordination are project decisions.

## Official references

- [Module layout](https://go.dev/doc/modules/layout)
- [Dependency management](https://go.dev/doc/modules/managing-dependencies)
- [Toolchain selection](https://go.dev/doc/toolchain)
- [Supported release policy](https://go.dev/doc/devel/release)
- [Code review guidance](https://go.dev/wiki/CodeReviewComments)
- [Context cancellation](https://pkg.go.dev/context)
- [HTTP shutdown](https://pkg.go.dev/net/http#Server.Shutdown)
