"""
Portfolio Management API — FastAPI routes.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional

router = APIRouter()


# --- Account endpoints ---

@router.get("/accounts")
async def list_accounts(
    pm_id: Optional[str] = None,
    custodian: Optional[str] = None,
    strategy: Optional[str] = None,
    limit: int = Query(100, le=1000),
    offset: int = 0,
):
    """List accounts with optional filters."""
    ...


@router.get("/accounts/{account_id}")
async def get_account(account_id: str):
    """Get account details including current positions and drift."""
    ...


@router.get("/accounts/{account_id}/positions")
async def get_positions(account_id: str, as_of: Optional[str] = None):
    """Get positions for an account. Defaults to latest; pass as_of for historical."""
    ...


@router.get("/accounts/{account_id}/drift")
async def get_drift(account_id: str):
    """Calculate current drift from target model."""
    ...


@router.post("/accounts/{account_id}/rebalance")
async def trigger_rebalance(account_id: str):
    """Generate rebalance trades for an account. Requires compliance approval."""
    ...


@router.get("/accounts/{account_id}/cash-flows")
async def get_cash_flows(account_id: str, status: Optional[str] = None):
    """List cash flows for an account."""
    ...


# --- Model endpoints ---

@router.get("/models")
async def list_models(strategy_type: Optional[str] = None):
    """List model portfolios."""
    ...


@router.get("/models/{model_id}")
async def get_model(model_id: str):
    """Get model portfolio with current weights."""
    ...


@router.put("/models/{model_id}/weights")
async def update_model_weights(model_id: str):
    """Update target weights. Triggers drift recalculation for all linked accounts."""
    ...


# --- Security / Market Data endpoints ---

@router.get("/securities/{cusip}")
async def get_security(cusip: str):
    """Get security master record with cross-referenced identifiers."""
    ...


@router.get("/securities/{cusip}/price")
async def get_price(cusip: str, source: Optional[str] = None):
    """Get latest price. Optional source filter (bloomberg, refinitiv, custodian)."""
    ...


@router.get("/securities/{cusip}/corporate-actions")
async def get_corporate_actions(cusip: str, pending_only: bool = False):
    """Get corporate actions for a security."""
    ...


# --- Recon & Operations ---

@router.get("/recon/breaks")
async def list_recon_breaks(custodian: Optional[str] = None, severity: Optional[str] = None):
    """List open reconciliation breaks across custodians."""
    ...


@router.post("/recon/breaks/{break_id}/resolve")
async def resolve_break(break_id: str):
    """Mark a reconciliation break as resolved."""
    ...


# --- TLH endpoints ---

@router.get("/accounts/{account_id}/tlh-opportunities")
async def get_tlh_opportunities(account_id: str, min_loss: float = 1000.0):
    """Identify tax-loss harvesting opportunities for an account."""
    ...


@router.post("/accounts/{account_id}/tlh-harvest")
async def execute_tlh(account_id: str):
    """Execute tax-loss harvest. Checks wash sale rules before generating trades."""
    ...
