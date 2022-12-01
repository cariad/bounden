from bounden.resolved import ResolvedVolume


def test__eq__resolved_volume() -> None:
    assert ResolvedVolume(1, 2, 3) == ResolvedVolume(1, 2, 3)


def test__eq__resolved_volume__not() -> None:
    assert ResolvedVolume(1, 2, 3) != ResolvedVolume(1)


def test__repr() -> None:
    assert repr(ResolvedVolume(1, 2, 3)) == "(1, 2, 3)"
