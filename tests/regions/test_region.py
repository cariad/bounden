from pytest import fixture, raises

from bounden import Region

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


# pylint: disable-next=redefined-outer-name
def test_region(region: RegionType) -> None:
    nr = region.region(("B", 2), (10, 11))
    assert nr.position == ("B", 2)
    assert nr.volume == (10, 11)


def test_repr() -> None:
    assert repr(Region((2.1, 2.2), (6.4, 6.5))) == "(2.1, 2.2) x (6.4, 6.5)"


# pylint: disable-next=redefined-outer-name
def test_size(region: RegionType) -> None:
    assert region.volume == (3, 7)
