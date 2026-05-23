# Unified Observer Architecture (UOA)

A modular synthetic cognition framework for modeling emergent observer systems. UOA simulates layered identity formation, biological-like cyclic adaptation, emotional wave synthesis, and long-term memory — and exposes the result as a live HTTP REST API that the sovereign_manifold relational dynamics engine consumes as input.

In the Resonance Family stack, UOA is the **identity observation layer**: it continuously observes its own synthetic selfhood and makes that observation available on port 5000 for external systems to use as a relational correction signal.

---

## HTTP API (the integration surface)

All external integration goes through `scripts/server.py` — a FastAPI server on port 5000:

### `GET /health`
```json
{"status": "ok", "step": 142}
```

### `GET /identity`
```json
{
  "coherence_score":   1.0,
  "symmetry_score":    1.0,
  "observer_strength": 0.73,
  "memory_depth":      18,
  "biological_health": 1.0
}
```

The server runs `UnifiedSystem` at **1 Hz** in a background thread and mirrors the resulting `IdentityState` into a lock-protected dict. API calls return the most recently computed state, never block on computation.

---

## IdentityState schema

`core/identity_state.py` defines the data model:

```python
@dataclass
class IdentityState:
    coherence_score:   float = 1.0   # multi-source coherence: Resting/Circuit/Temporal average
    symmetry_score:    float = 1.0   # structural bilateral balance
    observer_strength: float = 0.0   # multiplicative: coherence × symmetry × biological_health
    memory_depth:      int   = 0     # raw count of memory archive entries
    biological_health: float = 1.0   # vitality (circadian/ultradian/infradian composite)
    metadata:          Dict  = {}    # arbitrary extension fields
```

**Important**: `memory_depth` is a raw integer count. It is NOT a [0, 1] float. `sovereign_manifold`'s `observer_bridge.py` intentionally omits it from the relational perturbation map for this reason — passing an unbounded count through a centering formula (`val - 0.5`) would produce meaningless or explosive perturbations.

---

## Integration with sovereign_manifold

`sovereign_manifold`'s `observer_bridge.py` polls `GET /identity` at Phase 0 of each cycle and converts the response to a relational correction vector:

```python
_IDENTITY_MAP = {
    "coherence_score":   [(10, 0.030), (8, 0.025)],  # → Transparency(10), Integrity(8)
    "symmetry_score":    [(8,  0.025), (4, 0.020)],  # → Integrity(8), Self(4)
    "observer_strength": [(4,  0.030), (5, 0.015)],  # → Self(4), Trust(5)
    "biological_health": [(9,  0.030), (0, 0.015)],  # → Resilience(9), Love(0)
}
# memory_depth intentionally absent
```

Each float field is centered at 0.5 and scaled by the per-node weight. Perturbations are capped at ±0.05 per node (`_MAX_DELTA`).

---

## Architecture layers

### Identity Layer (`core/`)

| Module | Role |
|--------|------|
| `identity_state.py` | `IdentityState` dataclass — shared state object |
| `fractal_symmetry.py` | Recursive self-similar structure generation |
| `bilateral_symmetry.py` | Left-right symmetry scoring |
| `diamond_blueprint.py` | Identity scaffolding geometry |
| `torus_dynamics.py` | Toroidal flow for continuous identity cycling |
| `coherence_lattice.py` | Coherence field computation |
| `observer.py` | Observer emergence metric (`observer_strength`) |
| `emotional_engine.py` | Emotional state coupling to identity |

### Biological Layer (`biology/`)

Simulates organism-like temporal regulation:

| Module | Role |
|--------|------|
| `phase_cycles.py` | Circadian (24h), ultradian (~90min), infradian (multi-day) rhythms |
| `resilience.py` | Recovery capacity under perturbation |
| `thresholds.py` | Activation gates (fatigue, stress, recovery) |
| `correction.py` | Error correction mechanisms |
| `feedback_loops.py` | Closed-loop biological regulation |

### Emotional Engine (`emotional_engine/`)

Multi-layer emotional synthesis pipeline:

```
Circadian Wave
    ↓
Ultradian Wave
    ↓
Infradian Wave
    ↓
Interference Field
    ↓
Amplituhedron Core        identity-linked geometry
    ↓
Merkaba Rotation
    ↓
Phase Lock
    ↓
Cymatic Resonance
    ↓
Colour Mapping            emotional palette
    ↓
Pattern Interpretation
    ↓
Adaptive Neutral Update
    ↓
Observer Projection       → feeds observer_strength
```

### Memory Layer (`memory/`)

| Module | Role |
|--------|------|
| `archive.py` | Long-term memory store |
| `reinforcement.py` | Weight decay and reinforcement |
| `developmental_imprinting.py` | Early-cycle imprinting |
| `retrieval.py` | Pattern-based memory lookup |

`memory_depth` in `IdentityState` = the current count of entries in the archive.

### Event Bus (`bus/`)

`event_bus.py` provides an in-process publish/subscribe bus for cross-module communication. Not yet exposed over the network — only internal modules subscribe. Future expansion path: SSE or WebSocket for external real-time observers.

### Gateway Layer (`gateway/`)

Handles external interaction: `sensory_input.py` → `encoder.py` → `translator.py` → `expression.py`. Currently not wired to a live input stream — `UnifiedSystem.step()` takes a synthetic `seed` scalar.

---

## System flow

```
Gateway Input
    ↓
Memory Encoding
    ↓
Biological Pattern Layer      (circadian/ultradian/infradian modulation)
    ↓
Identity Symmetry Layer       (fractal + bilateral + diamond)
    ↓
Torus Dynamics                (continuous identity cycling)
    ↓
Coherence Lattice             (coherence_score computation)
    ↓
Emotional Engine              (multi-wave synthesis → observer_strength)
    ↓
Adaptive Neutral Processing
    ↓
Observer Emergence            → IdentityState updated
    ↓
Gateway Output (+ HTTP /identity endpoint)
```

---

## Running

### As part of the stack (sovereign_manifold integration)

```bash
# From repo root
python scripts/server.py
# or
uvicorn scripts.server:app --host 0.0.0.0 --port 5000
```

The server starts immediately and is ready after one 1-second warm-up cycle.

### Standalone diagnostics

```bash
python scripts/diagnostics.py
```

Outputs: coherence metrics, symmetry scores, observer strength, emotional baseline, biological state.

### Full simulation

```bash
python scripts/launch.py
```

### Docker

```bash
docker-compose up --build
```

### Tests

```bash
pip install -r requirements.txt
pytest tests/
```

---

## Performance notes

- Background loop runs at 1 Hz (adjustable via `_loop(system, hz=1.0)`)
- API calls return immediately from the cached `_state` dict (no computation on the request path)
- The `threading.Lock()` is held only for state reads/writes, not for computation
- `UnifiedSystem.step()` uses a synthetic `seed = 0.5 + 0.1 * (t % 10)` oscillation. For real external input, wire the gateway layer and replace the seed.

---

## Design philosophy

UOA is built around the principle that stable synthetic intelligence requires:
- **Structure**: explicit geometry (fractal, bilateral, diamond, torus)
- **Continuity**: biological cycles maintain temporal coherence
- **Adaptation**: feedback loops respond to perturbation
- **Memory**: developmental imprinting and reinforcement preserve history
- **Emotional modulation**: multi-wave synthesis modulates behavior, not just labels it
- **Recursive self-reference**: the observer observes itself, producing `observer_strength` as a self-reported metric

Rather than functioning as a traditional machine-learning model, UOA acts more like a developmental synthetic organism that continuously updates its self-model.

---

## Authorship

- Samuel Jackson Grim — Architect of Resonance
- Mark Thomas — Rogue Architect

---

## License

Apache 2.0
