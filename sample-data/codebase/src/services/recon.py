"""
Custodian reconciliation service.

Compares internal positions against custodian-reported positions
and flags breaks for operations review.
"""
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import Optional


class BreakSeverity(Enum):
    INFO = "info"          # < 1 share or < $100
    WARNING = "warning"    # 1-10 shares or $100-$10k
    CRITICAL = "critical"  # > 10 shares or > $10k


class BreakType(Enum):
    QUANTITY_MISMATCH = "quantity_mismatch"
    MISSING_INTERNAL = "missing_internal"    # custodian has it, we don't
    MISSING_CUSTODIAN = "missing_custodian"  # we have it, custodian doesn't
    PRICE_MISMATCH = "price_mismatch"
    IDENTIFIER_MISMATCH = "identifier_mismatch"


@dataclass
class ReconBreak:
    break_id: str
    account_id: str
    custodian: str
    security_id: str
    break_type: BreakType
    severity: BreakSeverity
    internal_value: Optional[str] = None
    custodian_value: Optional[str] = None
    difference: Optional[Decimal] = None
    is_resolved: bool = False
    resolution_note: Optional[str] = None


def run_daily_recon(custodian: str, recon_date: str) -> list[ReconBreak]:
    """
    Run daily reconciliation for a custodian.

    Process:
    1. Load internal positions as of recon_date
    2. Parse custodian file (format varies: Schwab=CSV, Fidelity=FIX, Pershing=DTCC)
    3. Match by account + CUSIP
    4. Compare quantities and market values
    5. Flag breaks by severity
    """
    ...


def load_custodian_file(custodian: str, file_path: str) -> list[dict]:
    """
    Parse custodian position file.

    Supported formats:
    - Schwab: CSV with headers
    - Fidelity: FIX-style pipe delimited
    - Pershing: DTCC format
    - BNY: proprietary XML
    """
    ...
