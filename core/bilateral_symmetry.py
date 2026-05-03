import numpy as np

class BilateralSymmetry:
    def evaluate(self, pattern):
        midpoint = len(pattern) // 2
        left = pattern[:midpoint]
        right = pattern[-midpoint:][::-1]
        diff = np.mean(np.abs(left - right))
        return max(0.0, 1.0 - diff)
