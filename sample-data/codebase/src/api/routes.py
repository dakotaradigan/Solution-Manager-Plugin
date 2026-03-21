"""
Transition Analysis API — FastAPI routes.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional

router = APIRouter()


# --- Transition Request endpoints ---

@router.post("/transitions")
async def create_transition_request(
    client_name: str,
    household_id: str,
    rm_id: str,
    target_strategy: str,
    total_market_value: float,
    tax_budget: Optional[float] = None,
):
    """Create a new transition analysis request. Triggers intake validation."""
    ...


@router.get("/transitions")
async def list_transitions(
    status: Optional[str] = None,
    rm_id: Optional[str] = None,
    analyst_id: Optional[str] = None,
    priority: Optional[str] = None,
    limit: int = Query(50, le=200),
    offset: int = 0,
):
    """List transition requests with optional filters."""
    ...


@router.get("/transitions/{request_id}")
async def get_transition(request_id: str):
    """Get transition request details including accounts, holdings, and scenarios."""
    ...


@router.put("/transitions/{request_id}/assign")
async def assign_analyst(request_id: str, analyst_id: str):
    """Assign a transition analyst to a request."""
    ...


@router.put("/transitions/{request_id}/status")
async def update_status(request_id: str, status: str):
    """Update transition request status. Emits status change event."""
    ...


# --- Holdings & Tax Lot endpoints ---

@router.post("/transitions/{request_id}/holdings/upload")
async def upload_holdings(request_id: str, account_id: str):
    """
    Upload custodian holdings file. Accepts CSV, pipe-delimited, DTCC XML.
    Auto-detects format, maps securities to internal master, flags unmapped positions.
    """
    ...


@router.get("/transitions/{request_id}/holdings/{account_id}")
async def get_holdings(request_id: str, account_id: str):
    """Get parsed holdings with lot-level detail for an account."""
    ...


@router.get("/transitions/{request_id}/tax-lots")
async def get_tax_lots(
    request_id: str,
    account_id: Optional[str] = None,
    gain_type: Optional[str] = None,
):
    """Get tax lots across household. Filter by account or gain type."""
    ...


@router.get("/transitions/{request_id}/wash-sale-check")
async def check_wash_sales(request_id: str):
    """
    Run wash sale detection across all household accounts.
    Returns flagged lots with related accounts and 30-day windows.
    """
    ...


# --- Scenario endpoints ---

@router.post("/transitions/{request_id}/scenarios")
async def create_scenario(
    request_id: str,
    scenario_type: str,             # clean, in_kind, tax_budget, hybrid
    tax_budget: Optional[float] = None,
):
    """Generate a transition scenario. Runs optimizer and tax calculator."""
    ...


@router.get("/transitions/{request_id}/scenarios")
async def list_scenarios(request_id: str):
    """List all scenarios for a transition request."""
    ...


@router.get("/transitions/{request_id}/scenarios/{scenario_id}")
async def get_scenario(request_id: str, scenario_id: str):
    """Get scenario detail: tax impact, tracking metrics, proposed trades."""
    ...


@router.get("/transitions/{request_id}/tradeoff-curve")
async def get_tradeoff_curve(request_id: str, num_points: int = Query(10, le=25)):
    """
    Generate tracking error vs. tax impact efficient frontier.
    Returns array of points the PM/client can use to pick their target.
    """
    ...


@router.post("/transitions/{request_id}/scenarios/{scenario_id}/compliance-check")
async def run_compliance_check(request_id: str, scenario_id: str):
    """Run pre-trade compliance check on a scenario. Returns violations if any."""
    ...


@router.put("/transitions/{request_id}/scenarios/{scenario_id}/approve")
async def approve_scenario(request_id: str, scenario_id: str, pm_id: str):
    """PM approval of a scenario. Required before generating client proposal."""
    ...


# --- Proposal endpoints ---

@router.post("/transitions/{request_id}/proposal")
async def generate_proposal(request_id: str, scenario_ids: list[str] = Query(...)):
    """
    Generate client proposal from one or more approved scenarios.
    Returns structured JSON (not PDF) for rendering by the client portal.
    """
    ...


@router.get("/transitions/{request_id}/proposal")
async def get_proposal(request_id: str):
    """Get the latest generated proposal for a transition request."""
    ...
