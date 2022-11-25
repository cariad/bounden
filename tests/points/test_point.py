from pytest import fixture, raises

from bounden import Point, Vector

PointType = Point[tuple[int, int]]


@fixture
def point() -> PointType:
    return PointType((1, 2))


# pylint: disable-next=redefined-outer-name
def test_add(point: PointType) -> None:
    vector = Vector((3, 4))
    actual = point + vector
    assert actual.coordinates == (4, 6)


# pylint: disable-next=redefined-outer-name
def test_add__dimension_mismatch(point: PointType) -> None:
    with raises(ValueError) as ex:
        _ = point + Vector((0, 3, 4))

    expect = "Vector force count (3) != point dimension count (2)"
    assert str(ex.value) == expect


# pylint: disable-next=redefined-outer-name
def test_add__not_vector(point: PointType) -> None:
    with raises(ValueError) as ex:
        _ = point + "foo"

    assert str(ex.value) == "Can add only vectors (not str) to points"


# pylint: disable-next=redefined-outer-name
def test_coordinates(point: PointType) -> None:
    assert point.coordinates == (1, 2)


# pylint: disable-next=redefined-outer-name
def test_len(point: PointType) -> None:
    assert len(point) == 2
