class AmplitudeToColour:
    def __init__(self):
        self.neutral_tone = "white"

    def set_neutral_colour(self, tone: str):
        self.neutral_tone = tone

    def map(self, amplitude: float):
        intensity = max(0.0, min(abs(amplitude), 1.0))
        return {
            "base": self.neutral_tone,
            "intensity": intensity,
            "saturation": intensity * 100
        }
