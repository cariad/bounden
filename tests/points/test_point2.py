from pytest import fixture

from bounden import IntegerCoordinate, Point2, StringCoordinate

PointType = Point2[StringCoordinate, IntegerCoordinate]


@fixture
def point() -> PointType:
    return PointType.new(StringCoordinate("ZZ"), IntegerCoordinate(2))


def test_new__type() -> None:
    class DerivedPoint2(Point2[StringCoordinate, IntegerCoordinate]):
        pass

    def require_derived(_: DerivedPoint2) -> None:
        pass

    p = DerivedPoint2.new(StringCoordinate("A"), IntegerCoordinate(1))
    require_derived(p)


# pylint: disable-next=redefined-outer-name
def test_x(point: PointType) -> None:
    assert point.x == StringCoordinate("ZZ")


# pylint: disable-next=redefined-outer-name
def test_y(point: PointType) -> None:
    assert point.y == IntegerCoordinate(2)
