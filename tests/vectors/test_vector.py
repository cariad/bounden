from bounden import Vector


def test_bool__false__empty() -> None:
    assert not Vector()


def test_bool__false__zeroes() -> None:
    assert not Vector((0, 0))


def test_bool__true() -> None:
    assert Vector((1,))


def test_getitem__empty() -> None:
    assert Vector()[0] == 0
