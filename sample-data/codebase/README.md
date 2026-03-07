# Sample Codebase: Portfolio Management Platform

This is a synthetic codebase for testing `/solution-work:discover`. It represents a portfolio management platform at an investment management firm.

**This is not real code** — the function bodies are stubs. The structure, models, APIs, and config are realistic enough for `discover` to extract meaningful findings.

## What's here

```
src/
  models/
    account.py        — Account, Position, CashFlow entities
    security.py       — Security master, pricing, corporate actions
    model_portfolio.py — Target model definitions with weights
  api/
    routes.py         — FastAPI endpoints (accounts, models, securities, recon, TLH)
  services/
    recon.py          — Custodian reconciliation (Schwab, Fidelity, Pershing, BNY)
    drift.py          — Portfolio drift calculation
config/
  settings.py         — Environment config (DB, Redis, Bloomberg, custodian SFTP)
requirements.txt      — Python dependencies
```

## Try it

```
cd sample-data/codebase
/solution-work:discover
```
