from pyspark.sql import SparkSession


from conf.configuration_manager import ConfigurationManager

conf_manager = ConfigurationManager()


def fetch_stream_source(spark_session: SparkSession):
    source_stream_port: str = conf_manager.get_general_configuration("input_stream")
    chosen_input_stream: StreamFactory = conf_manager.get_general_configuration(
        source_stream_port
    )

    input_stream = chosen_input_stream.fetch_stream_source().create_stream(
        spark_session, conf_manager
    )
    print(input_stream)
    return input_stream


def fetch_stream_sink(spark_session: SparkSession):
    sink_stream_port: str = conf_manager.get_general_configuration("output_stream")
    chosen_output_stream: StreamFactory = conf_manager.get_general_configuration(
        sink_stream_port
    )

    output_stream = chosen_output_stream.fetch_stream_sink().create_stream(
        spark_session, conf_manager
    )
    print(output_stream)
    return output_stream
