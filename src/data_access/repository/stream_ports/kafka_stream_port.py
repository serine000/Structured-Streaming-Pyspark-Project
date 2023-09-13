from data_access.abstract.abstract_stream_port import AbstractStreamPort

class KafkaStreamPort(AbstractStreamPort):
    """
    A class that creates a kafka stream port.
    """

    def create_stream_port(self):
        """
        Creates and returns a Kafka Port Object.
        """
        return 1