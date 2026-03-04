# Interview Notes: Portfolio Manager A — Senior Portfolio Manager, Equity Desk

**Date:** 2026-02-15
**Interviewer:** Dakota Radigan
**Duration:** 45 min
**Format:** 1:1 video call

## Context
Participant manages a $2B equity portfolio. 12 years at the firm. Power user of the current market data platform.

## Raw Notes

- Spends first 90 minutes of every day manually pulling data from 4 different systems to build his morning briefing
- "I need real-time corporate actions data but what I get is delayed by at least 6 hours. By the time I see a dividend announcement, the market has already priced it in."
- Uses Bloomberg terminal for real-time quotes but firm's internal system for position data — has to mentally reconcile the two
- Built his own Excel macros to merge data from internal and external sources. "If my spreadsheet breaks, my whole workflow breaks."
- Wants a single view that shows positions + live market data + corporate actions in one place
- Frustrated that reference data (security master) is inconsistent across systems: "I've seen the same bond show up with three different ISINs depending on which system I query"
- "The API exists but the documentation is terrible. I tried to build something myself and gave up after two weeks."
- Would love alerting on corporate actions relevant to his holdings — not a firehose of all events
- Mentioned that junior analysts waste 2-3 hours/day on data reconciliation tasks he considers "solved problems"
- Compliance team sometimes flags trades because their reference data doesn't match his — "it's the same security, just different identifiers"
- Wants historical corporate actions data for backtesting strategies

## Key Quotes
> "I'm paying for Bloomberg, Reuters, and our internal system. Why can't I get one clean answer to 'what's the price of X?'"

> "My biggest fear is making a trade based on stale data. It's happened before."

> "The junior analysts are doing data janitorial work instead of analysis. That's a waste of talent and money."

## Observed Pain Points
1. Data fragmentation across systems
2. Stale/delayed corporate actions
3. Reference data inconsistency (identifier mismatch)
4. Manual reconciliation burden
5. Poor API documentation blocking self-service
6. No personalized alerting
