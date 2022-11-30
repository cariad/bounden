from typing import Sequence

from pytest import mark, raises

from bounden import Percent, Volume


def test_absolute__relative_but_no_parent() -> None:
    with raises(ValueError) as ex:
        Volume(Percent(10)).absolute(0)

    expect = (
        "Volume (10.0%,) cannot calculate relative length 10.0% at dimension "
        "0 without a parent volume"
    )

    assert str(ex.value) == expect


@mark.parametrize(
    "v, d, expect",
    [
        (Volume(1), 1, (2,)),
        (Volume(1), 1.5, (2.5,)),
        (Volume(7), -2, (5,)),
        (Volume(1), -6, (-5,)),
        (Volume(1, 2), 3, (4, 5)),
        (Volume(1, 2, 3), 4, (5, 6, 7)),
        (Volume(1, 2, Percent(3)), 4, (5, 6, Percent(3))),
    ],
)
def test_expand(
    v: Volume, d: float, expect: Sequence[float | int | Percent]
) -> None:
    assert v.expand(d) == expect


def test_eq__volume() -> None:
    assert Volume(1) == Volume(1)


def test_eq__volume__not() -> None:
    assert Volume(1) != Volume(2)


def test_repr() -> None:
    assert repr(Volume(1, 2, 3)) == "(1, 2, 3)"
