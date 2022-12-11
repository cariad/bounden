from typing import Any, Protocol

from bounden.types import Numeric


class ResolvedPointProtocol(Protocol):
    """
    A resolved point in n-dimensional space.
    """

    def __getitem__(self, dimension: int) -> Any:
        ...  # pragma: nocover


class ResolvedVolumeProtocol(Protocol):
    """
    A resolved n-dimensional volume.
    """

    def __getitem__(self, dimension: int) -> Numeric:
        ...  # pragma: nocover
