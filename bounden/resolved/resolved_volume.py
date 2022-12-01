from typing import Any, Iterator


class ResolvedVolume:
    """
    Resolved volume.
    """

    def __init__(self, *lengths: float | int) -> None:
        self._lengths = lengths

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ResolvedVolume):
            return bool(list(self) == list(other))

        return bool(self._lengths == other)

    def __getitem__(self, dimension: int) -> float | int:
        return self._lengths[dimension]

    def __iter__(self) -> Iterator[float | int]:
        return iter(self._lengths)

    def __repr__(self) -> str:
        return str(self._lengths)
