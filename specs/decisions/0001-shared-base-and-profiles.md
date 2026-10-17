# Shared Base and Specialized Profiles

Status: accepted by operator direction.

## Context

Separate component and mobile templates duplicated general working conventions.
Manual synchronization risks drift; full inheritance adds unnecessary machinery.

## Decision

Maintain one repository containing a shared base and component/mobile profiles.
Compose files when generating a new repository, with explicit instruction merging
and collision rejection. Record template version and source digest without paths.

## Consequences

Shared conventions change once, platform-specific content remains independent, and
existing generated projects remain autonomous. Updates to those projects are
deliberate; this tool does not retrofit them automatically.
