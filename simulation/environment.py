import random

class Environment:
    def __init__(self):
        self.external_stress = 0.0
        self.signal_noise = 0.0

    def update(self):
        self.external_stress = random.uniform(0.0, 1.0)
        self.signal_noise = random.uniform(0.0, 0.5)
        return {
            "stress": self.external_stress,
            "noise": self.signal_noise
        }
