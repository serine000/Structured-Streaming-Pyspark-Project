from pyspark.sql import SparkSession

from services.create_stream_ports import fetch_stream_sink, fetch_stream_source
from services.spark_setup import SparkInitializer


def main():
    spark_session = SparkSession.builder.appName("KafkaStreamExample").getOrCreate()
    print(spark_session)
    input_stream_source = fetch_stream_source(spark_session)
    # output_stream_source = fetch_stream_sink()

    print(input_stream_source)


if __name__ == "__main__":
    main()
