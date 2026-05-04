from biology.resilience import Resilience

def test_resilience():
    resilience = Resilience()
    assert resilience.adapt(0.5) > 0
