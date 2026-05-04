import math

class MerkabaField:
    def __init__(self):
        self.rest_rotation = 1.0

    def set_rest_rotation(self, value: float):
        self.rest_rotation = value

    def rotate(self, t: float):
        theta = t * self.rest_rotation
        return {
            "upper": [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]],
            "lower": [[math.cos(-theta), -math.sin(-theta)], [math.sin(-theta), math.cos(-theta)]]
        }
