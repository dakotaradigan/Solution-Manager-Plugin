from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class ModelWeight:
    security_id: str  # CUSIP
    target_weight: Decimal  # e.g., 0.035 = 3.5%
    min_weight: Optional[Decimal] = None
    max_weight: Optional[Decimal] = None
    sector: Optional[str] = None
    is_substitute_eligible: bool = False


@dataclass
class ModelPortfolio:
    model_id: str
    name: str
    benchmark_index: str  # e.g., "SP500", "R1000V"
    strategy_type: str  # direct_index, custom_index, overlay
    weights: list[ModelWeight] = field(default_factory=list)
    rebalance_frequency: str = "quarterly"  # daily, weekly, monthly, quarterly
    drift_threshold_bps: int = 50
    tlh_enabled: bool = False
    wash_sale_lookback_days: int = 30
    version: int = 1
    is_active: bool = True
