from bounden.axes.axis import Axis
from bounden.resolve import resolved_length_to_numeric
from bounden.types import Numeric, ResolvedLength


class IntegerAxis(Axis[int]):
    """
    Axis of integer values.
    """

    def to_decimal(self, axis: int) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

        return axis

    def to_value(self, decimal: ResolvedLength) -> int:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return int(resolved_length_to_numeric(decimal))
