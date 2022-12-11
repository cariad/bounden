from typing import Optional, Type, TypeVar

from bounden.resolution import GetResolvedVolume
from bounden.resolved import ResolvedVolume
from bounden.types import Length, Numeric, ResolvedLength
from bounden.volume import Volume


class Volume2(Volume):
    """
    A two-dimensional volume.
    """

    @classmethod
    def new(
        cls: Type["Volume2T"],
        width: Length,
        height: Length,
        within: Optional[GetResolvedVolume] = None,
    ) -> "Volume2T":
        """
        Creates a new `Volume2`.
        """

        return cls(width, height, within=within)

    @property
    def height(self) -> Length:
        """
        Height.
        """

        return self[1]

    @property
    def width(self) -> Length:
        """
        Width.
        """

        return self[0]


class ResolvedVolume2(ResolvedVolume):
    """
    A resolved two-dimensional volume.
    """

    @property
    def height(self) -> Numeric:
        """
        Height.
        """

        return self[1]

    @classmethod
    def new(
        cls: Type["ResolvedVolume2T"],
        width: ResolvedLength,
        height: ResolvedLength,
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


ResolvedVolume2T = TypeVar("ResolvedVolume2T", bound=ResolvedVolume2)
Volume2T = TypeVar("Volume2T", bound=Volume2)
