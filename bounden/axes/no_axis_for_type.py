from typing import Any


class NoAxisForType(ValueError):
    """
    Raised when an axis cannot be found to handle axis `value`.
    """

    def __init__(self, value: Any) -> None:
        super().__init__(f"No axis for {repr(value)} ({type(value)})")
