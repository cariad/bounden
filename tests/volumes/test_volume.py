from typing import Sequence

from pytest import mark

from bounden import Volume


@mark.parametrize(
    "v, d, expect",
    [
        (Volume((1,)), 1, (2,)),
        (Volume((1,)), 1.5, (2.5,)),
        (Volume((7,)), -2, (5,)),
        (Volume((1,)), -6, (-5,)),
        (Volume((1, 2)), 3, (4, 5)),
        (Volume((1, 2, 3)), 4, (5, 6, 7)),
    ],
)
def test_expand(v: Volume, d: float, expect: Sequence[float | int]) -> None:
    assert v.expand(d) == expect


def test_eq__volume() -> None:
    assert Volume((1,)) == Volume((1,))


def test_eq__volume__not() -> None:
    assert Volume((1,)) != Volume((2,))


def test_repr() -> None:
    assert repr(Volume((1, 2, 3))) == "(1, 2, 3)"
