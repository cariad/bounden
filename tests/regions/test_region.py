from pytest import fixture, raises

from bounden import Alignment, Region, ResolvedPoint, ResolvedVolume

RegionType = Region[tuple[str, int]]


@fixture
def region() -> RegionType:
    return RegionType(("A", 1), (3, 7))


def test_add() -> None:
    assert Region(("A", 1), (3, 7)) + (3, 4) == Region(("D", 5), (3, 7))


def test_arg_count_mismatch() -> None:
    with raises(ValueError) as ex:
        _ = Region((0,), (1, 1))
    assert str(ex.value) == "Coordinates count (1) != lengths count (2)"


def test_eq() -> None:
    assert Region((1, 2), (3, 4)) == Region((1, 2), (3, 4))


def test_eq__not() -> None:
    assert Region((1, 2), (3, 4)) != "foo"


# pylint: disable-next=redefined-outer-name
def test_point(region: RegionType) -> None:
    assert region.point(("Z", 9)) == ("Z", 9)


# pylint: disable-next=redefined-outer-name
def test_position(region: RegionType) -> None:
    assert region.position.coordinates == ("A", 1)


def test_repr() -> None:
    assert repr(Region((1, 2), (3, 4))) == "(1, 2) x (3, 4)"


def test_resolve__near() -> None:
    parent = Region((2, 3), (13, 15))
    child = parent.region((Alignment.Near, 4), (7, 9))
    assert child.resolve() == (
        ResolvedPoint((2, 7)),
        ResolvedVolume(7, 9),
    )


def test_resolve__center() -> None:
    parent = Region((2, 3), (7, 15))
    child = parent.region((Alignment.Center, 4), (3, 9))
    assert child.resolve() == (
        ResolvedPoint((4, 7)),
        ResolvedVolume(3, 9),
    )


def test_resolve__far() -> None:
    parent = Region((2, 3), (7, 15))
    child = parent.region((Alignment.Far, 4), (3, 9))
    assert child.resolve() == (
        ResolvedPoint((6, 7)),
        ResolvedVolume(3, 9),
    )


# pylint: disable-next=redefined-outer-name
def test_size(region: RegionType) -> None:
    assert region.volume == (3, 7)
