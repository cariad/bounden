from bounden import LengthC, Percent, Volume2

# def require_volume2(_: Volume2) -> None:
#     pass


# def test_height() -> None:
#     assert Volume2.new(3, Percent(7)).height == Percent(7)


# def test_new__type() -> None:
#     class DerivedVolume2(Volume2):
#         pass

#     def require_derived(_: DerivedVolume2) -> None:
#         pass

#     v = DerivedVolume2.new(1, 1)
#     require_derived(v)


def test_width() -> None:
    assert Volume2.new(LengthC(Percent(3)), LengthC(7)).width == LengthC(
        Percent(3)
    )
