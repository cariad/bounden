from typing import Any, Generic, Optional, Sequence, TypeVar

from bounden.axes import Axes, AxesT, axes
from bounden.points import Point
from bounden.protocols import RegionProtocol
from bounden.volumes import Percent, Volume


class Region(RegionProtocol, Generic[AxesT]):
    """
    A region of n-dimensional space.
    """

    def __init__(
        self,
        coordinates: AxesT,
        volume: Sequence[float | int | Percent],
        axes_resolver: Optional[Axes] = None,
        parent: Optional[RegionProtocol] = None,
    ) -> None:
        if len(coordinates) != len(volume):
            raise ValueError(
                f"Coordinates count ({len(coordinates)}) "
                f"!= lengths count ({len(volume)})"
            )

        self._axes = axes_resolver or axes
        self._parent = parent
        self._position = Point[AxesT](coordinates)
        self._volume = Volume(
            *volume,
            parent=parent.volume if parent else None,
        )

    def __add__(self: "RegionT", other: Any) -> "RegionT":
        return self.__class__(
            tuple(self._position + other),
            tuple(self._volume),
            axes_resolver=self._axes,
            parent=self._parent,
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Region):
            return (
                self.position == other.position and self.volume == other.volume
            )

        return False

    def __repr__(self) -> str:
        return f"{self.position} x {self.volume}"

    def point(self, coordinates: AxesT) -> Point[AxesT]:
        """
        Creates a child point.
        """

        return self._position.__class__(
            coordinates,
            axes_resolver=self._axes,
            parent=self,
        )

    @property
    def position(self) -> Point[AxesT]:
        """
        Position.
        """

        return self._position

    def region(
        self: "RegionT",
        coordinates: AxesT,
        volume: Sequence[float | int | Percent],
    ) -> "RegionT":
        """
        Creates a child region.
        """

        return self.__class__(
            coordinates,
            volume,
            axes_resolver=self._axes,
            parent=self,
        )

    @property
    def volume(self) -> Volume:
        """
        Volume.
        """

        return self._volume


RegionT = TypeVar("RegionT", bound=Region[Any])
