from bounden.points.types import AxesT, PointABC


class Point(PointABC[AxesT]):
    """
    A point within an n-dimensional volume.

    `position` describes the coordinates of the point.
    """

    def __init__(self, position: AxesT) -> None:
        self._position = position

    def __len__(self) -> int:
        return len(self._position)

    @property
    def position(self) -> AxesT:
        """
        Position.
        """

        return self._position
