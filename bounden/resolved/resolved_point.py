from typing import Any, Generic, Iterator, List, TypeVar

from bounden.protocols import ResolvedPointProtocol
from bounden.types import AxisPosition, CoordinatesT
from bounden.vectors import get_vector_length


class ResolvedPoint(ResolvedPointProtocol, Generic[CoordinatesT]):
    """
    A resolved point in n-dimensional space.
    """

    def __init__(self, coordinates: CoordinatesT) -> None:
        self._coordinates = coordinates

    def __add__(self: "ResolvedPointT", other: Any) -> "ResolvedPointT":
        coords: List[AxisPosition[Any]] = []
        for dimension, coordinate in enumerate(self._coordinates):
            length = get_vector_length(other, dimension)
            coords.append(coordinate + length)

        return self.__class__(coords)

    def __eq__(self, other: Any) -> bool:
        return list(self) == list(other)

    def __getitem__(self, dimension: int) -> Any:
        return self._coordinates[dimension]

    def __iter__(self) -> Iterator[Any]:
        return iter(self._coordinates)

    def __repr__(self) -> str:
        return repr(self._coordinates)

    def __sub__(self: "ResolvedPointT", other: Any) -> "ResolvedPointT":
        coords: List[AxisPosition[Any]] = []
        for dimension, coordinate in enumerate(self._coordinates):
            length = get_vector_length(other, dimension)
            coords.append(coordinate - length)

        return self.__class__(coords)

    @property
    def coordinates(self) -> CoordinatesT:
        """
        Coordinates.
        """

        return self._coordinates


ResolvedPointT = TypeVar("ResolvedPointT", bound=ResolvedPoint[Any])
