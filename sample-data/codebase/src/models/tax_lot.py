from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional


class GainType(Enum):
    SHORT_TERM = "short_term"   # Held < 1 year
    LONG_TERM = "long_term"     # Held >= 1 year


class LotDisposition(Enum):
    HOLD = "hold"               # Keep in transition (in-kind)
    SELL = "sell"               # Liquidate
    PARTIAL_SELL = "partial"    # Reduce but don't eliminate
    RESTRICTED = "restricted"   # Cannot sell (concentrated position hold)


@dataclass
class TaxLot:
    lot_id: str
    account_id: str
    security_id: str            # CUSIP
    ticker: Optional[str] = None
    quantity: Decimal = Decimal("0")
    cost_basis_per_share: Decimal = Decimal("0")
    total_cost_basis: Decimal = Decimal("0")
    current_price: Decimal = Decimal("0")
    market_value: Decimal = Decimal("0")
    acquisition_date: Optional[date] = None
    gain_loss: Decimal = Decimal("0")
    gain_type: Optional[GainType] = None
    unrealized_gain_pct: Decimal = Decimal("0")
    disposition: LotDisposition = LotDisposition.HOLD
    wash_sale_flag: bool = False
    wash_sale_related_account: Optional[str] = None  # account_id of related wash sale


@dataclass
class WashSaleWindow:
    """Tracks the 30-day wash sale window for a security across household accounts."""
    security_id: str
    sold_date: date
    sold_account_id: str
    window_start: date          # sold_date - 30 days
    window_end: date            # sold_date + 30 days
    related_lots: list[str] = None  # lot_ids in other accounts that would trigger wash sale


def classify_gain_type(acquisition_date: date, sale_date: date) -> GainType:
    """Short-term if held less than 1 year, long-term otherwise."""
    ...


def calculate_lot_gain_loss(lot: TaxLot) -> Decimal:
    """Calculate unrealized gain/loss for a single lot."""
    ...


def detect_wash_sales(
    household_lots: list[TaxLot],
    proposed_sales: list[str],      # lot_ids being sold
    sale_date: date,
) -> list[WashSaleWindow]:
    """
    Detect wash sale violations across all accounts in a household.

    For each proposed sale at a loss:
    1. Check all other accounts in the household
    2. Find lots of the same or substantially identical security
    3. Purchased within 30 days before or after the sale date
    4. Flag as wash sale violation
    """
    ...
