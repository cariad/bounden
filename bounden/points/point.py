from typing import Any, cast

from bounden.points.types import AxesT, PointABC
from bounden.vectors import Vector


class Point(PointABC[AxesT]):
    """
    A point in n-dimensional space.

    `coordinates` describes the coordinates of the point.
    """

    def __init__(self, coordinates: AxesT) -> None:
        self._coordinates = coordinates

    def __add__(self, other: Any) -> "Point[AxesT]":
        if not isinstance(other, Vector):
            t = other.__class__.__name__
            raise ValueError(f"Can add only vectors (not {t}) to points")

        v: Vector[Any] = other

        if len(v) != len(self):
            raise ValueError(
                f"Vector force count ({len(v)}) != "
                f"point dimension count ({len(self)})"
            )

        cl = [c + v.lengths[i] for i, c in enumerate(self.coordinates)]
        return Point[AxesT](cast(AxesT, tuple(cl)))

    def __len__(self) -> int:
        return len(self._coordinates)

    @property
    def coordinates(self) -> AxesT:
        """
        Coordinates.
        """

        return self._coordinates
