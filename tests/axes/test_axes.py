from pytest import raises

from bounden import NoAxisForType, get_axis


def test_get_axis__none() -> None:
    class Foo:
        def __repr__(self) -> str:
            return "'just foo'"

    with raises(NoAxisForType) as ex:
        get_axis(Foo())

    assert str(ex.value) == "No axis for 'just foo' (Foo)"
