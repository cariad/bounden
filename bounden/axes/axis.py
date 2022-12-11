from abc import ABC, abstractmethod
from typing import Generic, SupportsFloat, SupportsInt

from vinculum import Rational

from bounden.axes.axis_operation import AxisOperation
from bounden.axes.types import ValueT
from bounden.resolve import resolved_length_to_numeric
from bounden.types import Numeric, ResolvedLength


class Axis(ABC, Generic[ValueT]):
    """
    Axis.
    """

    def add(
        self,
        a: ResolvedLength | ValueT,
        b: ResolvedLength | ValueT,
    ) -> ValueT:
        """
        Returns the axis' result of `a` + `b`.
        """

        return self.operate(a, b, AxisOperation.Add)

    def _resolve(self, value: ResolvedLength | ValueT) -> Numeric:
        resolvable = (float, int, Rational, SupportsFloat, SupportsInt)
        if isinstance(value, resolvable):
            return resolved_length_to_numeric(value)
        return self.to_decimal(value)

    def operate(
        self,
        a: ResolvedLength | ValueT,
        b: ResolvedLength | ValueT,
        op: AxisOperation,
    ) -> ValueT:
        """
        Returns the axis' result of operation `op` on `a` and `b`.
        """

        a = self._resolve(a)
        b = self._resolve(b)

        match op:
            case AxisOperation.Add:
                result = a + b

            case AxisOperation.Subtract:
                result = a - b

            case _:
                raise ValueError(f"Unrecognised AxisOperation {op}")

        return self.to_value(result)

    @abstractmethod
    def to_decimal(self, axis: ValueT) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

    @abstractmethod
    def to_value(self, decimal: ResolvedLength) -> ValueT:
        """
        Gets the axis value of decimal value `decimal`.
        """
