from bounden.axes.axes_cls import Axes
from bounden.axes.axis_operation import AxisOperation
from bounden.axes.integer_axis import IntegerAxis
from bounden.axes.no_axis_for_type import NoAxisForType
from bounden.axes.string_axis import StringAxis
from bounden.axes.types import AxesT, XAxisT, YAxisT

axes = Axes()
axes.register(int, IntegerAxis())
axes.register(str, StringAxis())

__all__ = [
    "Axes",
    "AxesT",
    "AxisOperation",
    "IntegerAxis",
    "NoAxisForType",
    "StringAxis",
    "XAxisT",
    "YAxisT",
    "axes",
]
