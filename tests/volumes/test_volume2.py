from pytest import fixture

from bounden import Volume2

Volume2Type = Volume2[int, int]


def require_volume2(_: Volume2Type) -> None:
    pass


@fixture
def volume2() -> Volume2Type:
    return Volume2Type.new(3, 7)


# pylint: disable-next=redefined-outer-name
def test_expand__type(volume2: Volume2Type) -> None:
    require_volume2(volume2.expand(1))


# pylint: disable-next=redefined-outer-name
def test_height(volume2: Volume2Type) -> None:
    assert volume2.height == 7


# pylint: disable-next=redefined-outer-name
def test_width(volume2: Volume2Type) -> None:
    assert volume2.width == 3
