from bounden.points.point import Point
from bounden.points.types import XCoordinateT, YCoordinateT


class Point2(Point[tuple[XCoordinateT, YCoordinateT]]):
    """
    A point within a two-dimensional volume.
    """

    def __init__(self, x: XCoordinateT, y: YCoordinateT) -> None:
        super().__init__((x, y))

    @property
    def x(self) -> XCoordinateT:
        """
        X coordinate.
        """

        return self.value[0]

    @property
    def y(self) -> YCoordinateT:
        """
        Y coordinate.
        """

        return self.value[1]
