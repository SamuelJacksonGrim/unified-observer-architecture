import math

class UltradianWave:
    def generate(self, t: float) -> float:
        return math.sin((2 * math.pi * t) / 1.5)
