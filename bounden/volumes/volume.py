from typing import Any, Generic, Iterator, TypeVar

from bounden.volumes.types import Length, LengthsT


class Volume(Generic[LengthsT]):
    """
    An n-dimensional volume.

    `lengths` describes the length of each dimension.
    """

    def __init__(self, lengths: LengthsT) -> None:
        self._lengths = lengths

    def __iter__(self) -> Iterator[Length]:
        for length in self._lengths:
            yield length

    def __len__(self) -> int:
        return len(self._lengths)

    @property
    def lengths(self) -> LengthsT:
        """
        Dimension lengths.
        """

        return self._lengths


VolumeT = TypeVar("VolumeT", bound=Volume[Any])
