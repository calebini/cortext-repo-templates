# Cortext Work Tracking

## Backlog

`docs/backlog.md` holds future ideas and work in the pipeline, with intent, priority
and selection decisions as needed. Once work is selected, link its implementation
plan instead of maintaining a second execution status. Selection alone does not
grant authority to implement or publish.

## Implementation Plan

`docs/implementation-plan.md` is the durable, incrementally maintained record of
selected work: sequence, acceptance criteria, progress, blockers, next steps and
completion evidence. Retain useful delivery history as the project advances.
Feature-specific leaves are allowed when the main plan links them and identifies
which document owns current execution. Link the backlog and plan from the README.

## Decision Records

`specs/decisions/` records meaningful forks: context, alternatives, chosen direction,
rationale, status and consequences. Routine progress is not a decision record.
The implementation plan links these records; it does not replace them. Update
normative specifications when accepted choices change behavioral promises.

## Handoffs

Handoffs are optional, transient continuation context. Prefer a concise current-state
section in the implementation plan. If a longer companion is necessary, link it
from the plan while active. Replace or retire it as work advances after preserving
lasting decisions and evidence in durable records. Do not create a permanent file
for every intermediate status. Required audit evidence has separate retention rules.

## Authority

README provides orientation; specifications and contracts define behavior. Tracking
documents record delivery and do not override those authorities. Keep a single
owner for current execution status rather than synchronizing duplicate checklists.
