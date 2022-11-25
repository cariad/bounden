from pytest import fixture

from bounden.points import Point

PointType = Point[tuple[int, int]]


@fixture
def point() -> PointType:
    return PointType((1, 2))


# pylint: disable-next=redefined-outer-name
def test_coordinates(point: PointType) -> None:
    assert point.coordinates == (1, 2)


# pylint: disable-next=redefined-outer-name
def test_len(point: PointType) -> None:
    assert len(point) == 2
