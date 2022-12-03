from typing import Any, Generic, Sequence, TypeVar

from bounden.axes import AxesT, Axis
from bounden.resolved.resolved_point import ResolvedPoint
from bounden.resolved.resolved_volume import ResolvedVolume


class ResolvedRegion(Generic[AxesT]):
    """
    A resolved region of n-dimensional space.
    """

    def __init__(
        self,
        axes: Sequence[Axis[Any]],
        position: ResolvedPoint[AxesT],
        volume: ResolvedVolume,
    ) -> None:
        self._axes = axes
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
        return self.__class__(self._axes, self._position + other, self._volume)

    def __repr__(self) -> str:
        return f"{self._position} x {self._volume}"

    def expand(
        self: "ResolvedRegionT",
        length: float | int,
    ) -> "ResolvedRegionT":
        """
        Returns a new resolved region expanded by `length` about its centre.

        Pass a negative length to contract.
        """

        coords = self._position - (length / 2)
        position = self._position.__class__(self._axes, coords)

        lengths = [vl + length for vl in self._volume]
        volume = self._volume.__class__(*lengths)

        return self.__class__(self._axes, position, volume)

    @property
    def position(self) -> ResolvedPoint[AxesT]:
        """
        Position.
        """

        return self._position

    @property
    def volume(self) -> ResolvedVolume:
        """
        Volume.
        """

        return self._volume


ResolvedRegionT = TypeVar("ResolvedRegionT", bound=ResolvedRegion[Any])
