from typing import Any

from pytest import fixture, mark, raises

from bounden import (
    FloatCoordinate,
    IntegerCoordinate,
    Length,
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


def test_eq__not() -> None:
    assert Region(Point((FloatCoordinate(2),)), Volume((6,))) != "foo"


@mark.parametrize(
    "r, d, expect",
    [
        (
            Region(Point((FloatCoordinate(2),)), Volume((6,))),
            1,
            Region(Point((FloatCoordinate(1.5),)), Volume((7,))),
        ),
        (
            Region(Point((IntegerCoordinate(2),)), Volume((6,))),
            1,
            # As an IntegerCoordinate, this is intentionally 2 rather than 1.5:
            Region(Point((IntegerCoordinate(2),)), Volume((7,))),
        ),
        (
            Region(Point((FloatCoordinate(2),)), Volume((6,))),
            -1,
            Region(Point((FloatCoordinate(2.5),)), Volume((5,))),
        ),
        (
            Region(
                Point((FloatCoordinate(2), FloatCoordinate(3))),
                Volume((6, 7)),
            ),
            -4,
            Region(
                Point((FloatCoordinate(4), FloatCoordinate(5))),
                Volume((2, 3)),
            ),
        ),
        (
            Region(
                Point((FloatCoordinate(2), FloatCoordinate(3))),
                Volume((6, 7)),
            ),
            8,
            Region(
                Point((FloatCoordinate(-2), FloatCoordinate(-1))),
                Volume((14, 15)),
            ),
        ),
    ],
)
def test_expand(
    r: Region[Any, Any],
    d: Length,
    expect: Region[Any, Any],
) -> None:
    assert r.expand(d) == expect


# pylint: disable-next=redefined-outer-name
def test_position(region: RegionType) -> None:
    assert region.position.coordinates == (
        StringCoordinate("A"),
        IntegerCoordinate(1),
    )


def test_repr() -> None:
    r = Region(
        Point((FloatCoordinate(2.1), FloatCoordinate(2.2))),
        Volume((6.4, 6.5)),
    )

    assert repr(r) == "(2.1, 2.2) x (6.4, 6.5)"


# pylint: disable-next=redefined-outer-name
def test_size(region: RegionType) -> None:
    assert region.volume.lengths == (3, 7)
