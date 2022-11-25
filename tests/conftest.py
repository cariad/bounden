from pytest import fixture

from bounden.points import Point2


@fixture
def point2() -> Point2[int, int]:
    return Point2[int, int](1, 2)
