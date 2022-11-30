from pytest import raises

from bounden import Coordinate


def test_parse__fail() -> None:
    with raises(ValueError) as ex:
        _ = Coordinate.parse("foo")

    expect = "Coordinate could not parse 'foo' (str) as a float or int"
    assert str(ex.value) == expect
