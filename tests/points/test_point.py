from pytest import raises

from bounden import Point


def test_add__int() -> None:
    assert Point(("Z", 2)) + 3 == ("AC", 5)


def test_add__unsupported() -> None:
    point = Point(("Z", 2))

    with raises(ValueError) as ex:
        _ = point + "foo"

    assert str(ex.value) == "'foo' (<class 'str'>) is not a vector"


def test_add__tuple() -> None:
    point = Point(("Z", 2))
    actual = point + (3, 4)
    assert actual.coordinates == ("AC", 6)


def test_coordinates() -> None:
    point = Point(("Z", 2))
    assert point.coordinates == ("Z", 2)


def test_len() -> None:
    point = Point(("Z", 2))
    assert len(point) == 2


def test_repr() -> None:
    point = Point(("Z", 2))
    assert repr(point) == "('Z', 2)"


def test_subtract() -> None:
    assert Point(("AA", 8)) - (6, 3) == ("U", 5)
