from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class IdentityState:
    coherence_score: float = 1.0
    symmetry_score: float = 1.0
    observer_strength: float = 0.0
    memory_depth: int = 0
    biological_health: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
