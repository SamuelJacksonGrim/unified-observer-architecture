"""
scripts/server.py — HTTP API for unified-observer-architecture.

Exposes the live IdentityState produced by UnifiedSystem so that
sovereign_manifold's observer_bridge can consume it.

Endpoints
---------
  GET /health    → {"status": "ok", "step": <int>}
  GET /identity  → IdentityState fields as JSON

Run: python scripts/server.py
Or:  uvicorn scripts.server:app --host 0.0.0.0 --port 5000
"""
from __future__ import annotations

import os
import sys
import threading
import time
from typing import Any, Dict

# Allow running as `python scripts/server.py` from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from simulation.unified_system import UnifiedSystem

# ---------------------------------------------------------------------------
# Shared state — updated by background thread, read by API handlers
# ---------------------------------------------------------------------------

_lock  = threading.Lock()
_step  = 0
_state: Dict[str, Any] = {
    "coherence_score":   1.0,
    "symmetry_score":    1.0,
    "observer_strength": 0.0,
    "memory_depth":      0,
    "biological_health": 1.0,
}


def _loop(system: UnifiedSystem, hz: float = 1.0) -> None:
    """Run UnifiedSystem at `hz` Hz and mirror its state into `_state`."""
    global _step
    interval = 1.0 / hz
    t = 0
    while True:
        start = time.monotonic()
        seed = 0.5 + 0.1 * (t % 10)
        obs = system.step(seed=seed, t=t)
        with _lock:
            s = system.state
            _state["coherence_score"]   = float(s.coherence_score)
            _state["symmetry_score"]    = float(s.symmetry_score)
            _state["observer_strength"] = float(obs)
            _state["memory_depth"]      = int(s.memory_depth)
            _state["biological_health"] = float(s.biological_health)
            _step = t
        t += 1
        time.sleep(max(0.0, interval - (time.monotonic() - start)))


# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------

app = FastAPI(
    title       = "Unified Observer Architecture",
    description = "Identity observation layer — REST interface",
    version     = "1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

_system = UnifiedSystem()
threading.Thread(target=_loop, args=(_system,), daemon=True).start()


@app.get("/health")
def health():
    with _lock:
        return {"status": "ok", "step": _step}


@app.get("/identity")
def identity():
    with _lock:
        return dict(_state)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
