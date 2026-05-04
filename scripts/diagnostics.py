from simulation.unified_system import UnifiedSystem

class Diagnostics:
    def __init__(self):
        self.system = UnifiedSystem()

    def run(self, steps=20):
        print("=== SYSTEM DIAGNOSTICS ===")
        for t in range(steps):
            observer_strength = self.system.step(seed=0.5, t=t)
            print(
                f"Step {t} | "
                f"Coherence: {self.system.state.coherence_score:.4f} | "
                f"Symmetry: {self.system.state.symmetry_score:.4f} | "
                f"Observer: {observer_strength:.4f}"
            )

if __name__ == "__main__":
    Diagnostics().run()
