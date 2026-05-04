from gateway.encoder import Encoder

def test_encoding():
    encoder = Encoder()
    encoded = encoder.encode({"test": 123})
    assert isinstance(encoded, str)
