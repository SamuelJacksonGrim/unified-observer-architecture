import math

class CircadianWave:
    def generate(self, t: float) -> float:
        return math.sin((2 * math.pi * t) / 24.0)
