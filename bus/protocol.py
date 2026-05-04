from dataclasses import dataclass
from typing import Any

@dataclass
class SystemSignal:
    signal_type: str
    source: str
    payload: Any
    timestamp: float
