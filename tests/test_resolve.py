from bounden.resolve import resolved_length_to_numeric


def test_resolved_length_to_numeric__supports_float() -> None:
    class Foo:
        def __float__(self) -> float:
            return 3.7

    assert resolved_length_to_numeric(Foo()) == 3.7


def test_resolved_length_to_numeric__supports_int() -> None:
    class Foo:
        def __int__(self) -> int:
            return 9

    assert resolved_length_to_numeric(Foo()) == 9
