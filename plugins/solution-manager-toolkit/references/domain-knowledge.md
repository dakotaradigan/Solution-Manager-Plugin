# Domain Knowledge: Financial Services — Direct Indexing & Transition Analysis

Domain-specific content for financial services solution management. Commands and agents reference this file for identifiers, NFR defaults, regulatory requirements, failure modes, and validation flags.

This file reflects the domain of direct indexing firms — specifically the transition analysis workflow: modeling what happens when an investor moves an existing portfolio into a new investment strategy. Analyzes tax impact, tracking error, turnover, and generates scenario-based proposals.

## Financial Instrument Identifiers

| Identifier | Scope | Format | Example |
|------------|-------|--------|---------|
| CUSIP | US/Canada | 9 chars (6 issuer + 2 issue + 1 check) | 037833100 |
| ISIN | Global | 12 chars (2 country + 9 local + 1 check) | US0378331005 |
| SEDOL | UK/Ireland | 7 chars alphanumeric | 2046251 |
| FIGI | Global | 12 chars (BBG prefix) | BBG000B9XRY4 |
| Ticker | Exchange-specific | Variable | AAPL |
| RIC | Reuters | Variable with suffix | AAPL.OQ |

**Cross-reference rule:** Any canonical instrument record should carry at least ISIN + one local identifier. Flag records with only a ticker — tickers are not globally unique.

## Investment Management Concepts

### Direct Indexing & Portfolio Construction

| Concept | Definition |
|---------|-----------|
| Direct indexing | Owning individual securities to replicate an index, enabling tax-loss harvesting and customization at the account level |
| Custom indexing | Building bespoke benchmarks with client-specific exclusions (ESG screens, concentrated stock, sector tilts) |
| Model portfolio | Target allocation template applied across many accounts with account-level customization |
| Tax-loss harvesting (TLH) | Selling positions at a loss to offset gains, replacing with correlated substitutes to maintain exposure |
| Wash sale rule | IRS rule prohibiting repurchase of substantially identical security within 30 days before/after a loss sale |
| Overlay strategy | Managing exposures (currency, duration, beta) across accounts without changing underlying holdings |
| Drift / rebalancing | Deviation from target weights triggering trade generation to restore alignment |
| Sleeve | Sub-allocation within an account managed by a specific strategy or manager |
| Completion portfolio | Filling gaps in a client's total exposure by building around existing concentrated positions |

### Transition Analysis

| Concept | Definition |
|---------|-----------|
| Transition analysis | Modeling what happens when a portfolio moves from one strategy/manager to another — tax impact, tracking error, turnover, and scenario comparison |
| Clean transition | Full liquidation of source portfolio and rebuy into target model — best tracking error, worst tax impact |
| In-kind transition | Retain positions that overlap with the target model, only sell non-overlapping — best tax outcome, higher tracking error |
| Tax-budget transition | Constrained optimization — minimize tracking error subject to a ceiling on realized gains the client will accept |
| Tracking error | Statistical measure of how closely a portfolio follows its benchmark, measured in basis points |
| Active share | Percentage of portfolio holdings that differ from the target model |
| Tax budget | Maximum realized gains a client is willing to accept in a transition year |
| Concentrated position | A holding significantly overweight vs. the model, often restricted from sale (family legacy, company stock, estate planning) |
| Transition cost analysis (TCA) | Total cost of transitioning: taxes + trading costs + opportunity cost of tracking error during transition period |
| Tradeoff curve | Efficient frontier showing tracking error vs. tax impact at various tax budget levels — the key deliverable for client proposals |
| In-kind transfer rate | Percentage of portfolio market value retained as-is during transition |
| Factor tilt | Unintended exposure to risk factors (value, momentum, size) introduced by retaining positions for tax reasons |
| Turnover rate | Percentage of portfolio value traded during transition |

### Account Structures

| Structure | Description |
|-----------|------------|
| SMA (Separately Managed Account) | Individual account with direct security ownership, full tax customization |
| UMA (Unified Managed Account) | Single account with multiple sleeves/strategies managed as one |
| Model delivery | Centralized model distributed to sponsor platforms (Schwab, Fidelity, Pershing) |
| Household | Group of related accounts managed for aggregate tax efficiency |
| Taxable vs tax-deferred | Different optimization rules: taxable accounts prioritize TLH, IRAs/401k ignore wash sales |

### Tax Lot Management

| Concept | Definition |
|---------|-----------|
| Tax lot | Individual purchase record: security, quantity, cost basis, acquisition date |
| Cost basis | Original purchase price per share, used to calculate gain/loss on sale |
| Lot selection | Choosing which tax lots to sell (highest cost, FIFO, specific ID) to optimize tax outcome |
| Short-term vs long-term gains | Holding period < 1 year = short-term (taxed as ordinary income); >= 1 year = long-term (lower rate) |
| Wash sale window | 30 days before and after a loss sale — cannot repurchase substantially identical security |
| Household wash sale | Wash sale triggered by purchase in a different account within the same household (e.g., selling in taxable, buying in IRA) |
| Cost basis step-up | Adjustment of cost basis at death, eliminating embedded gains — relevant for estate-planning-driven transitions |
| Disallowed loss | Loss that cannot be recognized due to wash sale — added to cost basis of replacement lot |

### Order Management & Trading

| Concept | Definition |
|---------|-----------|
| Trade generation | Algorithmic process comparing current holdings to target model, producing orders |
| Pre-trade compliance | Checking proposed trades against restrictions before execution |
| Post-trade compliance | Verifying executed trades meet all restrictions after settlement |
| Restriction | Account-level rule: do-not-buy, do-not-sell, sector cap, ESG screen, concentrated stock hold |
| Block trading | Aggregating orders across accounts for better execution, then allocating fills |

## Transition Analysis NFR Defaults

Starting-point NFR values for transition analysis and direct indexing systems.

| Quality | Target | Conditions | Measurement |
|---------|--------|------------|-------------|
| Scenario generation latency | < 30 sec for standard transition | < 500 positions, single account | API response time |
| Scenario generation latency | < 5 min for complex transition | Multi-account household, 1000+ lots | Job completion logs |
| Tax calculation accuracy | Lot-level match to custodian records | All tax lots with cost basis data | Custodian recon |
| Tracking error accuracy | Within 5bps of production optimizer | Compared to institutional-grade optimizer | Backtest comparison |
| Tradeoff curve generation | < 2 min for 10-point curve | Standard single-account transition | API response time |
| Proposal turnaround SLA | < 48 hours for standard requests | Under 500 positions, complete data | Request timestamp to proposal sent |
| Proposal turnaround SLA | < 5 business days for complex | Multi-account, concentrated positions | Request timestamp to proposal sent |
| Holdings ingestion | < 5 min from file upload to parsed lots | Any supported custodian format | Pipeline metrics |
| Security mapping success rate | > 95% auto-matched to internal master | US equities and ETFs | Mapping logs |
| Wash sale detection accuracy | 100% across household accounts | All accounts in household | Compliance audit |
| Availability | 99.9% during business hours | Business days 7am-7pm ET | Uptime dashboard |
| Audit trail completeness | Full provenance on every scenario | All scenario versions, approvals, changes | Audit log query |
| Auditability | 7-year retention, immutable audit trail | All proposals, compliance checks, approvals | Audit log query |

## SAFe / PI Planning Terminology

| Term | Definition |
|------|-----------|
| PI (Program Increment) | 8-12 week planning cycle, typically 4-5 sprints + IP sprint |
| ART (Agile Release Train) | Long-lived team of teams (50-125 people) |
| RTE (Release Train Engineer) | Facilitator for the ART |
| Feature | ART-level deliverable, fits within one PI |
| Capability | Solution-level deliverable spanning multiple ARTs |
| Enabler | Technical infrastructure or exploration work |
| PI Objective | SMART goal committed by a team for the PI |
| WSJF | Weighted Shortest Job First — prioritization (CoD / Job Size) |
| IP Sprint | Innovation and Planning sprint at end of PI |

## Regulatory Requirements

| Regulation | Jurisdiction | Key Requirements |
|-----------|-------------|-----------------|
| Investment Advisers Act | US | Fiduciary duty, best execution, trade allocation fairness |
| IRS wash sale rules | US | 30-day window for substantially identical securities |
| IRS cost basis reporting | US | Brokers must report cost basis on covered securities (Form 1099-B) |
| SOX | US | Financial reporting controls, audit trail, data integrity |
| ERISA | US | Prudence and diversification requirements for retirement accounts |
| SEC Rule 204 / Reg SHO | US | Locate and deliver requirements for short sales |
| GDPR | EU | Personal data handling in client-facing analytics |
| MiFID II | EU | Best execution, transaction reporting, data transparency |
| BCBS 239 | Global | Risk data aggregation, accuracy, completeness, timeliness |

**Compliance flags for requirements review:**
- Does this feature handle client PII? → GDPR / privacy review required
- Does this feature affect trade execution or allocation? → Best execution / fairness review
- Does this feature produce client reports or performance numbers? → GIPS / SOX controls review
- Does this feature touch tax lot or cost basis data? → IRS reporting accuracy review
- Does this feature involve retirement accounts? → ERISA fiduciary review
- Does this feature generate trades across accounts? → Fair allocation review (no cherry-picking)
- Does this feature involve wash sale detection? → IRS wash sale compliance review
- Does this feature generate transition proposals? → Fiduciary duty review (tax impact disclosure)

## Common Failure Modes

Flag these during data model review, NFR definition, and architecture decisions:

| Failure Mode | Description | Detection | Mitigation |
|-------------|------------|-----------|------------|
| Wash sale violation across household | TLH or transition sells a position at a loss while the same security was bought within 30-day window in another household account | Pre-trade wash sale check across all household accounts | Cross-account wash sale engine, 30-day lookback across household |
| Missing cost basis | Custodian file lacks cost basis for transferred positions — tax impact can't be calculated | Cost basis completeness check on ingestion | Flag incomplete lots, request from custodian or client, block scenario generation until resolved |
| Incorrect lot-level gain classification | Short-term/long-term misclassified due to wrong acquisition date | Compare acquisition dates to holding period threshold | Validate acquisition dates against custodian records |
| Concentrated position sold in error | Restricted position (do-not-sell, family legacy) included in transition trades | Pre-trade restriction check against concentrated position list | Restriction engine integrated into optimizer, compliance gate before proposal |
| Stale pricing in tax calculations | Tax impact calculated on yesterday's prices, producing inaccurate gain/loss estimates | Price timestamp validation | Require same-day pricing for scenario generation, fallback with staleness warning |
| Factor tilt from in-kind retention | Keeping positions for tax reasons introduces unintended factor exposures (value overweight, sector concentration) | Factor analysis on proposed post-transition portfolio | Factor exposure check in optimizer, flag tilts exceeding threshold |
| Duplicate transition request | Same prospect submitted via email and Slack, two analysts start modeling independently | Dedup check on client name + household ID | Intake system with dedup rules, request acknowledgment |
| Scenario version confusion | Client asks for changes, analyst modifies scenario in-place, PM reviewed an older version | Version mismatch between PM approval and current scenario | Version control on scenarios, approval tracks specific version ID |
| Tax budget overrun | Optimizer produces scenario with realized gains exceeding client's stated budget | Tax budget constraint validation | Hard constraint in optimizer, flag scenarios within 5% of budget ceiling |
| Multi-asset modeling gap | Client has equities + fixed income + alternatives but system models each separately | Asset class coverage check | Unified multi-asset optimizer or explicit cross-sleeve reconciliation |
| Settlement timing mismatch | Transition trades assume T+1 settlement but international securities settle T+2 | Settlement cycle validation per security | Exchange-specific settlement calendar integration |
| Proposal sent without compliance review | Analyst generates and sends proposal before compliance clears restrictions | Compliance gate in proposal generation workflow | Require compliance_cleared status before proposal generation |

## Financial Services Validation Flags

When reviewing any artifact, check for these transition-analysis-specific concerns:

- **Intake standardization** — Is there a structured intake form/API, or do requests arrive as unstructured email/Slack? Flag if no standard intake.
- **Household awareness** — Does the system see across all accounts in a household for wash sale checks and aggregate tax optimization?
- **Tax status handling** — Does it distinguish taxable, tax-deferred (IRA), tax-exempt (Roth) and apply different tax logic per account?
- **Lot-level tracking** — Does the system track individual tax lots with acquisition date, cost basis, and holding period?
- **Cost basis completeness** — What happens when custodian data is missing cost basis? Is there a fallback or blocking workflow?
- **Concentrated position handling** — Can the system identify, flag, and build around positions the client won't sell?
- **Wash sale detection scope** — Does wash sale checking cover the full household, or only the account being transitioned?
- **Tracking error vs. tax tradeoff** — Can the system produce a tradeoff curve, not just discrete scenarios?
- **Factor exposure analysis** — Does in-kind transfer analysis check for unintended factor tilts from retained positions?
- **Multi-asset coverage** — Can the system model equities, fixed income, ETFs, and alternatives in a single transition?
- **Custodian integration** — Which custodians (Schwab, Fidelity, Pershing, BNY)? File formats? Auto-ingestion or manual upload?
- **Scenario versioning** — Can the system track scenario versions, link approvals to specific versions, and compare side-by-side?
- **Compliance integration** — Are restriction checks (do-not-buy, sector caps, ESG screens) run during modeling or only after?
- **Proposal output format** — Structured JSON for interactive rendering, or static PDF? Does the client see a tradeoff curve?
- **Audit trail** — Can every scenario be traced back to the intake request, the holdings data, the tax calculations, and the compliance review?
- **SLA tracking** — Is there a defined turnaround SLA, and does the system track time-to-proposal?
- **Scalability** — Can the system handle 50+ concurrent transition requests without analyst bottleneck?
