import numpy as np

class TorusDynamics:
    def flow(self, x, y, z, t):
        dx = np.sin(y) - z * np.cos(t)
        dy = np.sin(z) - x * np.cos(t)
        dz = np.sin(x) - y * np.cos(t)
        return dx, dy, dz
