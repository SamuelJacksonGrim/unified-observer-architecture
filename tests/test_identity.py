from core.fractal_symmetry import FractalSymmetry
from core.bilateral_symmetry import BilateralSymmetry

def test_identity_pipeline():
    fractal = FractalSymmetry()
    pattern = fractal.generate_pattern(0.5)
    bilateral = BilateralSymmetry()
    score = bilateral.evaluate(pattern)
    assert score >= 0.0
