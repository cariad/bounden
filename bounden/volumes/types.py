from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

Length = float | int

LengthsT = TypeVar("LengthsT", bound=tuple[Length, ...])
"""
The dimensions of a region (e.g. width and height).
"""


class VolumeABC(ABC, Generic[LengthsT]):
    """
    Abstract base size.
    """

    @abstractmethod
    def __len__(self) -> int:
        """
        Gets the number of lengths that describe this volume.
        """


VolumeT = TypeVar("VolumeT", bound=VolumeABC[Any])

XLengthT = TypeVar("XLengthT", bound=Length)
YLengthT = TypeVar("YLengthT", bound=Length)
