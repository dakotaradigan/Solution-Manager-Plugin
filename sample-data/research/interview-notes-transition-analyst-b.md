# Interview Notes: Transition Analyst B — Senior Transition Analyst, Portfolio Operations

**Date:** 2026-02-17
**Interviewer:** Dakota Radigan
**Duration:** 60 min
**Format:** In-person

## Context
Builds transition analysis models for all incoming requests. 6 years in role. Team of 3 analysts handling ~15-20 transitions per month. Sole owner of the Excel-based modeling process.

## Raw Notes

- Receives requests via email, Slack, and sometimes verbal asks from RMs who stop by his desk
- "Every request is different. Some come with a Schwab CSV, some come with a PDF statement, one came as a screenshot from a phone. I spend the first day just getting the data into a usable format."
- Current model is a set of Excel workbooks — the most complex one has 47 tabs and takes 2 minutes to recalculate
- Process for a standard transition: (1) parse holdings, (2) map to internal security master, (3) run against target model, (4) calculate lot-level tax impact, (5) generate scenarios, (6) format PDF proposal — takes 3-5 days for a simple one, 2+ weeks for complex
- Wash sale detection across households is entirely manual: "I export all lots from every account in the household, cross-reference them in a separate sheet, flag anything within the 30-day window. It takes about a day per household."
- Cost basis data from custodians is frequently wrong or missing: "Schwab files are usually clean. Fidelity is hit-or-miss. When cost basis is missing, I have to call the custodian or ask the RM to get it from the client."
- No version control on models: "If I change a scenario and the RM asks for the old one back, I hope I saved a copy. Sometimes I didn't."
- Concentrated position handling is the hardest part: "The client says they won't sell AAPL, but the model has AAPL at 2% and they're holding 15%. Now I have to figure out how to build around that while still hitting the tracking error target."
- "I'm the bottleneck and I know it. If I'm on vacation, transitions don't happen."
- Would love a system that auto-ingests custodian files, maps securities, and gives him a starting point instead of a blank spreadsheet
- Mentioned that the tax calculation logic is "tribal knowledge" — not documented anywhere, lives in his head and his Excel formulas

## Key Quotes
> "Every transition is a snowflake. That's the problem — there's no standard process, just me and Excel."

> "The 47-tab workbook is load-bearing infrastructure. If that file corrupts, we're in serious trouble."

> "I don't need AI to do my job. I need a system that gives me clean data and a starting point so I can focus on the hard judgment calls."

## Observed Pain Points
1. No standardized intake format — every request arrives differently
2. Manual data parsing from multiple custodian formats (CSV, PDF, screenshots)
3. Excel-based modeling with no version control
4. Wash sale detection is manual and takes a full day per household
5. Cost basis data frequently missing or incorrect from custodians
6. Concentrated position modeling requires complex manual workarounds
7. Single point of failure — no one else can run the models
8. Tax calculation logic is undocumented tribal knowledge
9. No system integration — everything is files, email, and copy-paste
