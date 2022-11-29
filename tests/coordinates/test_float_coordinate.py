from bounden import FloatCoordinate


def test_translate() -> None:
    assert FloatCoordinate(2.3) + 4.8 == FloatCoordinate(7.1)
