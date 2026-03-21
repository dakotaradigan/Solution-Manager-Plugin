from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional


class ScenarioStatus(Enum):
    DRAFT = "draft"
    MODELED = "modeled"
    REVIEWED = "reviewed"       # PM has signed off
    COMPLIANCE_CLEARED = "compliance_cleared"
    SENT_TO_CLIENT = "sent_to_client"


@dataclass
class TaxImpact:
    total_realized_gains: Decimal = Decimal("0")
    short_term_gains: Decimal = Decimal("0")
    long_term_gains: Decimal = Decimal("0")
    total_realized_losses: Decimal = Decimal("0")
    short_term_losses: Decimal = Decimal("0")
    long_term_losses: Decimal = Decimal("0")
    net_tax_impact: Decimal = Decimal("0")
    estimated_federal_tax: Decimal = Decimal("0")
    estimated_state_tax: Decimal = Decimal("0")
    wash_sale_disallowed: Decimal = Decimal("0")
    num_lots_sold: int = 0
    num_lots_retained: int = 0


@dataclass
class TrackingMetrics:
    projected_tracking_error_bps: int = 0       # vs. target model
    active_share_pct: Decimal = Decimal("0")    # % of portfolio different from model
    positions_in_model: int = 0                  # positions matching target
    positions_retained_out_of_model: int = 0     # kept for tax reasons but not in target
    sector_deviation_max_bps: int = 0            # worst sector overweight/underweight
    factor_tilt_flags: list[str] = field(default_factory=list)  # e.g., ["value_overweight", "momentum_underweight"]


@dataclass
class TurnoverMetrics:
    turnover_pct: Decimal = Decimal("0")        # % of portfolio traded
    num_sells: int = 0
    num_buys: int = 0
    estimated_trading_cost_bps: int = 0
    settlement_days: int = 2                     # T+1 for equities, T+2 for some


@dataclass
class TransitionScenario:
    scenario_id: str
    request_id: str
    scenario_name: str                          # e.g., "Full Liquidation", "Tax Budget $500K"
    transition_type: str                        # clean, in_kind, tax_budget, hybrid
    status: ScenarioStatus
    created_at: datetime
    tax_impact: TaxImpact = None
    tracking_metrics: TrackingMetrics = None
    turnover_metrics: TurnoverMetrics = None
    tax_budget_limit: Optional[Decimal] = None  # for tax_budget scenarios
    tax_budget_used_pct: Optional[Decimal] = None
    proposed_trades: list[dict] = field(default_factory=list)  # [{lot_id, action, quantity, ...}]
    compliance_flags: list[str] = field(default_factory=list)  # restriction violations found
    analyst_notes: Optional[str] = None
    pm_approval: Optional[str] = None           # pm_id who approved
    version: int = 1
    updated_at: Optional[datetime] = None


@dataclass
class ScenarioComparison:
    """Side-by-side comparison of multiple scenarios for the same request."""
    request_id: str
    scenarios: list[TransitionScenario] = field(default_factory=list)
    recommended_scenario_id: Optional[str] = None
    recommendation_rationale: Optional[str] = None
