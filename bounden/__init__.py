"""
&copy; 2022 Cariad Eccleston and released under the MIT License.

For usage and support, see https://github.com/cariad/bounden.
"""

from importlib.resources import files

from bounden.enums import Alignment
from bounden.points import Point, Point2
from bounden.region import Region, RegionT, ResolvedRegion, ResolvedRegionT
from bounden.region2 import Region2, Region2T, ResolvedRegion2
from bounden.resolved import ResolvedPoint, ResolvedVolume
from bounden.types import (
    AxisPosition,
    CoordinatesT,
    IntegerAxisPosition,
    IntegerLength,
    LengthC,
    Percent,
    StringAxisPosition,
    XAxisT,
    YAxisT,
)
from bounden.volume import Volume, VolumeT
from bounden.volume2 import (
    ResolvedVolume2,
    ResolvedVolume2T,
    Volume2,
    Volume2T,
)


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "AxisPosition",
    "StringAxisPosition",
    "IntegerAxisPosition",
    "IntegerLength",
    "Alignment",
    "CoordinatesT",
    "LengthC",
    "Percent",
    "Point",
    "Point2",
    "Region",
    "Region2",
    "Region2T",
    "RegionT",
    "ResolvedPoint",
    "ResolvedRegion",
    "ResolvedRegion2",
    "ResolvedRegionT",
    "ResolvedVolume",
    "ResolvedVolume2",
    "ResolvedVolume2T",
    "Volume",
    "Volume2",
    "Volume2T",
    "VolumeT",
    "XAxisT",
    "YAxisT",
    "version",
]
