# Go Development

## Initialization and versions

Install the exact Go release in `.go-version`, then initialize the module using
the actual repository import path as shown in the README. Commit `go.mod` and any
generated `go.sum`. The starter has no third-party runtime dependencies.
CI intentionally fails until module initialization is complete.

Check `go version` and `go env GOTOOLCHAIN` when diagnosing version differences.
See [the standard](../specs/repo-standard.md) for version and dependency policy.

## Commands

Run from the repository root after initialization:

```sh
# Format and reconcile dependencies during development
gofmt -w .
go mod tidy

# Read-only consistency and quality checks (POSIX shell)
test -z "$(gofmt -l .)"
go mod tidy -diff
go vet ./...
go test ./...
go build ./...

# Concurrent execution checks on a supported runner
go test -race ./...

# Current root command; adjust if the entry point moves to cmd/<name>/
go run .
go build -trimpath -o bin/{{component_slug}} .
```

Install `golang.org/x/vuln/cmd/govulncheck` at the reviewed version pinned in
[CI](../.github/workflows/go.yml), then run `govulncheck ./...`. Keep that version
explicit during upgrades rather than installing `@latest` on every CI run.
The vulnerability database remains current; an unchanged dependency graph can
acquire new findings that need investigation and remediation.

CI runs on Linux with cgo enabled and a C compiler for race detection. Do not apply
a production `CGO_ENABLED=0` setting to the race job. Race detection only observes
executed paths; it does not prove that untested concurrency is safe.

Use standard-library behavior tests and add fixtures or integration checks when
they verify real promises. Extra analyzers, fuzzing, benchmarks, coverage thresholds,
task runners and container/deployment files are optional additions justified by
project needs. The greeting starter is not a behavior test suite.

## Official tooling references

- [gofmt](https://pkg.go.dev/cmd/gofmt)
- [Go commands, including tidy -diff and vet](https://pkg.go.dev/cmd/go)
- [Race detector and platform requirements](https://go.dev/doc/articles/race_detector)
- [Vulnerability checks](https://go.dev/doc/security/)
