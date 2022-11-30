from bounden import FloatCoordinate


def test_add() -> None:
    assert FloatCoordinate(2.3) + 4.8 == FloatCoordinate(7.1)


def test_float() -> None:
    assert float(FloatCoordinate(2.3)) == 2.3


def test_subtract() -> None:
    assert FloatCoordinate(2.5) - 1.1 == FloatCoordinate(1.4)
