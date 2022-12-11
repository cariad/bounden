from rebelbase import Base26C

from bounden.axes.axis import Axis
from bounden.resolve import resolved_length_to_numeric
from bounden.types import Numeric, ResolvedLength


class StringAxis(Axis[str]):
    """
    Axis of string values. Runs from "A" to "Z", then "AA" to "ZZ", then "AAA"
    to "ZZZ", and so on.
    """

    def to_decimal(self, axis: str) -> Numeric:
        """
        Gets the decimal value of axis value `axis`.
        """

        return float(Base26C(axis))

    def to_value(self, decimal: ResolvedLength) -> str:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return str(Base26C(float(resolved_length_to_numeric(decimal))))
