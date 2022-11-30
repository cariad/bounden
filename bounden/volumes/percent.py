from typing import Any


class Percent:
    """
    Perecentage of a length.
    """

    def __init__(self, percent: float) -> None:
        self._percent = float(percent)

    def __eq__(self, other: Any) -> bool:
        try:
            return self._percent == float(other)
        except TypeError:
            return False

    def __float__(self) -> float:
        return self._percent

    def calculate(self, full: float) -> float:
        return full / 100 * self._percent
