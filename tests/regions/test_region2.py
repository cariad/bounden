from pytest import fixture

from bounden.regions import Region2

Region2Type = Region2[int, int]


@fixture
def region() -> Region2Type:
    return Region2(1, 2, 7, 9)


# pylint: disable-next=redefined-outer-name
def test_position__x(region: Region2Type) -> None:
    assert region.position.x == 1


# pylint: disable-next=redefined-outer-name
def test_position__y(region: Region2Type) -> None:
    assert region.position.y == 2


# pylint: disable-next=redefined-outer-name
def test_lengths__height(region: Region2Type) -> None:
    assert region.volume.height == 9


# pylint: disable-next=redefined-outer-name
def test_lengths__width(region: Region2Type) -> None:
    assert region.volume.width == 7
