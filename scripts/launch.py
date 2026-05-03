from simulation.unified_system import UnifiedSystem

system = UnifiedSystem()

for t in range(10):
    observer_strength = system.step(seed=0.5, t=t)
    print(f"Step {t}: Observer Strength = {observer_strength}")
