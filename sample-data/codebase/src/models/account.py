from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional


class AccountType(Enum):
    SMA = "sma"
    UMA = "uma"
    SLEEVE = "sleeve"


class Strategy(Enum):
    DIRECT_INDEX = "direct_index"
    CUSTOM_INDEX = "custom_index"
    OVERLAY = "overlay"
    TAX_MANAGED = "tax_managed"


@dataclass
class Account:
    account_id: str
    custodian_account_id: str
    client_id: str
    account_type: AccountType
    strategy: Strategy
    model_id: str
    inception_date: date
    aum: Decimal
    drift_tolerance_bps: int
    is_taxable: bool = True
    restrictions: list[str] = field(default_factory=list)
    pm_id: Optional[str] = None
    custodian: Optional[str] = None  # schwab, fidelity, pershing


@dataclass
class Position:
    account_id: str
    security_id: str  # CUSIP
    isin: Optional[str] = None
    ticker: Optional[str] = None
    quantity: Decimal = Decimal("0")
    market_value: Decimal = Decimal("0")
    cost_basis: Decimal = Decimal("0")
    acquisition_date: Optional[date] = None
    lot_id: Optional[str] = None
    is_restricted: bool = False


@dataclass
class CashFlow:
    account_id: str
    flow_date: date
    amount: Decimal
    flow_type: str  # contribution, withdrawal, dividend, fee
    status: str  # pending, settled
