from typing import Any, Generic, Iterator, List, Optional, Sequence, cast

from bounden.axes import Axes, AxesT, AxisOperation, axes
from bounden.protocols import RegionProtocol


class Point(Generic[AxesT]):
    """
    A point in n-dimensional space.
    """

    def __init__(
        self,
        coordinates: AxesT,
        axes_resolver: Optional[Axes] = None,
        parent: Optional[RegionProtocol] = None,
    ) -> None:
        self._axes = axes_resolver or axes
        self._coordinates = coordinates
        self._parent = parent

    def __add__(self, other: Any) -> "Point[AxesT]":
        return self._operate(other, AxisOperation.Add)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Point):
            o: Point[Any] = other
            return bool(self.coordinates == o.coordinates)

        return bool(self.coordinates == other)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._coordinates)

    def __len__(self) -> int:
        return len(self._coordinates)

    def __repr__(self) -> str:
        return str(self._coordinates)

    def __sub__(self, other: Any) -> "Point[AxesT]":
        return self._operate(other, AxisOperation.Subtract)

    def _operate(self, vector: Any, op: AxisOperation) -> "Point[AxesT]":
        """
        Returns a new point based on the `op` between this and `vector`.
        """

        translated_coords: List[Any] = []

        for index, point_coord in enumerate(self._coordinates):
            axis = self._axes.get(point_coord)
            vector_coord = self._vector(vector, index)
            result = axis.operate(point_coord, vector_coord, op)
            translated_coords.append(result)

        point = cast(AxesT, tuple(translated_coords))
        return Point[AxesT](point, parent=self._parent)

    def _vector(self, vector: Any, dimension: int) -> float:
        """
        Gets the `vector` force of `dimension`.
        """

        if isinstance(vector, (float, int)):
            return vector

        if isinstance(vector, (list, tuple)):
            return cast(Sequence[float], vector)[dimension]

        raise ValueError(f"{repr(vector)} ({type(vector)}) is not a vector")

    @property
    def coordinates(self) -> AxesT:
        """
        Coordinates.
        """

        return self._coordinates
