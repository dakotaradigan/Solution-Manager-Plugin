# Workshop Notes: Transition Analysis — Future State Discovery

**Date:** 2026-02-21
**Facilitator:** Dakota Radigan
**Participants:** 8 (2 RMs, 1 transition analyst, 2 PMs, 1 compliance officer, 1 tech lead, 1 ops manager)
**Duration:** 2 hours
**Format:** In-person workshop with Miro board

## Card Sorting Results — "What's Broken Today"

### Cluster 1: Intake & Routing (10 cards)
- Requests arrive via email, Slack, verbal, and forwarded messages
- No standard format — holdings come as CSV, PDF, screenshots, or Excel
- Missing information triggers 2-3 rounds of back-and-forth before modeling can start
- Multi-account households submitted as separate requests that aren't linked
- No priority system — $5M and $50M transitions hit the same queue
- RMs have no visibility into request status
- No SLA or turnaround commitment
- Duplicate requests when RM follows up via a different channel
- No acknowledgment that a request was received
- Requests sometimes lost in email when analyst is on PTO

### Cluster 2: Data Ingestion & Mapping (8 cards)
- Custodian file formats vary (Schwab CSV, Fidelity pipe-delimited, Pershing DTCC, BNY XML)
- Cost basis data frequently missing or incorrect
- Security mapping to internal master fails for ~10% of positions (new issues, foreign securities)
- Concentrated stock positions require manual identification and flagging
- Lot-level data not always available — some custodians send aggregate positions only
- No automated validation of incoming holdings data
- Analyst spends first day of every transition on data cleanup
- Historical cost basis from transferred accounts often unreliable

### Cluster 3: Modeling & Scenarios (9 cards)
- Excel-based modeling is slow (2-minute recalc) and fragile (no version control)
- Tax calculation logic is undocumented — lives in one analyst's head
- Wash sale detection across household accounts is manual
- No tracking error vs. tax tradeoff curve — just discrete scenarios
- In-kind transfer analysis ignores factor exposures and sector tilts
- Can't model multi-asset transitions (equity + fixed income together)
- Scenario comparison is manual — copy-paste between workbook tabs
- No way to save and reload scenarios when client changes requirements
- Model validation is spot-checking, not systematic

### Cluster 4: Output & Delivery (6 cards)
- Proposals are static 15-page PDFs generated manually from Excel
- No interactive elements — client can't explore "what if" scenarios
- Proposals look dated compared to competitor output
- No standard template — each analyst formats differently
- Takes 2-4 hours just to format the PDF after analysis is complete
- Clients can't easily compare scenarios side-by-side

### Cluster 5: Compliance & Audit (5 cards)
- Compliance reviews proposals after they're built — causes rework
- No audit trail on how scenarios were constructed or what assumptions were used
- Wash sale monitoring across household is a regulatory risk
- Restriction checks (do-not-buy, sector caps) happen manually
- No record of which version of the proposal the client agreed to

## Dot Voting — Top 5 Priorities (each participant got 3 dots)
1. **Standardized intake with automated data ingestion** — 7 votes
2. **Automated tax lot analysis with wash sale detection** — 5 votes
3. **Interactive proposals with tracking error vs. tax curve** — 4 votes
4. **Pre-trade compliance checks during modeling** — 4 votes
5. **Request tracking with status visibility** — 3 votes

## Stakeholder Tensions Observed
- RMs want speed (48-hour turnaround) vs. Analysts want completeness (correct data before modeling)
- PMs want investment fidelity (tracking error) vs. Clients want tax savings (minimize realized gains)
- Compliance wants pre-trade checks vs. Analysts want to finish the model before reviews slow them down
- Tech wants system of record + APIs vs. Analysts want to keep Excel (it's flexible, they know it)
- Everyone agrees intake is broken, but disagree on whether to build a form, an API, or both

## Key Insight from Discussion
The group identified that ~80% of every transition follows the same pattern: ingest holdings → map securities → calculate tax lots → run against model → generate scenarios. The 20% that varies (concentrated positions, multi-asset, complex households) is where human judgment is needed. The consensus was: **automate the 80%, build exception handling for the 20%.**

## Action Items
- [ ] Map current transition workflow end-to-end with Raj (transition analyst)
- [ ] Document tax calculation logic before it's only in Excel formulas
- [ ] Evaluate intake form requirements with RM team
- [ ] Schedule deep-dive on compliance integration points
- [ ] Inventory custodian file formats and mapping rules
- [ ] Research competitor proposal tools (interactive, branded)
