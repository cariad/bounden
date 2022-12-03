from bounden import ResolvedPoint


def test_repr() -> None:
    assert repr(ResolvedPoint((1, 2))) == "(1, 2)"
