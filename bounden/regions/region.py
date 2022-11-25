from typing import Generic

from bounden.points.types import LengthsT, PointT


class Region(Generic[PointT, LengthsT]):
    """
    A region within an n-dimensional volume.

    `position` describes the region's origin.

    `lengths` describes the length of each of the region's dimensions.
    """

    def __init__(
        self,
        position: PointT,
        lengths: LengthsT,
    ) -> None:
        if len(position) != len(lengths):
            raise ValueError(
                f"Coordinates count ({len(position)}) "
                f"!= lengths count ({len(lengths)})"
            )

        self._lengths = lengths
        self._position = position

    @property
    def lengths(self) -> LengthsT:
        """
        Dimension lengths.
        """

        return self._lengths

    @property
    def position(self) -> PointT:
        """
        Position.
        """

        return self._position
