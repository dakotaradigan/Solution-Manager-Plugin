from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import Optional


class AssetClass(Enum):
    EQUITY = "equity"
    FIXED_INCOME = "fixed_income"
    CASH = "cash"
    DERIVATIVE = "derivative"
    ALTERNATIVE = "alternative"


class CorporateActionType(Enum):
    DIVIDEND = "dividend"
    SPLIT = "split"
    MERGER = "merger"
    SPINOFF = "spinoff"
    TENDER = "tender"
    NAME_CHANGE = "name_change"


@dataclass
class Security:
    cusip: str
    isin: Optional[str] = None
    sedol: Optional[str] = None
    figi: Optional[str] = None
    ticker: Optional[str] = None
    name: Optional[str] = None
    asset_class: AssetClass = AssetClass.EQUITY
    sector: Optional[str] = None
    country: str = "US"
    currency: str = "USD"
    is_active: bool = True


@dataclass
class PriceRecord:
    cusip: str
    price: Decimal
    price_date: str  # ISO date
    source: str  # bloomberg, refinitiv, custodian
    price_type: str = "close"  # close, intraday, bid, ask


@dataclass
class CorporateAction:
    event_id: str
    cusip: str
    action_type: CorporateActionType
    announcement_date: str
    effective_date: str
    details: dict = None  # varies by action type
    is_processed: bool = False
