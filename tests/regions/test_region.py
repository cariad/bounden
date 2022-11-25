from pytest import fixture, raises

from bounden import Point, Region, Volume

RegionType = Region[
    Point[tuple[str, int, bool]],
    Volume[tuple[float, float, float]],
]


@fixture
def region() -> RegionType:
    return RegionType(Point(("A", 1, False)), Volume((3, 7, 9.3)))


def test_arg_count_mismatch() -> None:
    with raises(ValueError) as ex:
        _ = Region[Point[tuple[int]], Volume[tuple[int, int]]](
            Point((0,)),
            Volume((1, 1)),
        )
    assert str(ex.value) == "Coordinates count (1) != lengths count (2)"


# pylint: disable-next=redefined-outer-name
def test_position(region: RegionType) -> None:
    assert region.position.coordinates == ("A", 1, False)


# pylint: disable-next=redefined-outer-name
def test_size(region: RegionType) -> None:
    assert region.volume.lengths == (3, 7, 9.3)
