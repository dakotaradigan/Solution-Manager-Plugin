# Interview Notes: Portfolio Manager C — Director of Portfolio Management

**Date:** 2026-02-19
**Interviewer:** Dakota Radigan
**Duration:** 40 min
**Format:** Video call

## Context
Oversees all direct indexing strategies. Responsible for model portfolios, transition quality, and investment outcomes. Reports to CIO. 15 years in investment management.

## Raw Notes

- Primary concern is tracking error post-transition: "If a client transitions in and their portfolio tracks 200bps away from the benchmark for the first quarter, that's a relationship problem regardless of the tax savings"
- Wants transition scenarios to explicitly show the tracking error vs. tax tradeoff: "Every transition is a negotiation between tax efficiency and investment fidelity. I need to see that curve, not just one point on it."
- Currently reviews transition proposals by opening Raj's Excel file, scanning the summary tab, and checking a few formulas: "Honestly, I'm spot-checking. I don't have time to audit every lot."
- Frustrated that in-kind transfer analysis doesn't account for the model's factor exposures: "Keeping a position because it saves taxes is fine, but if it blows up your sector exposure or introduces unintended factor tilts, that's a problem"
- Wants the ability to run multi-asset transitions: "We're getting more UMA mandates where the client has equities, fixed income, and alternatives. Right now we model each sleeve separately and hope the aggregate makes sense."
- "The wash sale thing keeps me up at night. If we trigger a wash sale across a household because the transition analyst didn't check the IRA, that's a compliance issue, not just a tax issue."
- Would like to see historical transition outcomes: "We've done hundreds of transitions. I have no data on how they actually performed — what was the realized tracking error vs. projected? Did the tax savings materialize?"
- Concerned about the firm's ability to scale: "We're winning more direct indexing mandates but our transition capacity is fixed. Raj can only do so many per month."
- Mentioned that competitor firms are offering "transition-as-a-service" with same-day preliminary analysis
- Wants automated pre-trade compliance checks built into the transition workflow: "Right now compliance reviews the proposal after it's built. If there's a restriction violation, we have to rework the whole thing."

## Key Quotes
> "Tax savings mean nothing if the portfolio doesn't track. I need both numbers, together, on a curve I can evaluate."

> "We're making investment decisions in Excel and hope-checking the results. That's not a process, that's a prayer."

> "Every transition we do is a one-off. We've never systematized it because every client is different. But the 80% that's the same — data ingestion, security mapping, basic tax calc — that should be automated."

## Observed Pain Points
1. No visibility into tracking error vs. tax tradeoff as a curve
2. Can't model multi-asset transitions (equities + fixed income + alternatives together)
3. In-kind transfer analysis ignores factor exposures
4. No historical data on transition outcomes (projected vs. actual)
5. Wash sale risk across household accounts
6. Compliance review happens after modeling, not during — causes rework
7. Capacity constrained by manual process — can't scale with demand
8. No pre-trade compliance integration in transition workflow
