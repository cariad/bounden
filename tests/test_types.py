from pytest import mark

from bounden import Percent


@mark.parametrize(
    "length, percent, expect",
    [
        (75, 0, 0),
        (75, 25, 18.75),
        (75, 50, 37.5),
        (75, 100, 75),
    ],
)
def test_percent__calculate(
    length: float,
    percent: float,
    expect: float,
) -> None:
    assert Percent(percent).calculate(length) == expect


def test_percent__eq__not() -> None:
    assert Percent(50) != Percent(51)


def test_percent__eq__percent() -> None:
    assert Percent(50) == Percent(50)


def test_percent__eq__unsupported() -> None:
    assert Percent(50) != "50"
