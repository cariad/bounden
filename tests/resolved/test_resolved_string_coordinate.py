from bounden.resolved import ResolvedStringCoordinate


def test_float() -> None:
    assert float(ResolvedStringCoordinate("AA")) == 27


def test_from_float() -> None:
    expect = ResolvedStringCoordinate("AB")
    assert ResolvedStringCoordinate.from_float(28) == expect
