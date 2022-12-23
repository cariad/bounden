from bounden import (
    IntegerAxisPosition,
    IntegerLength,
    LengthC,
    Percent,
    Region2,
    StringAxisPosition,
)

# def require_region2(_: Region2[str, int]) -> None:
#     pass


# def test_add__type() -> None:
#     require_region2(Region2.new("ZZ", 2, 7, 9) + (1, 1))


# def test_height() -> None:
#     assert Region2.new("ZZ", 2, 7, Percent(11)).height == Percent(11)


# def test_left() -> None:
#     assert Region2.new("ZZ", 2, 7, 9).left == "ZZ"


# def test_new__type() -> None:
#     class DerivedRegion2(Region2[str, int]):
#         pass

#     def require_derived(_: DerivedRegion2) -> None:
#         pass

#     require_derived(DerivedRegion2.new("A", 1, 1, 1))


# def test_point2() -> None:
#     parent = Region2.new("ZZ", 2, 7, 9)
#     point = parent.point2("E", 9)
#     assert point.resolve() == ("AAE", 11)


# def test_point2__alignment() -> None:
#     parent = Region2.new("ZZ", 2, 7, 9)
#     point = parent.point2(Alignment.Far, 9)
#     assert point.resolve() == ("AAG", 11)


# def test_region2() -> None:
#     parent = Region2.new("ZZ", 2, 7, 9)
#     child = parent.region2(Alignment.Center, 9, 11, 12)
#     assert child.position == (Alignment.Center, 9)
#     assert child.volume == (11, 12)


# def test_resolve() -> None:
#     parent = Region2.new("ZZ", 2, 8, 9)
#     child = parent.region2(Alignment.Center, 9, 4, 12)

#     expect = ResolvedRegion2(
#         (),
#         ResolvedPoint((), ("AAB", 11)),
#         ResolvedVolume(4, 12),
#     )

#     assert child.resolve() == expect


# def test_top() -> None:
#     assert Region2.new("ZZ", 2, 7, 9).top == 2


def test_width() -> None:
    region = Region2.new(
        StringAxisPosition("ZZ"),
        IntegerAxisPosition(2),
        IntegerLength(Percent(17)),
        IntegerLength(9),
    )
    assert region.width == LengthC(Percent(17))
