from __future__ import annotations

from typing import Any, Generic, Optional, Sequence, TypeVar

# from bounden.axes import Axis  # , get_axis
from bounden.points import Point
from bounden.resolution import RegionResolver
from bounden.resolve import resolved_length_to_numeric
from bounden.resolved.resolved_point import ResolvedPoint
from bounden.resolved.resolved_volume import ResolvedVolume
from bounden.types import CoordinatesT, LengthsT, ResolvedLength
from bounden.volume import Volume


class Region(Generic[CoordinatesT, LengthsT]):
    """
    A region of n-dimensional space.
    """

    def __init__(
        self,
        coordinates: CoordinatesT,
        lengths: LengthsT,
        within: Optional[RegionResolver] = None,
    ) -> None:
        if len(coordinates) != len(lengths):
            raise ValueError(
                f"Coordinates count ({len(coordinates)}) "
                f"!= lengths count ({len(lengths)})"
            )

        self._volume = Volume(
            lengths,
            within=within.volume if within else None,
        )

        self._position = Point[CoordinatesT](
            coordinates,
            within=within,
            origin_of=self._volume.resolve,
        )

        self._resolver = RegionResolver(
            self._position.resolve,
            self._volume.resolve,
        )

        self._within = within

    def __add__(self: "RegionT", other: Any) -> "RegionT":
        return self.__class__(
            tuple(self._position + other),
            tuple(self._volume),
            within=self._within,
        )

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Region)
            and self.position == other.position
            and self.volume == other.volume
        )

    def __repr__(self) -> str:
        return f"{self._position} x {self._volume}"

    def point(self, coordinates: Any) -> Point[CoordinatesT]:
        """
        Creates a child point.
        """

        return Point(
            coordinates,
            within=self._resolver,
        )

    @property
    def position(self) -> Point[CoordinatesT]:
        """
        Position.
        """

        return self._position

    def resolve(self) -> ResolvedRegion[CoordinatesT, LengthsT]:
        """
        Resolves the region.
        """

        return ResolvedRegion(
            self._position.resolve(),
            self._volume.resolve(),
        )

    def region(
        self: "RegionT",
        coordinates: Sequence[Any],
        lengths: LengthsT,
    ) -> "RegionT":
        """
        Creates a child region.
        """

        return self.__class__(
            coordinates,
            lengths,
            within=self._resolver,
        )

    @property
    def volume(self) -> Volume[LengthsT]:
        """
        Volume.
        """

        return self._volume


class ResolvedRegion(Generic[CoordinatesT, LengthsT]):
    """
    A resolved region of n-dimensional space.
    """

    def __init__(
        self,
        position: ResolvedPoint[CoordinatesT],
        volume: ResolvedVolume[LengthsT],
    ) -> None:
        self._axes = None  # axes
        self._position = position
        self._volume = volume

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ResolvedRegion):
            return (
                self.position == other.position and self.volume == other.volume
            )

        if isinstance(other, (list, tuple)):
            return bool(
                len(other) == 2
                and self._position == other[0]
                and self._volume == other[1]
            )

        return False

    def __add__(self: "ResolvedRegionT", other: Any) -> "ResolvedRegionT":
        return self.__class__(
            # self._axes,
            self._position + other,
            self._volume,
        )

    def __repr__(self) -> str:
        return f"{self._position} x {self._volume}"

    def expand(
        self: "ResolvedRegionT",
        length: ResolvedLength,
    ) -> "ResolvedRegionT":
        """
        Returns a new resolved region expanded by `length` about its centre.

        Pass a negative length to contract.
        """

        length = resolved_length_to_numeric(length)

        coords = self._position - (length / 2)
        position = self._position.__class__(coords)

        lengths = [vl + length for vl in self._volume]
        volume = self._volume.__class__(*lengths)

        return self.__class__(position, volume)

    @property
    def position(self) -> ResolvedPoint[CoordinatesT]:
        """
        Position.
        """

        return self._position

    def region(
        self,
        coordinates: CoordinatesT,
        volume: LengthsT,
    ) -> Region[CoordinatesT, LengthsT]:
        """
        Creates and returns a new subregion.
        """

        return Region(
            coordinates,
            volume,
            within=RegionResolver(self._position, self._volume),
        )

    @property
    def volume(self) -> ResolvedVolume[LengthsT]:
        """
        Volume.
        """

        return self._volume


RegionT = TypeVar("RegionT", bound=Region[Any, Any])
ResolvedRegionT = TypeVar("ResolvedRegionT", bound=ResolvedRegion[Any, Any])
