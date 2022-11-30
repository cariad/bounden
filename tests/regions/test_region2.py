from pytest import fixture

from bounden import (
    IntegerCoordinate,
    Percent,
    Region2,
    StringCoordinate,
    Vector2,
)

Region2Type = Region2[StringCoordinate, IntegerCoordinate]


@fixture
def region() -> Region2Type:
    return Region2.new(StringCoordinate("ZZ"), IntegerCoordinate(2), 7, 9)


def require_region2(_: Region2Type) -> None:
    pass


# pylint: disable-next=redefined-outer-name
def test_add__type(region: Region2Type) -> None:
    require_region2(region + Vector2(1, 1))


# pylint: disable-next=redefined-outer-name
def test_absolute__from_subregion(region: Region2Type) -> None:
    child = region.region2(
        StringCoordinate("A"),
        IntegerCoordinate(1),
        Percent(1),
        1,
    )
    assert child.width == 0.07


# pylint: disable-next=redefined-outer-name
def test_absolute__type(region: Region2Type) -> None:
    require_region2(region.absolute)


# pylint: disable-next=redefined-outer-name
def test_bottom(region: Region2Type) -> None:
    assert region.bottom == IntegerCoordinate(11)


# pylint: disable-next=redefined-outer-name
def test_expand__type(region: Region2Type) -> None:
    require_region2(region.expand(1))


# pylint: disable-next=redefined-outer-name
def test_height(region: Region2Type) -> None:
    assert region.height == 9


# pylint: disable-next=redefined-outer-name
def test_left(region: Region2Type) -> None:
    assert region.left == StringCoordinate("ZZ")


def test_new__type() -> None:
    class DerivedRegion2(Region2[StringCoordinate, IntegerCoordinate]):
        pass

    def require_derived(_: DerivedRegion2) -> None:
        pass

    r = DerivedRegion2.new(StringCoordinate("A"), IntegerCoordinate(1), 1, 1)
    require_derived(r)


# pylint: disable-next=redefined-outer-name
def test_point2(region: Region2Type) -> None:
    point = region.point2(StringCoordinate("C"), IntegerCoordinate(7))
    assert point == ("C", 7)


# pylint: disable-next=redefined-outer-name
def test_region2(region: Region2Type) -> None:
    nr = region.region2(StringCoordinate("B"), IntegerCoordinate(2), 10, 11)
    assert nr.position == ("B", 2)
    assert nr.volume == (10, 11)


# pylint: disable-next=redefined-outer-name
def test_region__absolute2(region: Region2Type) -> None:
    nr = region.region2(StringCoordinate("B"), IntegerCoordinate(2), 10, 11)
    na = nr.absolute
    assert na.position == ("AAB", 4)
    assert na.volume == (10, 11)


# pylint: disable-next=redefined-outer-name
def test_right(region: Region2Type) -> None:
    assert region.right == StringCoordinate("AAG")


# pylint: disable-next=redefined-outer-name
def test_top(region: Region2Type) -> None:
    assert region.top == IntegerCoordinate(2)


# pylint: disable-next=redefined-outer-name
def test_width(region: Region2Type) -> None:
    assert region.width == 7
