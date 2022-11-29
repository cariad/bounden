from typing import Any

from pytest import fixture, mark, raises

from bounden import (
    FloatCoordinate,
    IntegerCoordinate,
    Point,
    Region,
    StringCoordinate,
    Volume,
)

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


@mark.parametrize(
    "r, expect",
    [
        (
            Region(Point((IntegerCoordinate(2),)), Volume((6,))),
            Point((IntegerCoordinate(5),)),
        ),
        (
            Region(Point((StringCoordinate("Y"),)), Volume((4,))),
            Point((StringCoordinate("AA"),)),
        ),
        (
            Region(Point((IntegerCoordinate(2),)), Volume((7,))),
            # As an IntegerCoordinate, this is intentionally 5 rather than 5.5:
            Point((IntegerCoordinate(5),)),
        ),
        (
            Region(Point((FloatCoordinate(2),)), Volume((7,))),
            Point((FloatCoordinate(5.5),)),
        ),
        (
            Region(
                Point((StringCoordinate("Z"), IntegerCoordinate(1))),
                Volume((4, 5)),
            ),
            ("AB", 3),
        ),
        (
            Region(
                Point((FloatCoordinate(2), FloatCoordinate(3))),
                Volume((7, 9)),
            ),
            (5.5, 7.5),
        ),
        (
            Region(
                Point(
                    (
                        FloatCoordinate(2),
                        FloatCoordinate(3),
                        FloatCoordinate(4),
                    )
                ),
                Volume((11, 12, 13)),
            ),
            (7.5, 9.0, 10.5),
        ),
    ],
)
def test_center(r: Region[Any, Any], expect: Point[Any]) -> None:
    assert r.center == expect


# pylint: disable-next=redefined-outer-name
def test_position(region: RegionType) -> None:
    assert region.position.coordinates == (
        StringCoordinate("A"),
        IntegerCoordinate(1),
    )


# pylint: disable-next=redefined-outer-name
def test_size(region: RegionType) -> None:
    assert region.volume.lengths == (3, 7)
