# Workshop Notes: Market Data Platform — Future State Discovery

**Date:** 2026-02-21
**Facilitator:** Dakota Radigan
**Participants:** 8 (2 PMs, 2 traders, 1 ops lead, 1 quant, 1 compliance officer, 1 tech lead)
**Duration:** 2 hours
**Format:** In-person workshop with Miro board

## Card Sorting Results — "What's Broken Today"

### Cluster 1: Data Quality & Consistency (12 cards)
- Reference data mismatches across systems
- Corporate actions applied inconsistently
- Historical data has gaps and errors
- No single source of truth for security identifiers
- Price discrepancies between internal and vendor data
- Stale data causing incorrect valuations
- Different teams see different data for the same security
- No data validation at ingestion
- Vendor data conflicts with no resolution process
- Adjusted vs unadjusted prices unclear
- Missing securities in reference data
- No data lineage tracking

### Cluster 2: Access & Usability (8 cards)
- No Python API
- Poor API documentation
- 3-day access provisioning process
- No data catalog
- Can't self-service — need to file tickets for everything
- No sandbox/test environment for data exploration
- Query performance too slow for large datasets
- UI is outdated and non-intuitive

### Cluster 3: Timeliness (6 cards)
- Corporate actions delayed by 6+ hours
- Reconciliation only at T+1
- Real-time pricing not available in internal system
- End-of-day data delivered too late for Asian markets
- No alerting on data that matters to me
- Batch processing creates bottlenecks

### Cluster 4: Compliance & Audit (4 cards)
- No audit trail on data changes
- Can't prove data lineage to regulators
- Compliance and front office see different reference data
- No version history on corrections

## Dot Voting — Top 5 Priorities (each participant got 3 dots)
1. **Single source of truth for reference data** — 6 votes
2. **Automated corporate actions processing** — 5 votes
3. **Real-time data availability** — 4 votes
4. **Self-service data access with Python API** — 4 votes
5. **Data lineage and audit trail** — 3 votes

## Stakeholder Tensions Observed
- Traders want speed (real-time, low latency) vs. Ops wants accuracy (validated, reconciled)
- Quants want historical completeness vs. current system optimized for current-day views
- Compliance wants full audit trail vs. Tech wants system simplicity
- Everyone agrees on reference data as the foundation, but disagree on build vs. buy for the golden source

## Action Items
- [ ] Follow up with compliance officer on specific regulatory requirements for data lineage
- [ ] Map current data flow architecture with tech lead
- [ ] Schedule deep-dive on corporate actions workflow with ops team
- [ ] Evaluate vendor options for reference data management (golden source)
