from bounden import (  # FloatAxis,; Percent,; IntegerAxis,
    IntegerAxisPosition,
    LengthC,
    ResolvedPoint,
    ResolvedRegion,
    ResolvedVolume,
)

# def test_add() -> None:
#     axes = (IntegerAxis(), IntegerAxis())

#     region = ResolvedRegion(
#         axes,
#         ResolvedPoint(axes, (1, 2)),
#         ResolvedVolume((3, 4)),
#     )

#     expect = ResolvedRegion(
#         axes,
#         ResolvedPoint(axes, (4, 6)),
#         ResolvedVolume((3, 4)),
#     )

#     assert region + (3, 4) == expect


# def test_eq__not_comparable() -> None:
#     region = ResolvedRegion(
#         (),
#         ResolvedPoint((), (1, 2)),
#         ResolvedVolume((3, 4)),
#     )
#     assert region != "foo"


# def test_eq__resolved_region() -> None:
#     a = ResolvedRegion((), ResolvedPoint((), (1, 2)), ResolvedVolume((3, 4)))
#     b = ResolvedRegion((), ResolvedPoint((), (1, 2)), ResolvedVolume((3, 4)))
#     assert a == b


# def test_eq__resolved_region__axes_mismatch() -> None:
#     a = ResolvedRegion((), ResolvedPoint((), (1, 2)), ResolvedVolume((3, 4)))
#     b = ResolvedRegion(
#         (IntegerAxis(),),
#         ResolvedPoint((IntegerAxis(),), (1, 2)),
#         ResolvedVolume((3, 4)),
#     )
#     assert a == b


# def test_eq__resolved_region__position_mismatch() -> None:
#     a = ResolvedRegion(
#         (IntegerAxis(),),
#         ResolvedPoint((), (1, 2)),
#         ResolvedVolume((3, 4)),
#     )

#     b = ResolvedRegion(
#         (IntegerAxis(),),
#         ResolvedPoint((IntegerAxis(),), (2, 2)),
#         ResolvedVolume((3, 4)),
#     )
#     assert a != b


# def test_expand() -> None:
#     axes = (FloatAxis(), FloatAxis())

#     region = ResolvedRegion(
#         axes,
#         ResolvedPoint(axes, (7, 9)),
#         ResolvedVolume((3, 4)),
#     )

#     expanded = region.expand(3)

#     expect = ResolvedRegion(
#         axes,
#         ResolvedPoint(axes, (5.5, 7.5)),
#         ResolvedVolume((6, 7)),
#     )

#     assert expanded == expect


# def test_region() -> None:
#     axes = (IntegerAxis(), IntegerAxis())

#     parent = ResolvedRegion[tuple[int, int], tuple[int, int]](
#         axes,
#         ResolvedPoint(axes, (3, 4)),
#         ResolvedVolume((17, 18)),
#     )

#     child = parent.region((5, 7), (8, Percent(50)))

#     expect = ResolvedRegion[tuple[int, int], tuple[int, int]](
#         axes,
#         ResolvedPoint(axes, (8, 11)),
#         ResolvedVolume((8, 9)),
#     )

#     assert child.resolve() == expect


def test_repr() -> None:
    region = ResolvedRegion(
        ResolvedPoint((IntegerAxisPosition(1), IntegerAxisPosition(2))),
        ResolvedVolume((LengthC(3), LengthC(4))),
    )
    assert repr(region) == "(1, 2) x (3, 4)"
