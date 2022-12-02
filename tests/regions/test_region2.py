from pytest import fixture

from bounden import Region2

Region2Type = Region2[str, int]


@fixture
def region() -> Region2Type:
    return Region2.new("ZZ", 2, 7, 9)


def require_region2(_: Region2Type) -> None:
    pass


def test_add__type() -> None:
    require_region2(Region2.new("ZZ", 2, 7, 9) + (1, 1))


def test_bottom() -> None:
    assert Region2.new("ZZ", 2, 7, 9).bottom == 11


# pylint: disable-next=redefined-outer-name
def test_height(region: Region2Type) -> None:
    assert region.height == 9


def test_left() -> None:
    assert Region2.new("ZZ", 2, 7, 9).left == "ZZ"


def test_new__type() -> None:
    class DerivedRegion2(Region2[str, int]):
        pass

    def require_derived(_: DerivedRegion2) -> None:
        pass

    require_derived(DerivedRegion2.new("A", 1, 1, 1))


# pylint: disable-next=redefined-outer-name
def test_point2(region: Region2Type) -> None:
    point = region.point2("C", 7)
    assert point == ("C", 7)


# pylint: disable-next=redefined-outer-name
def test_region2(region: Region2Type) -> None:
    nr = region.region2("B", 2, 10, 11)
    assert nr.position == ("B", 2)
    assert nr.volume == (10, 11)


def test_right() -> None:
    assert Region2.new("ZZ", 2, 7, 9).right == "AAG"


def test_top() -> None:
    assert Region2.new("ZZ", 2, 7, 9).top == 2


# pylint: disable-next=redefined-outer-name
def test_width(region: Region2Type) -> None:
    assert region.width == 7
