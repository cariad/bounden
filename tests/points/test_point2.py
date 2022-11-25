from pytest import fixture

from bounden.points import Point2

PointType = Point2[int, int]


@fixture
def point() -> PointType:
    return PointType(1, 2)


def test_x(point: PointType) -> None:
    assert point.x == 1


def test_y(point: PointType) -> None:
    assert point.y == 2
