from pytest import fixture

from bounden.regions import Region2

Region2Type = Region2[int, int, int, int]


@fixture
def region() -> Region2Type:
    return Region2(1, 2, 7, 9)


def test_height(region: Region2Type) -> None:
    assert region.height == 9


def test_width(region: Region2Type) -> None:
    assert region.width == 7
