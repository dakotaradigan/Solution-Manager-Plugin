"""
Tax calculation service for transition analysis.

Computes lot-level gain/loss, applies wash sale rules across
household accounts, and projects tax impact for proposed scenarios.
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


# Federal tax rates (2026 brackets, simplified)
FEDERAL_SHORT_TERM_RATE = Decimal("0.37")   # Ordinary income rate (top bracket)
FEDERAL_LONG_TERM_RATE = Decimal("0.20")    # Long-term capital gains (top bracket)
NIIT_RATE = Decimal("0.038")               # Net investment income tax

# State tax rates (common states, simplified)
STATE_TAX_RATES = {
    "CA": Decimal("0.133"),
    "NY": Decimal("0.109"),
    "NJ": Decimal("0.1075"),
    "CT": Decimal("0.0699"),
    "FL": Decimal("0"),
    "TX": Decimal("0"),
    "WA": Decimal("0.07"),     # Long-term only, effective 2026
    "DEFAULT": Decimal("0.05"),
}


@dataclass
class TaxProjection:
    gross_gains: Decimal
    gross_losses: Decimal
    net_gain_loss: Decimal
    federal_tax: Decimal
    state_tax: Decimal
    niit: Decimal
    total_tax: Decimal
    effective_rate: Decimal


def calculate_lot_level_tax(
    lots: list,
    proposed_dispositions: dict,    # {lot_id: "sell" | "hold" | "partial"}
    client_state: str = "DEFAULT",
) -> TaxProjection:
    """
    Calculate total tax impact for proposed lot dispositions.

    Steps:
    1. For each lot marked "sell" or "partial", calculate realized gain/loss
    2. Separate into short-term and long-term
    3. Net short-term gains against short-term losses
    4. Net long-term gains against long-term losses
    5. Apply federal + state + NIIT rates
    6. Return projection with breakdown
    """
    ...


def optimize_lot_selection(
    lots: list,
    target_sell_value: Decimal,
    tax_budget: Decimal,
    client_state: str = "DEFAULT",
    prefer_long_term_losses: bool = True,
) -> list:
    """
    Select which lots to sell to stay within a tax budget.

    Strategy:
    1. Sort lots by tax efficiency (losses first, then long-term gains, then short-term gains)
    2. Greedily select lots until target_sell_value is reached
    3. If tax_budget would be exceeded, swap highest-tax lots for lower-tax alternatives
    4. Return selected lot_ids with projected tax for each

    Note: This is a greedy heuristic, not a global optimizer.
    For complex cases (100+ lots with cross-account wash sales),
    the analyst should review and adjust.
    """
    ...


def apply_wash_sale_adjustment(
    sold_lot_tax: Decimal,
    wash_sale_lots: list,
) -> Decimal:
    """
    Adjust disallowed loss for wash sale violations.

    When a loss is disallowed due to wash sale:
    1. The disallowed loss is added to the cost basis of the replacement lot
    2. The holding period of the replacement lot is adjusted
    3. Return the adjusted tax impact (loss is deferred, not eliminated)
    """
    ...


def project_annual_tax_impact(
    current_year_realized: Decimal,
    proposed_transition_gains: Decimal,
    estimated_tlh_offset: Decimal,
    client_state: str = "DEFAULT",
) -> TaxProjection:
    """
    Project total annual tax impact including transition.

    Combines:
    - Already-realized gains/losses in the current tax year
    - Gains/losses from the proposed transition
    - Estimated future TLH opportunities in the direct indexing strategy
    """
    ...
