from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional


class RequestStatus(Enum):
    RECEIVED = "received"
    PENDING_DATA = "pending_data"
    DATA_VALIDATED = "data_validated"
    MODELING = "modeling"
    REVIEW = "review"
    PROPOSAL_SENT = "proposal_sent"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


class RequestPriority(Enum):
    STANDARD = "standard"       # < $10M
    HIGH = "high"               # $10M - $50M
    STRATEGIC = "strategic"     # > $50M or key relationship


class TransitionType(Enum):
    CLEAN = "clean"             # Full liquidation and rebuy
    IN_KIND = "in_kind"         # Maximum overlap retention
    TAX_BUDGET = "tax_budget"   # Constrained realized gains
    HYBRID = "hybrid"           # Mix of approaches per sleeve


class AccountTaxType(Enum):
    TAXABLE = "taxable"
    IRA = "ira"
    ROTH = "roth"
    TRUST = "trust"
    FOUNDATION = "foundation"


@dataclass
class HouseholdAccount:
    account_id: str
    custodian: str                      # schwab, fidelity, pershing, bny
    custodian_account_id: str
    tax_type: AccountTaxType
    market_value: Decimal
    num_positions: int
    has_cost_basis: bool = False
    has_lot_level_data: bool = False
    source_file_format: Optional[str] = None  # csv, pdf, fix, dtcc_xml


@dataclass
class ConcentratedPosition:
    security_id: str                    # CUSIP
    ticker: str
    current_weight_pct: Decimal         # e.g., 15.2
    restriction: str                    # do_not_sell, reduce_over_time, client_hold
    reason: Optional[str] = None        # family_legacy, company_stock, estate_planning


@dataclass
class TransitionRequest:
    request_id: str
    client_name: str
    household_id: str
    rm_id: str
    rm_name: str
    status: RequestStatus
    priority: RequestPriority
    created_at: datetime
    target_strategy: str                # model_id of target direct indexing strategy
    total_market_value: Decimal
    accounts: list[HouseholdAccount] = field(default_factory=list)
    concentrated_positions: list[ConcentratedPosition] = field(default_factory=list)
    client_tax_budget: Optional[Decimal] = None   # max realized gains client will accept
    requested_scenarios: list[TransitionType] = field(default_factory=list)
    source_manager: Optional[str] = None
    notes: Optional[str] = None
    assigned_analyst_id: Optional[str] = None
    sla_due_date: Optional[date] = None
    updated_at: Optional[datetime] = None
