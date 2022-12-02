from pytest import raises

from bounden.axes import IntegerAxis


def test_operate__unrecognised() -> None:
    with raises(ValueError) as ex:
        IntegerAxis().operate(0, 0, -1)  # type: ignore

    assert str(ex.value) == "Unrecognised AxisOperation -1"


def test_to_decimal() -> None:
    assert IntegerAxis().to_decimal(5) == 5


def test_to_value() -> None:
    assert IntegerAxis().to_value(6.0) == 6
