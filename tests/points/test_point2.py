from bounden import Point2


def test_new__type() -> None:
    class DerivedPoint2(Point2[str, int]):
        pass

    def require_derived(_: DerivedPoint2) -> None:
        pass

    require_derived(DerivedPoint2.new("A", 1))


def test_left() -> None:
    assert Point2.new("ZZ", 3).left == "ZZ"


def test_top() -> None:
    assert Point2.new("ZZ", 3).top == 3


def test_x() -> None:
    assert Point2.new("ZZ", 3).x == "ZZ"


def test_y() -> None:
    assert Point2.new("ZZ", 3).y == 3
