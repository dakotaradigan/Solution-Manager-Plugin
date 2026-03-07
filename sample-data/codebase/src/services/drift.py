"""
Drift calculation service.

Calculates how far each account's actual holdings have drifted
from its target model portfolio weights.
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class DriftResult:
    account_id: str
    model_id: str
    total_drift_bps: int
    threshold_bps: int
    is_breached: bool
    positions_over: list[dict]   # [{cusip, actual_weight, target_weight, drift_bps}]
    positions_under: list[dict]
    cash_drag_bps: int = 0
    last_rebalance_date: Optional[str] = None


def calculate_drift(account_id: str) -> DriftResult:
    """
    Calculate portfolio drift for a single account.

    Steps:
    1. Load account positions + market values
    2. Load target model weights
    3. Calculate actual weight per position (mv / total_mv)
    4. Compare actual vs target for each security
    5. Sum absolute drift across all positions
    6. Include cash drag (uninvested cash / total_mv)
    7. Flag if total drift exceeds account's tolerance
    """
    ...


def calculate_drift_batch(pm_id: str) -> list[DriftResult]:
    """Calculate drift for all accounts belonging to a PM."""
    ...


def get_breached_accounts(threshold_override: Optional[int] = None) -> list[DriftResult]:
    """Return all accounts currently exceeding their drift tolerance."""
    ...
