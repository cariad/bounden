from pytest import fixture

from bounden import IntegerCoordinate, Point2, StringCoordinate

PointType = Point2[StringCoordinate, IntegerCoordinate]


@fixture
def point() -> PointType:
    return PointType(StringCoordinate("ZZ"), IntegerCoordinate(2))


# pylint: disable-next=redefined-outer-name
def test_x(point: PointType) -> None:
    assert point.x == StringCoordinate("ZZ")


# pylint: disable-next=redefined-outer-name
def test_y(point: PointType) -> None:
    assert point.y == IntegerCoordinate(2)
