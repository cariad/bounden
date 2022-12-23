from typing import Any, Generic, Iterator

from bounden.log import log
from bounden.protocols import ResolvedVolumeProtocol
from bounden.resolve import resolved_length_to_numeric
from bounden.types import LengthsT, Numeric


class ResolvedVolume(ResolvedVolumeProtocol, Generic[LengthsT]):
    """
    A resolved n-dimensional volume.
    """

    def __init__(self, lengths: LengthsT) -> None:
        self._lengths = lengths

    def __eq__(self, other: Any) -> bool:
        return bool(list(self) == list(other))

    def __iter__(self) -> Iterator[Numeric]:
        for dimension in range(len(self._lengths)):
            yield self[dimension]

    def __getitem__(self, dimension: int) -> Numeric:
        length = self._lengths[dimension]
        log.debug(
            "The length of dimension %s is %s (%s)",
            dimension,
            length,
            length.__class__.__name__,
        )
        return resolved_length_to_numeric(length.resolved)

    def __repr__(self) -> str:
        return str(self._lengths)

    @property
    def lengths(self) -> LengthsT:
        return self._lengths
