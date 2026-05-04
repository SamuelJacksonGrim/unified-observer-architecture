import numpy as np

class CymaticResonance:
    def generate(self, geometry, rotation):
        upper_factor = rotation["upper"][0][0]
        lower_factor = rotation["lower"][0][0]
        modulation = (upper_factor + lower_factor) / 2.0
        return geometry * modulation
