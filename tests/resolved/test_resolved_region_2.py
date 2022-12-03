from bounden import (
    IntegerAxis,
    ResolvedPoint,
    ResolvedRegion2,
    ResolvedVolume,
    StringAxis,
)

x_axis = StringAxis()
y_axis = IntegerAxis()

region = ResolvedRegion2(
    (x_axis, y_axis),
    ResolvedPoint(("AA", 3)),
    ResolvedVolume(11, 13),
)


def test_bottom() -> None:
    assert region.bottom == 16


def test_height() -> None:
    assert region.height == 13


def test_left() -> None:
    assert region.left == "AA"


def test_right() -> None:
    assert region.right == "AL"


def test_top() -> None:
    assert region.top == 3


def test_width() -> None:
    assert region.width == 11


def test_x() -> None:
    assert region.x == "AA"


def test_x_axis() -> None:
    assert region.x_axis == x_axis


def test_y() -> None:
    assert region.y == 3


def test_y_axis() -> None:
    assert region.y_axis == y_axis
