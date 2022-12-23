from bounden import LengthC, ResolvedVolume2


def test_height() -> None:
    assert ResolvedVolume2.new(LengthC(1), LengthC(2)).height == 2


def test_width() -> None:
    assert ResolvedVolume2.new(LengthC(1), LengthC(2)).width == 1
