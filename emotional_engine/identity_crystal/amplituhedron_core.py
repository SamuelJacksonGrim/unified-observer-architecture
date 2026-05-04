import numpy as np

class AmplituhedronCore:
    def __init__(self):
        self.neutral_baseline = 0.0

    def set_neutral(self, neutral: float):
        self.neutral_baseline = neutral

    def transform(self, frequency: float):
        adjusted = frequency + self.neutral_baseline
        return np.array([
            np.sin(adjusted),
            np.cos(adjusted),
            np.sin(adjusted * 2),
            np.cos(adjusted * 2)
        ])
