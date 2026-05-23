# CLAUDE.md — unified-observer-architecture

## What the server actually exposes

`scripts/server.py` is a FastAPI server on port 5000 (changed from 8000 in Phase 1 to avoid collision with rfe-core2). It exposes:

- `GET /health` → `{"status": "ok"}`
- `GET /identity` → `IdentityState` JSON
- `GET /observer` → observer emergence metrics
- `GET /coherence` → coherence lattice state

`observer_bridge.py` in sovereign_manifold polls `/identity` at 1Hz and converts `IdentityState` fields to relational perturbation vectors.

## IdentityState fields — types matter

```python
@dataclass
class IdentityState:
    symmetry_score:     float   # [0, 1] — bilateral structural balance
    biological_health:  float   # [0, 1] — circadian/ultradian cycle coherence
    observer_strength:  float   # [0, 1] — emergence metric
    coherence_score:    float   # [0, 1] — lattice coherence
    memory_depth:       int     # raw count of stored memories — NOT [0,1]
```

`memory_depth` is a raw integer count. It is not a [0,1] float. `observer_bridge.py` intentionally excludes it from `_IDENTITY_MAP`. Do not add it back without a normalization strategy — a raw count run through `deviation = val - 0.5` either collapses nodes at zero or explodes at large counts.

## EventBus has no network surface

`bus/event_bus.py` is an in-process pub/sub system. It does not emit events over HTTP, WebSocket, or SSE. If you need event streaming to external consumers, add a WebSocket or SSE layer in `scripts/server.py` — the EventBus alone is not sufficient.

## The C++ coherence engine is optional

`cpp_engine/` provides a compiled coherence engine for performance. It is not required for the stack to run. If cmake is unavailable or the build fails, the Python fallback in `core/coherence_lattice.py` runs. Don't block on the C++ build for integration testing.

## Biological cycles are wall-clock-based

`biology/phase_cycles.py` derives circadian, ultradian, and infradian cycles from actual wall-clock time. The system's biological health reading at 3am is different from its reading at 3pm by design. Integration tests will see different `biological_health` values depending on when they run. This is not a bug.

## Running for stack integration

```bash
cd unified-observer-architecture
pip install -r requirements.txt
python scripts/server.py    # starts on :5000
```

Or use `run_observer.py` from the sovereign_manifold repo root, which handles the path setup and cwd change automatically.

## Port is 5000, not 8000

The original code used port 8000. It was changed to 5000 in Phase 1 to avoid collision with rfe-core2. If you see references to port 8000 in old documentation or configs, they are stale. The server runs on 5000.
