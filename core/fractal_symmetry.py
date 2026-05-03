import numpy as np

class FractalSymmetry:
    def __init__(self, recursion_depth: int = 5):
        self.recursion_depth = recursion_depth

    def generate_pattern(self, seed: float):
        values = [seed]
        for _ in range(self.recursion_depth):
            seed = np.sin(seed) + np.cos(seed)
            values.append(seed)
        return np.array(values)

    def stability_score(self, pattern):
        return float(np.std(pattern) ** -1 if np.std(pattern) != 0 else 1.0)
