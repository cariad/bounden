from pytest import raises

from bounden.axes import Axes, NoAxisForType


def test_get__none() -> None:
    with raises(NoAxisForType) as ex:
        Axes().get("foo")

    assert str(ex.value) == "No axis for 'foo' (<class 'str'>)"
