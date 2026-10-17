# Cortext Repository Templates

A shared base for Cortext working conventions, composed with component or mobile
starter files. Generated repositories receive an independent snapshot; this tool
never updates an existing project automatically.

## Generate a repository

Requires Python 3.11 or newer; no dependencies or network access are needed.

```sh
python3 scripts/scaffold.py component my-service ../my-service --display-name "My Service"
python3 scripts/scaffold.py mobile my-app ../my-app --platform ios-swift --display-name "My App"
python3 scripts/scaffold.py mobile my-app ../my-app --platform android-kotlin
python3 scripts/scaffold.py mobile my-app ../my-app --platform cross-platform
```

The destination must be absent or empty. Mobile profiles provide platform guidance
and directories; generate Xcode, Gradle or framework projects using native tooling.

## Ownership

- `base/` owns common agent guidance, work tracking, backlog and implementation-plan
  starters. Update shared conventions here once.
- `profiles/component/` owns the Python component layout, tools and specifications.
- `profiles/mobile/` owns mobile lifecycle, privacy, accessibility, release guidance
  and selectable platform profiles.
- `scripts/scaffold.py` composes base files with the selected profile. Base files
  cannot be overridden silently. Agent instructions are composed explicitly.

Work tracking separates future work in the backlog, durable incremental execution
in the implementation plan, durable choices in decision records, and transient
handoff context. See [the shared convention](base/docs/work-tracking.md).

Each generated repo records version, profile, platform and source-content digest
in `.cortext-template.json`. It contains no source installation paths or host data.
Existing repositories adopt later template changes deliberately.

## Verify

```sh
python3 -m unittest discover -s tests -v
```

The suite generates all four variants and checks composition, portable provenance,
substitutions, profile boundaries and refusal to overwrite existing work.

## Template development

Use [the backlog](docs/backlog.md) for future template work and [the implementation
plan](docs/implementation-plan.md) for selected delivery. The initial profiles
preserve the earlier Cortext component and mobile starter content. Those original
folders are retained as historical sources; this repository is the unified source
for future changes.
