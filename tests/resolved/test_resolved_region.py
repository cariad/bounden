from bounden import IntegerAxis, ResolvedPoint, ResolvedRegion, ResolvedVolume


def test_eq__not_comparable() -> None:
    region = ResolvedRegion((), ResolvedPoint((1, 2)), ResolvedVolume(3, 4))
    assert region != "foo"


def test_eq__resolved_region() -> None:
    a = ResolvedRegion((), ResolvedPoint((1, 2)), ResolvedVolume(3, 4))
    b = ResolvedRegion((), ResolvedPoint((1, 2)), ResolvedVolume(3, 4))
    assert a == b


def test_eq__resolved_region__axes_mismatch() -> None:
    a = ResolvedRegion((), ResolvedPoint((1, 2)), ResolvedVolume(3, 4))
    b = ResolvedRegion(
        (IntegerAxis(),),
        ResolvedPoint((1, 2)),
        ResolvedVolume(3, 4),
    )
    assert a != b


def test_repr() -> None:
    region = ResolvedRegion((), ResolvedPoint((1, 2)), ResolvedVolume(3, 4))
    assert repr(region) == "(1, 2) x (3, 4)"
