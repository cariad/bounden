from typing import Generic

from bounden.vectors.types import LengthsT


class Vector(Generic[LengthsT]):
    """
    An n-dimensional vector.

    `lengths` describes the length of the vector in each dimension. The index
    indicates the dimension and the value describes the length.
    """

    def __init__(self, lengths: LengthsT) -> None:
        self._lengths = lengths

    def __len__(self) -> int:
        return len(self._lengths)

    @property
    def lengths(self) -> LengthsT:
        """
        Length of the vector in each dimension.

        The index indicates the dimension and the value describes the length.
        """

        return self._lengths
