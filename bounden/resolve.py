from typing import SupportsFloat

from vinculum import Rational

from bounden.types import Numeric, ResolvedLength


def resolved_length_to_numeric(length: ResolvedLength) -> Numeric:
    """
    Resolves `length` to a numeric value.
    """

    if isinstance(length, (float, int, Rational)):
        return length

    if isinstance(length, SupportsFloat):
        return float(length)

    return int(length)
