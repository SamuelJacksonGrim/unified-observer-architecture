class PhaseLock:
    def lock(self, rotation, frequency: float):
        factor = max(0.1, min(abs(frequency), 2.0))
        return {
            "upper": [[x * factor for x in row] for row in rotation["upper"]],
            "lower": [[x * factor for x in row] for row in rotation["lower"]]
        }
