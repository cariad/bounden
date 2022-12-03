from bounden import IntegerAxis, ResolvedPoint


def test_add() -> None:
    point = ResolvedPoint((IntegerAxis(), IntegerAxis()), (1, 2))
    assert point + (3, 4) == (4, 6)


def test_repr() -> None:
    assert repr(ResolvedPoint((), (1, 2))) == "(1, 2)"
