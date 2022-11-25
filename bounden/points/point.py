from typing import Generic

from bounden.points.types import CoordinatesT


class Point(Generic[CoordinatesT]):
    """
    A point within an n-dimensional volume.
    """

    def __init__(self, value: CoordinatesT) -> None:
        self._value = value

    @property
    def value(self) -> CoordinatesT:
        """
        Coordinates.
        """

        return self._value
