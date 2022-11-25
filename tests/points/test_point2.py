from bounden.points import Point2


def test_x(point2: Point2[int, int]) -> None:
    assert point2.x == 1


def test_y(point2: Point2[int, int]) -> None:
    assert point2.y == 2
