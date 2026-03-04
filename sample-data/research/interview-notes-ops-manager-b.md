# Interview Notes: Ops Manager B — Head of Data Operations

**Date:** 2026-02-17
**Interviewer:** Dakota Radigan
**Duration:** 60 min
**Format:** In-person

## Context
Manages a 15-person operations team responsible for trade settlement, reconciliation, and corporate actions processing. 8 years in current role.

## Raw Notes

- Team processes ~2,000 trades/day across equities, fixed income, and derivatives
- Corporate actions are the #1 source of settlement breaks: "Roughly 40% of our breaks trace back to a corporate action we either missed or processed late"
- Current workflow: receive corporate action notifications via email and vendor feeds, manually key them into the settlement system
- "We have three vendor feeds for corporate actions and they often disagree. Someone has to manually determine which one is correct."
- Identifier mapping is a daily headache — CUSIP, ISIN, SEDOL, internal IDs don't always cross-reference cleanly
- Wants an automated corporate actions processing pipeline: ingest → validate → match to positions → apply
- "We hired two additional people last year just to handle the volume of corporate actions. That's not scalable."
- Reconciliation between front office and back office systems happens at T+1, but issues found at T+1 are expensive to fix
- "If I could get real-time position reconciliation instead of end-of-day, we'd catch 80% of breaks before they become problems"
- Settlement failures cost the firm ~$200K/quarter in penalties and buy-ins
- Wants better audit trail — regulators asking for full lineage on how corporate actions were processed
- "The vendor promised us golden source data but we still end up with conflicts"

## Key Quotes
> "Every corporate action is a potential settlement break waiting to happen."

> "We're throwing people at a data problem. That doesn't scale."

> "I need to know the full story — where did this data come from, who touched it, what changed and when."

## Observed Pain Points
1. Corporate actions as settlement break source
2. Conflicting vendor data requiring manual adjudication
3. Identifier mapping failures across standards
4. Manual corporate actions processing (no automation)
5. T+1 reconciliation too late to prevent breaks
6. Scaling through headcount rather than technology
7. Audit trail gaps for regulatory compliance
