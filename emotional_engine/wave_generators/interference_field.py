class InterferenceField:
    def combine(self, circadian: float, ultradian: float, infradian: float) -> float:
        return (circadian + ultradian + infradian) / 3.0
