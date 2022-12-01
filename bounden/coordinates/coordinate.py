from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from bounden.enums import Alignment
from bounden.log import log
from bounden.resolved import ResolvedCoordinate

ValueT = TypeVar("ValueT")


class Coordinate(ABC, Generic[ValueT]):
    """
    Abstract base coordinate.
    """

    def __init__(self, value: ValueT | Alignment) -> None:
        self._value = value

    def __add__(self: "CoordinateT", other: Any) -> "CoordinateT":
        return self.translate(self.parse(other))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Coordinate):
            o: Coordinate[Any] = other
            return bool(self._value == o._value)

        return bool(self._value == other)

    def __repr__(self) -> str:
        if isinstance(self._value, Alignment):
            return str(self._value.name)
        return str(self._value)

    def __sub__(self: "CoordinateT", other: Any) -> "CoordinateT":
        return self.translate(-self.parse(other))

    @abstractmethod
    def make_value(self, f: float) -> ValueT:
        """
        Creates and returns the axis value for distance `f` from the origin.
        """

    @classmethod
    def parse(cls, other: Any) -> float | int:
        """
        Attempts to parse `other` to an float or integer.
        """

        o_id = f"{repr(other)} ({other.__class__.__name__})"

        log.debug(
            "%s attempting to parse %s to float or int",
            cls.__name__,
            o_id,
        )

        if isinstance(other, (float, int)):
            return other

        try:
            return float(other)
        except ValueError as value_error:
            msg = f"{cls.__name__} could not parse {o_id} as a float or int"
            raise ValueError(msg) from value_error

    @abstractmethod
    def resolve(
        self,
        value: int | float | ValueT,
    ) -> ResolvedCoordinate[ValueT]:
        """
        Resolved the distance/value `value` to a resolved coordinate.
        """

    @abstractmethod
    def translate(self: "CoordinateT", distance: float) -> "CoordinateT":
        """
        Gets a copy of this coordinate translated by `distance`.
        """

    @property
    def value(self) -> ValueT | Alignment:
        """
        Axis value.
        """

        return self._value


CoordinateT = TypeVar("CoordinateT", bound=Coordinate[Any])
