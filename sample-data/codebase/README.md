# Sample Codebase: Transition Analysis Platform

This is a synthetic codebase for testing `/solution-work:discover`. It represents a transition analysis platform at a direct indexing firm.

**This is not real code** — the function bodies are stubs. The structure, models, APIs, and config are realistic enough for `discover` to extract meaningful findings.

## What's here

```
src/
  models/
    transition_request.py  — Request intake, household accounts, concentrated positions
    tax_lot.py             — Lot-level tracking, gain/loss classification, wash sale detection
    scenario.py            — Transition scenarios, tax impact, tracking metrics, comparisons
  api/
    routes.py              — FastAPI endpoints (transitions, holdings, scenarios, proposals)
  services/
    tax_calculator.py      — Lot-level tax computation, wash sale adjustments, optimization
    transition_optimizer.py — Scenario generation, tradeoff curves, compliance checks
config/
  settings.py              — Environment config (DB, custodian SFTP, pricing, compliance)
requirements.txt           — Python dependencies
```

## Try it

```
cd sample-data/codebase
/solution-work:discover
```
