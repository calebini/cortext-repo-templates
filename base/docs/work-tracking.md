# Cortext Project Workflow

## README and agent instructions

`README.md` gives the project overview, purpose, context, usage and development
entry points. Link the HLD, agent instructions, implementation plan and roadmap.
`AGENTS.md` directs agents: repository ground rules, required checks, engineering
expectations and the documents to maintain as work advances.

## High-level design

`specs/HLD.md` is the authoritative design entry point. Describe scope and non-goals,
system context, architecture, dependency direction, major flows, constraints and
key guarantees. Link supporting specifications, contracts and accepted decisions.

Small projects may keep their design in the HLD. Extract detailed specifications
when needed, leaving a summary and link in the HLD rather than duplicate promises.
Profile-specific required specifications and qualification gates still apply.
Update the HLD and affected supporting specs when accepted design changes.

## Roadmap

`docs/roadmap.md` holds future ideas, intended outcomes and tentative priorities.
Distinguish exploratory ideas from intended direction; neither is a delivery promise.
Once work is selected, link its implementation plan instead of maintaining a second
execution status. Selection alone does not grant authority to implement or publish.

## Implementation plan

`docs/implementation-plan.md` is the durable record of current implementation work:
concrete steps, sequence, acceptance criteria, progress, blockers, next steps and
completion evidence. Link the relevant design and roadmap items. Retain useful
completion history as the project advances. Feature-specific leaves are allowed
when the main plan links them and identifies which document owns current execution.

## Handoffs

Handoffs are optional, transient continuation context. Keep current continuation
notes in the implementation plan, or link a separate handoff from it while active.
Record the current state, relevant evidence, outstanding issues and next actions.
Replace or retire handoffs as work advances, preserving lasting decisions and evidence
in durable records first. Required audit evidence has separate retention rules.

## Decision records and authority

`specs/decisions/` records meaningful forks: context, alternatives, chosen direction,
rationale, status and consequences. Routine progress belongs in the plan. Link
relevant decisions from the HLD or plan and update affected normative specifications.

README provides orientation; specifications and contracts define behavior. Plans,
roadmaps and handoffs record delivery context and do not override those authorities.
Keep a single owner for current execution status.
