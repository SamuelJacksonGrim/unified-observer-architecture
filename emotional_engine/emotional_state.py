from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class EmotionalState:
    pattern: Any
    colour: Dict[str, Any]
    meaning: str
    amplitude: float
    neutral_baseline: float
