from __future__ import annotations

from abc import ABC, abstractmethod
from typing import (
    Any,
    Generic,
    Sequence,
    SupportsFloat,
    SupportsInt,
    TypeVar,
    Union,
)

from vinculum import Rational

AxisUnitT = TypeVar("AxisUnitT")


class AxisPosition(ABC, Generic[AxisUnitT]):
    def __init__(self, position: AxisUnitT) -> None:
        self._position = position

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, AxisPosition):
            return bool(self._position == other._position)

        return bool(self._position == other)

    @abstractmethod
    def __add__(self: AxisPositionT, other: Any) -> AxisPositionT:
        ...

    @abstractmethod
    def __sub__(self: AxisPositionT, other: Any) -> AxisPositionT:
        ...

    @property
    def position(self) -> AxisUnitT:
        return self._position

    @abstractmethod
    def to_decimal(self, axis: AxisUnitT) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

    @abstractmethod
    def to_value(self, decimal: ResolvedLength) -> AxisUnitT:
        """
        Gets the axis value of decimal value `decimal`.
        """


AxisPositionT = TypeVar("AxisPositionT", bound=AxisPosition[Any])


# CoordinateT = TypeVar("CoordinateT", bound=AxisPosition[Any])

CoordinatesT = TypeVar("CoordinatesT", bound=Sequence[AxisPosition[Any]])


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

ResolvedLengthT = TypeVar("ResolvedLengthT", bound=ResolvedLength)


class LengthC(Generic[ResolvedLengthT]):
    def __init__(self, value: ResolvedLengthT | Percent) -> None:
        self._value = value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, LengthC):
            return bool(self.value == other.value)

        return False

    def __repr__(self) -> str:
        return repr(self._value)

    @property
    def resolved(self) -> ResolvedLengthT:
        if isinstance(self._value, Percent):
            raise TypeError()

        return self._value

    @property
    def value(self) -> ResolvedLengthT | Percent:
        return self._value


class IntegerLength(LengthC[int]):
    pass


LengthsT = TypeVar("LengthsT", bound=Sequence[LengthC[Any]])
# ResolvedLengthsT = TypeVar(
#     "ResolvedLengthsT",
#     bound=tuple[ResolvedLength, ...],
# )

XLengthT = TypeVar("XLengthT", bound=LengthC[Any])
YLengthT = TypeVar("YLengthT", bound=LengthC[Any])

AxisValueT = TypeVar("AxisValueT")
# AxisValueT must be unbound from any type because "Axis" classes will perform
# conversions from disparate types.

XAxisT = TypeVar("XAxisT", bound=AxisPosition[Any])
YAxisT = TypeVar("YAxisT", bound=AxisPosition[Any])


# XResolvedLengthT = TypeVar("XResolvedLengthT", bound=ResolvedLength)
# YResolvedLengthT = TypeVar("YResolvedLengthT", bound=ResolvedLength)

# XLengthPairT = TypeVar("XLengthPairT", bound=LengthPair)
# YLengthPairT = TypeVar("YLengthPairT", bound=LengthPair)


class StringAxisPosition(AxisPosition[str]):
    # def __eq__(self, other: Any) -> bool:
    #     if isinstance(other, str):
    #         return self._position == other

    #     return super().__eq__(other)

    def __add__(self: AxisPositionT, other: Any) -> AxisPositionT:
        return self

    def __sub__(self: AxisPositionT, other: Any) -> AxisPositionT:
        return self

    def to_decimal(self, axis: str) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

        return 0

    def to_value(self, decimal: ResolvedLength) -> str:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return "FOO"


class IntegerAxisPosition(AxisPosition[int]):
    def __add__(self: AxisPositionT, other: Any) -> AxisPositionT:
        return self

    def __sub__(self: AxisPositionT, other: Any) -> AxisPositionT:
        return self

    def to_decimal(self, axis: int) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

        return 0

    def to_value(self, decimal: ResolvedLength) -> int:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return 0
