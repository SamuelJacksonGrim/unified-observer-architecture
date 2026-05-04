from collections import deque

from emotional_engine.emotional_state import EmotionalState
from emotional_engine.wave_generators import (
    CircadianWave,
    UltradianWave,
    InfradianWave,
    InterferenceField,
)
from emotional_engine.identity_crystal import (
    AmplituhedronCore,
    MerkabaField,
    PhaseLock,
    CymaticResonance,
)
from emotional_engine.colour_system import AmplitudeToColour
from emotional_engine.interpretation import (
    PatternInterpreter,
    ObserverProjection,
)

class EmotionalEngine:
    def __init__(self, history_size: int = 1000, adaptation_rate: float = 0.05):
        self.circadian = CircadianWave()
        self.ultradian = UltradianWave()
        self.infradian = InfradianWave()
        self.field = InterferenceField()

        self.amplituhedron = AmplituhedronCore()
        self.merkaba = MerkabaField()
        self.phase_lock = PhaseLock()
        self.cymatic = CymaticResonance()

        self.colour_map = AmplitudeToColour()
        self.interpreter = PatternInterpreter()
        self.projector = ObserverProjection()

        self.history = deque(maxlen=history_size)
        self.adaptation_rate = adaptation_rate
        self.neutral_baseline = 0.0

    def _update_adaptive_neutral(self, amplitude: float):
        self.history.append(amplitude)
        if not self.history:
            return

        average = sum(self.history) / len(self.history)
        self.neutral_baseline = (
            (1 - self.adaptation_rate) * self.neutral_baseline +
            self.adaptation_rate * average
        )

        self.amplituhedron.set_neutral(self.neutral_baseline)
        self.merkaba.set_rest_rotation(1.0 + (self.neutral_baseline * 0.25))

        if self.neutral_baseline > 0.3:
            self.colour_map.set_neutral_colour("gold")
        elif self.neutral_baseline < -0.3:
            self.colour_map.set_neutral_colour("blue")
        else:
            self.colour_map.set_neutral_colour("white")

    def update(self, t: float) -> EmotionalState:
        c = self.circadian.generate(t)
        u = self.ultradian.generate(t)
        i = self.infradian.generate(t)

        frequency = self.field.combine(c, u, i)

        geometry = self.amplituhedron.transform(frequency)
        rotation = self.merkaba.rotate(t)
        locked_rotation = self.phase_lock.lock(rotation, frequency)

        pattern = self.cymatic.generate(geometry, locked_rotation)
        colour = self.colour_map.map(frequency)
        meaning = self.interpreter.interpret(pattern, colour)
        projected = self.projector.project(meaning)

        self._update_adaptive_neutral(frequency)

        return EmotionalState(
            pattern=pattern,
            colour=colour,
            meaning=projected,
            amplitude=frequency,
            neutral_baseline=self.neutral_baseline,
        )
