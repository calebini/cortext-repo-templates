# Implementation Plan

## Current State

Initial delivery: shared work-tracking base, component/mobile profile composition,
portable version provenance, generated-output verification and GitHub publication.

## Delivery Sequence

1. Preserve existing profile content and extract shared conventions into `base/`.
2. Implement one dependency-free generator and verify all profile variants.
3. Inspect staged contents for private/environment-specific data.
4. Commit and publish the public repository under operator authorization.

## Decisions

Use simple file composition rather than template inheritance. Generated repositories
receive snapshots and adopt future changes deliberately. See
`specs/decisions/0001-shared-base-and-profiles.md`.
