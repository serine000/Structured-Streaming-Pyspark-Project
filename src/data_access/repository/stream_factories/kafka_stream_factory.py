from pyspark.sql import SparkSession
from data_access.abstract.abstract_stream_factory import StreamFactory
from data_access.repository.stream_ports.stream_sinks.kafka_sink_port import (
    KafkaSinkPort,
)
from data_access.repository.stream_ports.stream_sources.kafka_source_port import (
    KafkaSourcePort,
)


class KafkaStreamFactory(StreamFactory):
    def fetch_stream_source(self) -> KafkaSourcePort:
        """
        Returns an instance of the KafkaSourcePort class.
        """
        return KafkaSourcePort()

    def fetch_stream_sink(self) -> KafkaSinkPort:
        """
        Returns an instance of the KafkaSinkPort class.
        """
        return KafkaSinkPort()
