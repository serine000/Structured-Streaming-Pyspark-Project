from abc import ABC, abstractclassmethod

class AbstractStreamPort(ABC):
    """
    Abstract base class for creating stream ports.
    """

    @classmethod
    def create_stream_port(self, *args):
        """
        Creates a stream port.
        """
        pass