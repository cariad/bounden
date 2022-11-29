from pytest import raises

from bounden import IntegerCoordinate


def test_add__not_numeric() -> None:
    with raises(ValueError) as ex:
        _ = IntegerCoordinate(0) + "foo"

    expect = "Can translate only by numeric distances, not str ('foo')"
    assert str(ex.value) == expect


def test_eq__coordinate() -> None:
    assert IntegerCoordinate(7) == IntegerCoordinate(7)


def test_eq__not() -> None:
    assert IntegerCoordinate(7) != "foo"


def test_eq__value() -> None:
    assert IntegerCoordinate(7) == 7


def test_repr() -> None:
    assert repr(IntegerCoordinate(7)) == "7"
