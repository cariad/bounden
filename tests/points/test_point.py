from bounden.points import Point


def test_position() -> None:
    assert Point[tuple[int, int]]((1, 2)).position == (1, 2)
