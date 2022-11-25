from pytest import fixture, raises

from bounden import Point, Region

RegionType = Region[
    Point[tuple[str, int, bool]],
    tuple[float, float, float],
]


@fixture
def region() -> RegionType:
    return RegionType(Point(("A", 1, False)), (3, 7, 9.3))


def test_arg_count_mismatch() -> None:
    with raises(ValueError) as ex:
        _ = Region[Point[tuple[int]], tuple[int, int]](Point((0,)), (1, 1))
    assert str(ex.value) == "Coordinates count (1) != lengths count (2)"


# pylint: disable-next=redefined-outer-name
def test_lengths(region: RegionType) -> None:
    assert region.lengths == (3, 7, 9.3)


# pylint: disable-next=redefined-outer-name
def test_position(region: RegionType) -> None:
    assert region.position.position == ("A", 1, False)
