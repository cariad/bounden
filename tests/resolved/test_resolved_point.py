from bounden import IntegerAxisPosition, ResolvedPoint

point = ResolvedPoint((IntegerAxisPosition(1), IntegerAxisPosition(2)))


def test_add() -> None:
    assert point + (3, 4) == (4, 6)


def test_repr() -> None:
    assert repr(point) == "(1, 2)"
