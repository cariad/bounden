from bounden import IntegerAxisPosition, Point, StringAxisPosition


def test_add__int() -> None:
    assert Point((StringAxisPosition("Z"), IntegerAxisPosition(2))) + 3 == (
        "AC",
        5,
    )


# def test_add__unsupported() -> None:
#     point = Point(("Z", 2))

#     with raises(ValueError) as ex:
#         _ = point + "foo"

#     assert str(ex.value) == "'foo' (<class 'str'>) is not a vector"


# def test_add__tuple() -> None:
#     point = Point(("Z", 2))
#     actual = point + (3, 4)
#     assert actual.coordinates == ("AC", 6)


# def test_coordinates() -> None:
#     point = Point(("Z", 2))
#     assert point.coordinates == ("Z", 2)


# def test_len() -> None:
#     point = Point(("Z", 2))
#     assert len(point) == 2


# def test_repr() -> None:
#     point = Point(("Z", 2))
#     assert repr(point) == "('Z', 2)"


# def test_resolve__near() -> None:
#     parent = Region(("B", 3), (LengthC(11), LengthC(11)))
#     point = parent.point((Alignment.Near, 4))
#     assert point.resolve() == ("B", 7)


# def test_resolve__center() -> None:
#     parent = Region(("B", 3), (4, 11))
#     point = parent.point((Alignment.Center, 5))
#     assert point.resolve() == ("D", 8)


# def test_resolve__far() -> None:
#     parent = Region(("B", 3), (12, 11))
#     point = parent.point((Alignment.Far, 6))
#     assert point.resolve() == ("N", 9)


# def test_subtract() -> None:
#     assert Point(("AA", 8)) - (6, 3) == ("U", 5)
