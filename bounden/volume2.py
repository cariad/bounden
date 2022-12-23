from typing import Any, Optional, Type, TypeVar

from bounden.resolution import GetResolvedVolume
from bounden.resolved import ResolvedVolume
from bounden.types import Numeric, XLengthT, YLengthT
from bounden.volume import Volume


class Volume2(Volume[tuple[XLengthT, YLengthT]]):
    """
    A two-dimensional volume.
    """

    @classmethod
    def new(
        cls: Type["Volume2T"],
        width: XLengthT,
        height: YLengthT,
        within: Optional[GetResolvedVolume] = None,
    ) -> "Volume2T":
        """
        Creates a new `Volume2`.
        """

        return cls((width, height), within=within)

    @property
    def height(self) -> YLengthT:
        """
        Height.
        """

        return self.lengths[1]

    @property
    def width(self) -> XLengthT:
        """
        Width.
        """

        return self.lengths[0]


class ResolvedVolume2(ResolvedVolume[tuple[XLengthT, YLengthT]]):
    """
    A resolved two-dimensional volume.
    """

    def __init__(self, width: XLengthT, height: YLengthT) -> None:
        super().__init__((width, height))

    @property
    def height(self) -> Numeric:
        """
        Height.
        """

        return self[1]

    @classmethod
    def new(
        cls: Type["ResolvedVolume2T"],
        width: XLengthT,
        height: YLengthT,
    ) -> "ResolvedVolume2T":
        """
        Creates a new resolved two-dimensional volume.
        """

        return cls(width, height)

    @property
    def width(self) -> Numeric:
        """
        Width.
        """

        return self[0]


ResolvedVolume2T = TypeVar("ResolvedVolume2T", bound=ResolvedVolume2[Any, Any])
Volume2T = TypeVar("Volume2T", bound=Volume2[Any, Any])
