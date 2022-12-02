from typing import Any, Optional, Type, TypeVar

from bounden.axes import Axes, XAxisT, YAxisT
from bounden.points import Point2
from bounden.protocols import RegionProtocol
from bounden.regions import Region
from bounden.volumes import Percent


class Region2(Region[tuple[XAxisT, YAxisT]]):
    """
    A region of two-dimensional space.
    """

    @classmethod
    def new(
        cls: Type["Region2T"],
        x: XAxisT,
        y: YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
        axes_resolver: Optional[Axes] = None,
        parent: Optional[RegionProtocol] = None,
    ) -> "Region2T":
        """
        Creates a new `Region2`.
        """

        return cls(
            (x, y),
            (width, height),
            axes_resolver=axes_resolver,
            parent=parent,
        )

    @property
    def bottom(self) -> YAxisT:
        """
        Bottom.
        """

        axis = self._axes.get(self.top)
        return axis.add(self.top, self.height)

    @property
    def height(self) -> float | int:
        """
        Height.
        """

        return self.volume.absolute(1)

    @property
    def left(self) -> XAxisT:
        """
        Left.
        """

        return self.x

    def point2(self, x: XAxisT, y: YAxisT) -> Point2[XAxisT, YAxisT]:
        """
        Creates a child point.
        """

        return Point2.new(x, y, parent=self)

    def region2(
        self: "Region2T",
        x: XAxisT,
        y: YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
    ) -> "Region2T":
        """
        Creates a child region.
        """

        return self.__class__.new(x, y, width, height, parent=self)

    @property
    def right(self) -> XAxisT:
        """
        Right.
        """

        axis = self._axes.get(self.left)
        return axis.add(self.left, self.width)

    @property
    def top(self) -> YAxisT:
        """
        Top.
        """

        return self.y

    @property
    def width(self) -> float | int:
        """
        Width.
        """

        return self.volume.absolute(0)

    @property
    def x(self) -> XAxisT:
        """
        X coordinate.
        """

        return self.position.coordinates[0]

    @property
    def y(self) -> YAxisT:
        """
        Y coordinate.
        """

        return self.position.coordinates[1]


Region2T = TypeVar("Region2T", bound=Region2[Any, Any])
