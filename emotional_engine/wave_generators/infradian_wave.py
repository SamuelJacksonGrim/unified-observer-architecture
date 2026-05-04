import math

class InfradianWave:
    def generate(self, t: float) -> float:
        return math.sin((2 * math.pi * t) / 72.0)
