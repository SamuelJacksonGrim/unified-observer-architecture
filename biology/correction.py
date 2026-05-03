class ErrorCorrection:
    def correct(self, signal):
        return min(max(signal, -1.0), 1.0)
