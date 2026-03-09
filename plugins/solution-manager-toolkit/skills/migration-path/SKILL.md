---
name: migration-path
description: This skill should be used when defining staged migration plans with rollback options for transitioning from current state to future state.
---

# Migration Path

Domain knowledge for defining safe, staged transitions from current state to future state.

## When to Use

- Planning how to get from current system to new system without breaking anything
- Reviewing a solution that has no migration plan defined
- Any deployment in a regulated domain where data integrity is critical

## Standard Stages

1. **Parallel run** — Old and new side by side. Old is source of truth. Compare outputs for accuracy.
2. **Cutover with safety net** — New is primary, old is backup/verification. Users start using new system.
3. **Full migration** — Old retired. All consumers on new system. Monitoring fully operational.

## Each Stage Needs

- **Entry criteria** — What must be true before entering this stage
- **Rollback procedure** — How to revert if something goes wrong
- **Success criteria** — What must be true to proceed to the next stage
- **Duration** — How long this stage runs before evaluation

## Key Principles

- Never flip a switch. Migrate in stages with rollback at each one.
- In financial services, wrong data for even one day means trades on bad data.
- Rollback procedures must be tested before cutover, not documented after.
- "2-week clean run with no exceptions" is a reasonable success criterion for final stage.
- Flag when a solution has no migration path: "How do you get from current state to future state without breaking anything?"
