# Implementation Plan

## Current State

Go profile 0.3.0 is the current delivery, authorized for implementation, commit and
push on 2026-10-25. See [the decision](../specs/decisions/0003-minimal-go-profile.md).
Earlier delivery history and evidence remain below.

## Go profile delivery

1. Add a small Go profile composed with the unchanged shared base. Preserve the
   Python/mobile outputs, explicit collision handling and portable provenance.
2. Leave module initialization to native Go tooling; supply minimal command source,
   Go-specific engineering guidance, toolchain policy and generated Go CI checks.
3. Extend generator validation and tests for Go output, language option boundaries,
   shared workflow, provenance and native initialization/build/check execution.
4. Update README, HLD, version and decision record. Keep service/application
   requirements conditional; do not create framework, container or hosting starters.
5. Review changes, run local checks, commit only this delivery and push to origin.

Acceptance: all five variants generate without unresolved tokens or broken local
workflow links; shared base bytes remain unchanged; Go output contains no Python
or mobile artifacts; rejected options write no destination; initialized Go output
passes formatting, tidy, vet, tests, race and build checks. Existing generated
projects and pre-existing untracked `whetstone_runs/` remain untouched.

Progress: implementation and local acceptance verification complete. No blockers or
separate handoff. Commit and push are authorized as the final publication steps;
remote CI evidence remains separate from local acceptance evidence.

Verification on 2026-10-25: all eight unittest checks passed with Go 1.27.3 installed
in temporary storage. Native smoke checks exercised module initialization, gofmt,
tidy consistency, vet, tests, race execution, build and running generated output.
The pinned govulncheck v1.9.0 scan of an initialized generated starter reported
no vulnerabilities. Both workflow YAML files parsed successfully, all generated Go
Markdown links resolved, and `git diff --check` passed. Shared base and existing
Python/mobile profile contents are unchanged. Official toolchain archive checksum
was verified before execution. No tests or tools were installed into a project.

## Earlier workflow delivery state

Workflow 0.2.0 implemented: both profiles use `specs/HLD.md` as the design entry
point and `docs/roadmap.md` for future ideas. Shared conventions define README context,
agent rules, concrete implementation steps and optional linked handoffs. Required
mobile specifications, safety rules and release qualification remain intact.

The earlier quoted-display-name repair was committed as `1276817`.

Initial delivery complete: shared work-tracking base, component/mobile profile
composition, portable version provenance and generated-output verification. The
public repository is https://github.com/calebini/cortext-repo-templates.

## Earlier workflow delivery

1. Rename the shared future-work starter to roadmap and update generator navigation.
2. Add profile HLDs, clarify supporting spec ownership and preserve mobile requirements.
3. Update generated-output verification and check links and missing required documents.
4. Document deliberate adoption for existing projects; leave existing repositories unchanged.

## Earlier workflow continuation and handoffs

No separate handoff. Implementation and local verification complete. The operator
authorized commit and push on 2026-10-23. Existing generated projects have not been
migrated. Pre-existing local audit artifacts are outside this workflow update.
See [the HLD](../specs/HLD.md) and
[workflow decision](../specs/decisions/0002-hld-and-roadmap-workflow.md).

## Delivery Sequence

1. Preserved existing profile content and extracted shared conventions into `base/`.
2. Implemented one dependency-free generator; all four generated variants pass local
   tests, including mobile structural verification and non-overwrite behavior.
3. Inspected staged content; removed personal Git identity defaults. No local paths,
   credentials or machine-specific settings were published.
4. Published initial checkpoint `7c84dc1` under operator authorization. CI verifies
   generation across Linux, macOS and Windows using Python 3.11 and 3.13.

## Verification

Workflow 0.2.0: `python3 -B -m unittest discover -s tests -v` passed all five tests
across the component and three mobile variants. Checks cover generated workflow
links, shared roadmap composition, and verifier rejection when the HLD, tracking
files or required mobile safety/qualification specs are missing. `git diff --check`
passed. These are scaffolding checks, not mobile application release evidence.

### Initial delivery evidence

`python3 -m unittest discover -s tests -v`: four tests passed, covering all four
profile variants. Staged diff hygiene passed. Remote CI results are separate from
this local evidence. The local scaffold skill now routes future work to this repo.

## Decisions

Use simple file composition rather than template inheritance. Generated repositories
receive snapshots and adopt future changes deliberately. See
`specs/decisions/0001-shared-base-and-profiles.md`.
