from pyspark.sql import SparkSession
from data_access.abstract.abstract_stream_port import StreamPort


class KafkaSourcePort(StreamPort):
    def create_stream(self, spark_session: SparkSession, conf):
        return 1
        # try:
        #     read_stream = (
        #         spark_session.readStream.format(kafka_settings.get("kafka_format"))
        #         .option(
        #             "kafka.bootstrap.servers",
        #             kafka_settings.get("kafka_bootstrap_servers"),
        #         )
        #         .option(
        #             "subscribe",
        #             kafka_settings.get("kafka_topic_subscribe"),
        #         )
        #         .option(
        #             "startingOffsets",
        #             kafka_settings.get("kafka_starting_offset"),
        #         )
        #         .load()
        #     )
        #     return read_stream
        # except ConnectionError:
        #     raise Exception("Could not connect to kafka")
