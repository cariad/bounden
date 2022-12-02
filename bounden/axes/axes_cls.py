from typing import Any, Type

from bounden.axes.axis import Axis
from bounden.axes.no_axis_for_type import NoAxisForType
from bounden.axes.types import ValueT


class Axes:
    """
    Axes.
    """

    def __init__(self) -> None:
        self._axes: dict[Type[Any], Axis[Any]] = {}

    def register(self, axis_type: Type[ValueT], axis: Axis[ValueT]) -> None:
        """
        Register an axis for a given value type.
        """

        self._axes[axis_type] = axis

    def get(self, value: ValueT) -> Axis[ValueT]:
        """
        Gets an axis to handle value `value`.

        Raises `NoAxisForType` if no registered axis can handle the value.
        """

        try:
            return self._axes[type(value)]
        except KeyError as key_error:
            raise NoAxisForType(value) from key_error
