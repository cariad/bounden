from typing import Any, Iterator

from bounden.protocols import ResolvedVolumeProtocol
from bounden.resolve import resolved_length_to_numeric
from bounden.types import Numeric, ResolvedLength


class ResolvedVolume(ResolvedVolumeProtocol):
    """
    A resolved n-dimensional volume.
    """

    def __init__(self, *lengths: ResolvedLength) -> None:
        self._lengths = lengths

    def __eq__(self, other: Any) -> bool:
        return bool(list(self) == list(other))

    def __iter__(self) -> Iterator[Numeric]:
        for dimension in range(len(self._lengths)):
            yield self[dimension]

    def __getitem__(self, dimension: int) -> Numeric:
        return resolved_length_to_numeric(self._lengths[dimension])

    def __repr__(self) -> str:
        return str(self._lengths)
