from pyspark.sql import SparkSession


from data_access.abstract.abstract_stream_port import StreamPort


class KafkaSinkPort(StreamPort):
    def create_stream(self, spark_session: SparkSession, conf):
        pass
