"""
Transition optimization service.

Generates transition scenarios that balance tracking error against
tax impact, subject to constraints (concentrated positions, wash sales,
compliance restrictions).
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class OptimizationConstraints:
    tax_budget: Optional[Decimal] = None        # Max realized gains
    max_tracking_error_bps: int = 200           # Max acceptable tracking error
    max_turnover_pct: Decimal = Decimal("100")  # 100% = full liquidation allowed
    restricted_securities: list[str] = None      # CUSIPs that cannot be sold
    sector_bounds: dict = None                   # {"Technology": (0.15, 0.30)} min/max
    wash_sale_accounts: list[str] = None         # Account IDs to check for wash sales


@dataclass
class OptimizationResult:
    scenario_type: str
    proposed_trades: list[dict]     # [{lot_id, action, quantity, projected_gain_loss}]
    tracking_error_bps: int
    tax_impact: Decimal
    turnover_pct: Decimal
    in_kind_transfer_pct: Decimal   # % of portfolio value kept as-is
    wash_sale_violations: list[dict]
    compliance_flags: list[str]
    converged: bool                 # Did optimizer find a valid solution?
    iterations: int


def generate_clean_transition(
    current_holdings: list,
    target_model: dict,
    constraints: OptimizationConstraints,
) -> OptimizationResult:
    """
    Full liquidation scenario: sell everything, buy target model.

    This is the simplest scenario — produces the best tracking error
    but the worst tax impact. Useful as a baseline for comparison.
    """
    ...


def generate_in_kind_transition(
    current_holdings: list,
    target_model: dict,
    constraints: OptimizationConstraints,
) -> OptimizationResult:
    """
    Maximum in-kind transfer: keep every position that overlaps with
    the target model, only sell positions not in the model.

    Steps:
    1. Match current holdings to target model by CUSIP
    2. For overlapping positions: keep up to target weight, sell excess
    3. For non-overlapping: sell entirely (unless restricted)
    4. Buy positions in model that aren't in current holdings
    5. Calculate resulting tracking error and tax impact
    """
    ...


def generate_tax_budget_transition(
    current_holdings: list,
    target_model: dict,
    constraints: OptimizationConstraints,
) -> OptimizationResult:
    """
    Tax-budget constrained transition: minimize tracking error subject
    to a ceiling on realized gains.

    This is the most complex scenario. Uses iterative optimization:
    1. Start with in-kind baseline
    2. Sort non-overlapping positions by tax cost (cheapest to sell first)
    3. Sell positions greedily until tax budget is reached
    4. Buy into underweight model positions with proceeds
    5. Check tracking error — if still above threshold, flag for review
    6. Validate no wash sale violations across household
    """
    ...


def generate_tradeoff_curve(
    current_holdings: list,
    target_model: dict,
    constraints: OptimizationConstraints,
    num_points: int = 10,
) -> list[OptimizationResult]:
    """
    Generate a tracking error vs. tax impact efficient frontier.

    Runs tax_budget_transition with varying tax budgets from $0
    (pure in-kind) to unlimited (clean transition), producing a
    curve the PM and client can use to select their preferred point.

    Returns a list of OptimizationResults at different tax budget levels.
    """
    ...


def check_compliance(
    proposed_trades: list[dict],
    account_restrictions: list[dict],
) -> list[str]:
    """
    Pre-trade compliance check for proposed transition trades.

    Checks:
    - Do-not-buy restrictions
    - Do-not-sell restrictions
    - Sector concentration limits
    - Single security position limits
    - ESG exclusion lists
    - Client-specific holds (concentrated positions)

    Returns list of violation descriptions. Empty list = compliant.
    """
    ...
