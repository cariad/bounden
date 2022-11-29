from pytest import fixture

from bounden import IntegerCoordinate, StringCoordinate
from bounden.regions import Region2

Region2Type = Region2[StringCoordinate, IntegerCoordinate, int, int]


@fixture
def region() -> Region2Type:
    return Region2(StringCoordinate("ZZ"), IntegerCoordinate(2), 7, 9)


# pylint: disable-next=redefined-outer-name
def test_bottom(region: Region2Type) -> None:
    assert region.bottom == IntegerCoordinate(11)


# pylint: disable-next=redefined-outer-name
def test_height(region: Region2Type) -> None:
    assert region.height == 9


# pylint: disable-next=redefined-outer-name
def test_left(region: Region2Type) -> None:
    assert region.left == StringCoordinate("ZZ")


# pylint: disable-next=redefined-outer-name
def test_right(region: Region2Type) -> None:
    assert region.right == StringCoordinate("AAG")


# pylint: disable-next=redefined-outer-name
def test_top(region: Region2Type) -> None:
    assert region.top == IntegerCoordinate(2)


# pylint: disable-next=redefined-outer-name
def test_width(region: Region2Type) -> None:
    assert region.width == 7
