from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

ValueT = TypeVar("ValueT")


class Coordinate(ABC, Generic[ValueT]):
    """
    Abstract base coordinate.
    """

    def __init__(self, coordinate: ValueT) -> None:
        self.coordinate = coordinate

    def __add__(self, other: Any) -> "Coordinate[ValueT]":
        if isinstance(float, int) or isinstance(other, int):
            return self.translate(other)

        raise ValueError("Can translate only by numeric distances")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Coordinate):
            return False

        o: Coordinate[Any] = other
        return bool(self.coordinate == o.coordinate)

    def __repr__(self) -> str:
        return str(self.coordinate)

    @abstractmethod
    def translate(self, distance: float) -> "Coordinate[ValueT]":
        """
        Gets a copy of this coordinate translated by `distance`.
        """
