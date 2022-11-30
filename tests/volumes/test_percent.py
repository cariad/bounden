from bounden import Percent


def test_eq__fail() -> None:
    assert Percent(50) != "foo"


def test_eq__float() -> None:
    assert Percent(50) == 50.0


def test_eq__int() -> None:
    assert Percent(50) == 50


def test_eq__percent() -> None:
    assert Percent(50) == Percent(50)
