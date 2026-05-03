from core.identity_state import IdentityState
from core.fractal_symmetry import FractalSymmetry
from core.bilateral_symmetry import BilateralSymmetry
from core.coherence_lattice import CoherenceLattice
from core.observer import Observer
from biology.phase_cycles import PhaseCycles
from memory.archive import MemoryArchive

class UnifiedSystem:
    def __init__(self):
        self.state = IdentityState()
        self.fractal = FractalSymmetry()
        self.bilateral = BilateralSymmetry()
        self.lattice = CoherenceLattice()
        self.observer = Observer()
        self.phase = PhaseCycles()
        self.memory = MemoryArchive()

    def step(self, seed, t):
        pattern = self.fractal.generate_pattern(seed)
        self.state.symmetry_score = self.bilateral.evaluate(pattern)
        bio_signal = self.phase.cycle(t)
        mem_signal = len(self.memory.retrieve_all()) * 0.01
        self.lattice.stabilize(self.state, bio_signal, mem_signal)
        return self.observer.emerge(self.state)
