# {{Component Name}}

TODO: Describe the project's purpose, users, scope, current state and dependencies.
This is a minimal Go command starter; replace its greeting with useful behavior,
or replace the command with a library package if that is the project's purpose.

## Quick start

Install the exact supported Go release in `.go-version`. From the generated repo,
initialize one module using the actual repository import path (replace the example):

```sh
go mod init github.com/your-org/{{component_slug}}
go mod tidy
go run .
```

Commit `go.mod` and any generated `go.sum` before enabling CI. Generation is offline
and deliberately leaves module initialization to native Go tooling. See
[development](docs/development.md) for checks, dependencies and toolchain policy.

## Design and layout

Start at [the HLD](specs/HLD.md) and follow [the Go standard](specs/repo-standard.md).
Implementation starts in root-level Go files with adjacent `_test.go` files.
Add `internal/`, `cmd/`, supporting specs, contracts and examples only as needed.
No framework, persistence layer, service runtime or hosting provider is selected.
