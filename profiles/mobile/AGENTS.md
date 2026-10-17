# Cortext Mobile App Repo Standard

This repository follows the Cortext mobile application scaffold.

## Rules

- Treat `specs/` as normative and `docs/` as explanatory.
- Put wire formats and interoperability agreements in `contracts/`.
- Keep domain logic independent of UI frameworks and vendor adapters where practical.
- Keep credentials, signing keys, provisioning profiles, and production configuration out of Git.
- Changes to permissions, privacy, background execution, authentication, or retention require specification and test updates.
- Cross-repository compatibility changes require contract tests and migration notes.
- A green unit suite alone is not mobile release qualification.

The normative standard is [specs/repo-standard.md](specs/repo-standard.md).
