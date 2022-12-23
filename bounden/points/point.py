from __future__ import annotations

from typing import (
    Any,
    Generic,
    Iterator,
    List,
    Optional,
    Sequence,
    TypeVar,
    cast,
)

from bounden.enums import Alignment
from bounden.log import log
from bounden.resolution import GetResolvedVolume, RegionResolver
from bounden.resolved import ResolvedPoint
from bounden.types import AxisPosition, CoordinatesT
from bounden.vectors import get_vector_length  # transform_coordinates


class Point(Generic[CoordinatesT]):
    """
    A point in n-dimensional space.
    """

    def __init__(
        self,
        coordinates: CoordinatesT,
        origin_of: Optional[GetResolvedVolume] = None,
        within: Optional[RegionResolver] = None,
    ) -> None:
        self._coordinates = coordinates
        self._origin_of = origin_of
        self._within = within

    def __add__(self: "PointT", other: Any) -> "PointT":
        coords: List[AxisPosition[Any]] = []
        for dimension, coordinate in enumerate(self._coordinates):
            length = get_vector_length(other, dimension)
            coords.append(coordinate + length)

        return self._respawn(coords)

    def __eq__(self, other: Any) -> bool:
        return list(self) == list(other)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.coordinates)

    def __len__(self) -> int:
        return len(self._coordinates)

    def __repr__(self) -> str:
        return str(self._coordinates)

    def __sub__(self, other: Any) -> Point[CoordinatesT]:
        coords: List[AxisPosition[Any]] = []
        for dimension, coordinate in enumerate(self._coordinates):
            length = get_vector_length(other, dimension)
            coords.append(coordinate - length)

        return self._respawn(coords)

    def _respawn(self: PointT, coords: Sequence[AxisPosition[Any]]) -> PointT:
        return self.__class__(
            coords,
            origin_of=self._origin_of,
            within=self._within,
        )

    @property
    def coordinates(self) -> CoordinatesT:
        """
        Coordinates.
        """

        return self._coordinates

    def resolve(self) -> ResolvedPoint[CoordinatesT]:
        translated_coords: List[Any] = []

        for dimension, coordinate in enumerate(self._coordinates):
            if isinstance(coordinate, Alignment):
                if self._within is None:
                    raise ValueError(  # pragma: nocover
                        f"{self.__class__.__name__} cannot resolve alignment "
                        f"{coordinate.name} without a parent region"
                    )

                within_offset = self._within.position()[dimension]

                match coordinate.value:
                    case Alignment.Near:
                        translated_coords.append(within_offset)

                    case Alignment.Center:
                        # axis = self._axes[dimension]
                        distance = coordinate.to_decimal(within_offset)

                        within_len = self._within.volume()[dimension]
                        distance += within_len / 2

                        if self._origin_of is not None:
                            distance -= self._origin_of()[dimension] / 2

                        translated_coords.append(coordinate.to_value(distance))

                    case Alignment.Far:
                        # axis = self._axes[dimension]
                        distance = coordinate.to_decimal(within_offset)

                        within_len = self._within.volume()[dimension]
                        distance += within_len

                        if self._origin_of:
                            distance -= self._origin_of()[dimension]

                        translated_coords.append(coordinate.to_value(distance))

                    case _:  # pragma: nocover
                        m = f"Unrecognised alignment {repr(coordinate.value)}"
                        raise ValueError(m)

            else:
                translated = coordinate

                if self._within is not None:
                    within_origin = self._within.position()
                    translated = coordinate + within_origin[dimension]

                translated_coords.append(translated)

        resolved_point = cast(CoordinatesT, tuple(translated_coords))
        log.debug("Resolved %s to %s", self, resolved_point)
        return ResolvedPoint(resolved_point)


PointT = TypeVar("PointT", bound=Point[Any])
