from typing import Any, Iterator, List, Optional, TypeVar

from bounden.resolution.types import GetResolvedVolume
from bounden.resolve import resolved_length_to_numeric
from bounden.resolved import ResolvedVolume
from bounden.types import Length, Numeric, Percent


class Volume:
    """
    An n-dimensional volume.

    `lengths` describes the length of each dimension.
    """

    def __init__(
        self,
        *lengths: Length,
        within: Optional[GetResolvedVolume] = None,
    ) -> None:
        self._lengths = lengths
        self._within = within
        self._resolved: Optional[ResolvedVolume] = None

    def __eq__(self, other: Any) -> bool:
        return bool(list(self) == list(other))

    def __getitem__(self, dimension: int) -> Length:
        return self._lengths[dimension]

    def __iter__(self) -> Iterator[Length]:
        return iter(self._lengths)

    def __len__(self) -> int:
        return len(self._lengths)

    def __repr__(self) -> str:
        return str(self._lengths)

    def resolve(self) -> ResolvedVolume:
        """
        Resolves relative lengths to absolute.
        """

        if self._resolved is None:
            lengths: List[Numeric] = []

            for index, length in enumerate(self._lengths):
                if isinstance(length, Percent):
                    within = self._within() if self._within else None
                    if within is None:
                        raise ValueError(
                            f"{self.__class__.__name__} {self} has no "
                            "parent so cannot fit to volume"
                        )
                    within_length = within[index]
                    resolved_length = length.calculate(within_length)

                else:
                    resolved_length = resolved_length_to_numeric(length)

                lengths.append(resolved_length)

            self._resolved = ResolvedVolume(*lengths)

        return self._resolved

    def volume(self: "VolumeT", *lengths: float | int | Percent) -> "VolumeT":
        """
        Creates and returns a child volume.
        """

        return self.__class__(*lengths, within=self.resolve)


VolumeT = TypeVar("VolumeT", bound=Volume)
