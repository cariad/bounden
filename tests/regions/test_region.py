from pytest import fixture, raises

from bounden.regions import Region

RegionType = Region[tuple[str, int, bool], tuple[float, float, float]]


@fixture
def region() -> RegionType:
    return RegionType(("A", 1, False), (3, 7, 9.3))


def test_arg_count_mismatch() -> None:
    with raises(ValueError) as ex:
        _ = Region[tuple[int], tuple[int, int]]((0,), (1, 1))
    assert str(ex.value) == "Coordinates count (1) != lengths count (2)"


def test_lengths(region: RegionType) -> None:
    assert region.lengths == (3, 7, 9.3)
