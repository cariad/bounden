from bounden.axes.axis import Axis
from bounden.resolve import resolved_length_to_numeric
from bounden.types import Numeric, ResolvedLength


class FloatAxis(Axis[float]):
    """
    Axis of float values.
    """

    def to_decimal(self, axis: float) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

        return axis

    def to_value(self, decimal: ResolvedLength) -> float:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return float(resolved_length_to_numeric(decimal))
