from bounden import IntegerAxisPosition, Point2, StringAxisPosition


def test_new__type() -> None:
    class DerivedPoint2(Point2[StringAxisPosition, IntegerAxisPosition]):
        pass

    def require_derived(_: DerivedPoint2) -> None:
        pass

    require_derived(
        DerivedPoint2.new(StringAxisPosition("A"), IntegerAxisPosition(1))
    )


def test_left() -> None:
    point = Point2.new(StringAxisPosition("ZZ"), IntegerAxisPosition(3))
    assert point.left == "ZZ"


# def test_top() -> None:
#     assert Point2.new("ZZ", 3).top == 3


# def test_x() -> None:
#     assert Point2.new("ZZ", 3).x == "ZZ"


# def test_y() -> None:
#     assert Point2.new("ZZ", 3).y == 3
