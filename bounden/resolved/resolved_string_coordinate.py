from rebelbase import Base26C

from bounden.resolved.resolved_coordinate import ResolvedCoordinate


class ResolvedStringCoordinate(ResolvedCoordinate[str]):
    """
    Resolved string coordinate.
    """

    def __float__(self) -> float:
        return float(Base26C(self._value))

    @classmethod
    def from_float(cls, f: float) -> "ResolvedStringCoordinate":
        return ResolvedStringCoordinate(str(Base26C(f)))
