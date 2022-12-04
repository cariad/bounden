from bounden import ResolvedVolume2


def test_height() -> None:
    assert ResolvedVolume2.new(1, 2).height == 2


def test_width() -> None:
    assert ResolvedVolume2.new(1, 2).width == 1
