from typing import Protocol

from bounden.protocols.volume import VolumeProtocol


class RegionProtocol(Protocol):
    """
    Region protocol.
    """

    @property
    def volume(self) -> VolumeProtocol:
        """
        Volume.
        """
