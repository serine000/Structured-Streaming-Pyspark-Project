import pytest
from pyspark.sql import SparkSession


class TestSparkInitializer:
    # Create a new instance of SparkInitializer with default arguments.
    def test_create_instance_with_default_arguments(self):
        spark_initializer = SparkInitializer()
        assert isinstance(spark_initializer, SparkInitializer)
        assert isinstance(spark_initializer.get_spark_session, SparkSession)

    # Create a new instance of SparkInitializer with custom arguments.
    def test_create_instance_with_custom_arguments(self):
        app_name = "MyCustomApp"
        master = "local[2]"
        config = {"spark.executor.memory": "2g"}

        spark_initializer = SparkInitializer(app_name, master, config)

        assert spark_initializer.get_spark_session.appName == app_name
        assert spark_initializer.get_spark_session.master == master
        assert (
            spark_initializer.get_spark_session.conf.get("spark.executor.memory")
            == "2g"
        )

    # Create a new instance of SparkInitializer with an invalid config parameter.
    def test_invalid_config_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer(config="invalid_config")

    # Create multiple instances of SparkInitializer and ensure they are the same object.
    def test_multiple_instances_same_object(self):
        spark_init_1 = SparkInitializer()
        spark_init_2 = SparkInitializer()
        assert spark_init_1 is spark_init_2

    # Access the SparkSession object using the get_spark_session property.
    def test_access_spark_session(self):
        # Create an instance of SparkInitializer
        spark_initializer = SparkInitializer()

        # Access the SparkSession object using the get_spark_session property
        spark_session = spark_initializer.get_spark_session

        # Check if the returned object is an instance of SparkSession
        assert isinstance(spark_session, SparkSession)

        # Check if the SparkSession object is not None
        assert spark_session is not None

    # Create a new instance of SparkInitializer with an invalid app name.
    def test_invalid_app_name(self):
        with pytest.raises(ValueError):
            SparkInitializer(app_name=123)

    # Create a new instance of SparkInitializer with additional configuration options.
    def test_create_instance_with_config_options(self):
        config = {"spark.executor.memory": "2g", "spark.executor.cores": "4"}
        spark_initializer = SparkInitializer(config=config)
        spark_session = spark_initializer.get_spark_session

        assert spark_session is not None
        assert spark_session.conf.get("spark.executor.memory") == "2g"
        assert spark_session.conf.get("spark.executor.cores") == "4"

    # Create a new instance of SparkInitializer with a custom SparkSession object.
    def test_create_instance_with_custom_spark_session(self):
        # Create a custom SparkSession object
        custom_spark = (
            SparkSession.builder.appName("CustomApp").master("local[2]").getOrCreate()
        )

        # Create a new instance of SparkInitializer with the custom SparkSession object
        spark_initializer = SparkInitializer(
            app_name="MySparkApp", master="local[*]", config=None
        )
        spark_initializer._spark = custom_spark

        # Check if the SparkSession object in SparkInitializer is the same as the custom SparkSession object
        assert spark_initializer.get_spark_session == custom_spark

    # Create a new instance of SparkInitializer with a non-local master URL.
    def test_create_instance_with_non_local_master_url(self):
        spark_initializer = SparkInitializer(master="spark://localhost:7077")
        assert spark_initializer.get_spark_session.master == "spark://localhost:7077"

    # Create a new instance of SparkInitializer with a custom SparkSession object that has already been stopped.
    def test_custom_spark_session_stopped(self):
        # Create a custom SparkSession object that has already been stopped
        spark = (
            SparkSession.builder.appName("CustomSparkApp")
            .master("local[*]")
            .getOrCreate()
        )
        spark.stop()

        # Create a new instance of SparkInitializer with the custom SparkSession object
        initializer = SparkInitializer(
            config={"spark.driver.allowMultipleContexts": "true"}
        )
        spark_session = initializer.get_spark_session

        # Assert that the returned SparkSession object is not None
        assert spark_session is not None

        # Assert that the returned SparkSession object is the same as the custom SparkSession object
        assert spark_session == spark
