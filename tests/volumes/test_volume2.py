from bounden import Volume2


def test_height() -> None:
    assert Volume2(3, 7).height == 7


def test_width() -> None:
    assert Volume2(3, 7).width == 3
