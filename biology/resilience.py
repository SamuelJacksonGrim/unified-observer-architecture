class Resilience:
    def adapt(self, stress_level):
        return max(0.0, 1.0 - stress_level * 0.1)
