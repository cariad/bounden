from pytest import fixture

from bounden import Vector2


@fixture
def vector() -> Vector2:
    return Vector2(7, 9)


# pylint: disable-next=redefined-outer-name
def test_x(vector: Vector2) -> None:
    assert vector.x == 7


# pylint: disable-next=redefined-outer-name
def test_y(vector: Vector2) -> None:
    assert vector.y == 9
