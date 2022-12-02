from typing import Any, Optional, Type, TypeVar

from bounden.axes import Axes, XAxisT, YAxisT
from bounden.points.point import Point
from bounden.protocols import RegionProtocol


class Point2(Point[tuple[XAxisT, YAxisT]]):
    """
    A point in two-dimensional space.
    """

    @classmethod
    def new(
        cls: Type["Point2T"],
        x: XAxisT,
        y: YAxisT,
        axes: Optional[Axes] = None,
        parent: Optional[RegionProtocol] = None,
    ) -> "Point2T":
        """
        Creates a new `Point2`.
        """

        return cls((x, y), axes_resolver=axes, parent=parent)

    @property
    def left(self) -> XAxisT:
        """
        Left.
        """

        return self.x

    @property
    def top(self) -> YAxisT:
        """
        Top
        """

        return self.y

    @property
    def x(self) -> XAxisT:
        """
        X coordinate.
        """

        return self.coordinates[0]

    @property
    def y(self) -> YAxisT:
        """
        Y coordinate.
        """

        return self.coordinates[1]


Point2T = TypeVar("Point2T", bound=Point2[Any, Any])
