from bounden.points import Point


def test_value() -> None:
    p = Point[tuple[int, int]]((1, 2))
    assert p.value == (1, 2)
