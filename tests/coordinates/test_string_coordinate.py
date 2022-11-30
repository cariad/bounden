from bounden.coordinates import StringCoordinate


def test_float() -> None:
    assert float(StringCoordinate("AA")) == 27
