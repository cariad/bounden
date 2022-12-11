from pytest import raises

from bounden import Percent, Volume


def test_eq__volume() -> None:
    assert Volume(1) == Volume(1)


def test_eq__volume__not() -> None:
    assert Volume(1) != Volume(2)


def test_get_item() -> None:
    assert Volume(1, 2, 3)[1] == 2


def test_repr() -> None:
    assert repr(Volume(1, 2, 3)) == "(1, 2, 3)"


def test_resolve__absolute() -> None:
    parent = Volume(10, 10)
    child = parent.volume(5, 5)
    assert child.resolve() == (5, 5)


def test_resolve__percent() -> None:
    parent = Volume(10, 10)
    child = parent.volume(5, Percent(10))
    assert child.resolve() == (5, 1.0)


def test_resolve__percent__orphan() -> None:
    with raises(ValueError) as ex:
        Volume(10, Percent(3)).resolve()

    expect = "Volume (10, 3.0%) has no parent so cannot fit to volume"
    assert str(ex.value) == expect


def test_resolve__same() -> None:
    parent = Volume(10, 10)
    child = parent.volume(5, Percent(10))
    assert child.resolve() is child.resolve()
