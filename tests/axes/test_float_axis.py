from bounden.axes import FloatAxis


def test_to_decimal() -> None:
    assert FloatAxis().to_decimal(5.0) == 5.0


def test_to_value() -> None:
    assert FloatAxis().to_value(6) == 6.0
