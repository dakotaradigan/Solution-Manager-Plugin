# Interview Notes: Quant Analyst C — Quantitative Research Team

**Date:** 2026-02-19
**Interviewer:** Dakota Radigan
**Duration:** 40 min
**Format:** Video call

## Context
PhD in financial engineering, 3 years at firm. Builds factor models and backtesting frameworks. Relies heavily on historical market data.

## Raw Notes

- Primary complaint: historical data quality. "I'll run a backtest and get anomalous results, then spend two days discovering it was a data issue — an unadjusted split, a missing dividend, a wrong price."
- Needs survivorship-bias-free datasets but current system only has active securities
- "Point-in-time data is critical for backtesting. I need to know what the data looked like on a specific date, not what it looks like after corrections."
- Uses Python almost exclusively. Current internal API has a Java SDK only. "I wrote a Python wrapper but it's brittle and I'm the only one maintaining it."
- Wants corporate actions history to properly adjust historical prices — "total return calculations are wrong if you don't account for every dividend and split"
- Data latency is less of an issue for quant work — "I can live with end-of-day data, but it needs to be *correct* end-of-day data"
- Frustrated with data access permissions: "I have to submit a ticket and wait 3 days to get access to a new dataset. By then I've moved on to something else."
- Would benefit from a data catalog — "I don't even know what datasets are available. I find out by asking around."
- Mentioned other quant teams at competitor firms have self-service data platforms with Python-native APIs
- "If you give me clean, well-documented data with a Python API, I'll build the tools myself. Just don't make me fight the data."

## Key Quotes
> "Bad data is worse than no data. At least with no data I know I don't have an answer."

> "I spend 60% of my time cleaning data and 40% doing actual research. That ratio should be flipped."

> "Point-in-time matters. If I can't reproduce a backtest result from last year using last year's data, the whole thing is meaningless."

## Observed Pain Points
1. Historical data quality issues (unadjusted actions)
2. No survivorship-bias-free datasets
3. Missing point-in-time data capability
4. No Python SDK (Java only)
5. Slow data access provisioning (3-day tickets)
6. No data catalog / discoverability
7. Time wasted on data cleaning vs. research
