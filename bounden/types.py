from __future__ import annotations

from typing import Any, SupportsFloat, SupportsInt, Union

from vinculum import Rational


class Percent:
    """
    Perecentage of a length.
    """

    def __init__(self, percent: float | int) -> None:
        self._percent = float(percent)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Percent):
            return self._percent == other._percent
        return False

    def __repr__(self) -> str:
        return str(self._percent) + "%"

    def calculate(self, length: Numeric) -> Numeric:
        """
        Calculates the percentage of `length`.
        """

        return length * (self._percent / 100)


Numeric = float | int | Rational
ResolvedLength = Numeric | SupportsFloat | SupportsInt
Length = Union[Percent, ResolvedLength]
