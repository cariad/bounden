from bounden import Alignment, StringCoordinate


def test_repr__alignment() -> None:
    assert repr(StringCoordinate(Alignment.Near)) == "Near"


def test_value() -> None:
    assert StringCoordinate("AA").value == "AA"
