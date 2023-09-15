from abc import ABC, abstractmethod


class StreamPort(ABC):
    @abstractmethod
    def create_stream(self, *args):
        """
        Create a stream sink.

        This method is meant to be overridden by
        subclasses to create a stream sink.
        """
        pass
