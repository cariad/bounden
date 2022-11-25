from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

AxesT = TypeVar("AxesT", bound=tuple[Any, ...])
LengthsT = TypeVar("LengthsT", bound=tuple[float, ...])
"""
The dimensions of a region (e.g. width and height).
"""

XAxisT = TypeVar("XAxisT")
YAxisT = TypeVar("YAxisT")

XLengthT = TypeVar("XLengthT", bound=float)
YLengthT = TypeVar("YLengthT", bound=float)


class PointABC(ABC, Generic[AxesT]):
    """
    Abstract base point.
    """

    @abstractmethod
    def __len__(self) -> int:
        """
        Gets the number of coordinates that describe this position.
        """


PointT = TypeVar("PointT", bound=PointABC[Any])
