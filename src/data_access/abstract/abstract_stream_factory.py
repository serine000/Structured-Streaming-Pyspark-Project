from abc import ABC, abstractmethod


class StreamFactory(ABC):
    @abstractmethod
    def fetch_stream_source(self, *args):
        pass

    def fetch_stream_sink(self, *args):
        pass
