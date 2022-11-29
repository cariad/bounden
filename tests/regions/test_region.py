from pytest import fixture, raises

from bounden import Point, Region, Volume
from bounden.coordinates import IntegerCoordinate, StringCoordinate

RegionType = Region[
    Point[tuple[StringCoordinate, IntegerCoordinate]],
    Volume[tuple[float, float]],
]


@fixture
def region() -> RegionType:
    return RegionType(
        Point(
            (
                StringCoordinate("A"),
                IntegerCoordinate(1),
            )
        ),
        Volume((3, 7)),
    )


def test_arg_count_mismatch() -> None:
    with raises(ValueError) as ex:
        _ = Region[Point[tuple[IntegerCoordinate]], Volume[tuple[int, int]]](
            Point((IntegerCoordinate(0),)),
            Volume((1, 1)),
        )
    assert str(ex.value) == "Coordinates count (1) != lengths count (2)"


# pylint: disable-next=redefined-outer-name
def test_position(region: RegionType) -> None:
    assert region.position.coordinates == (
        StringCoordinate("A"),
        IntegerCoordinate(1),
    )


# pylint: disable-next=redefined-outer-name
def test_size(region: RegionType) -> None:
    assert region.volume.lengths == (3, 7)
