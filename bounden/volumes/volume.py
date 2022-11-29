from typing import Any, Generic, TypeVar

from bounden.volumes.types import LengthsT


class Volume(Generic[LengthsT]):
    """
    An n-dimensional volume.

    `lengths` describes the length of each dimension.
    """

    def __init__(self, lengths: LengthsT) -> None:
        self._lengths = lengths

    def __len__(self) -> int:
        return len(self._lengths)

    @property
    def lengths(self) -> LengthsT:
        """
        Dimension lengths.
        """

        return self._lengths


VolumeT = TypeVar("VolumeT", bound=Volume[Any])
