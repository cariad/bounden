from bounden import Volume2


def require_volume2(_: Volume2) -> None:
    pass


# def test_expand__type() -> None:
#     require_volume2(Volume2.new(3, 7).expand(1))


# def test_height() -> None:
#     assert Volume2.new(3, 7).height == 7


def test_new__type() -> None:
    class DerivedVolume2(Volume2):
        pass

    def require_derived(_: DerivedVolume2) -> None:
        pass

    v = DerivedVolume2.new(1, 1)
    require_derived(v)


# def test_percent() -> None:
#     parent = Volume2.new(200, 200)
#     child = Volume2.new(Percent(50), 75, within=parent)
#     assert child == (Percent(50), 75)


# def test_percent__absolute() -> None:
#     parent = Volume2.new(200, 200)
#     child = Volume2.new(Percent(50), 75, within=parent)
#     assert child.width == 100


# def test_width() -> None:
#     assert Volume2.new(3, 7).width == 3
