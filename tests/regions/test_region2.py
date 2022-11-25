from pytest import fixture

from bounden.regions import Region2

Region2Type = Region2[int, int]


@fixture
def region() -> Region2Type:
    return Region2(1, 2, 7, 9)


# pylint: disable-next=redefined-outer-name
def test_bottom(region: Region2Type) -> None:
    assert region.bottom == 11


# pylint: disable-next=redefined-outer-name
def test_bottom_right(region: Region2Type) -> None:
    assert region.bottom_right == (8, 11)


# pylint: disable-next=redefined-outer-name
def test_left(region: Region2Type) -> None:
    assert region.left == 1


# pylint: disable-next=redefined-outer-name
def test_position__x(region: Region2Type) -> None:
    assert region.position.x == 1


# pylint: disable-next=redefined-outer-name
def test_position__y(region: Region2Type) -> None:
    assert region.position.y == 2


# pylint: disable-next=redefined-outer-name
def test_right(region: Region2Type) -> None:
    assert region.right == 8


# pylint: disable-next=redefined-outer-name
def test_top(region: Region2Type) -> None:
    assert region.top == 2


# pylint: disable-next=redefined-outer-name
def test_volume__height(region: Region2Type) -> None:
    assert region.volume.height == 9


# pylint: disable-next=redefined-outer-name
def test_volume__width(region: Region2Type) -> None:
    assert region.volume.width == 7
