from bounden import IntegerCoordinate


def test_eq__coordinate() -> None:
    assert IntegerCoordinate(7) == IntegerCoordinate(7)


def test_eq__not() -> None:
    assert IntegerCoordinate(7) != "foo"


def test_eq__value() -> None:
    assert IntegerCoordinate(7) == 7


def test_float() -> None:
    assert float(IntegerCoordinate(7)) == 7


def test_repr() -> None:
    assert repr(IntegerCoordinate(7)) == "7"
