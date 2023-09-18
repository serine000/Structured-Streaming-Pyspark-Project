import pytest
from pyspark.sql import SparkSession
from src.services.spark_setup import SparkInitializer


class TestSparkInitializer:
    # Initialize SparkSession with default parameters
    def test_initialize_spark_session_with_default_parameters(self):
        spark_initializer = SparkInitializer()
        spark_session = spark_initializer.get_spark_session
        assert isinstance(spark_session, SparkSession)
        assert spark_session.appName == "MySparkApp"
        assert spark_session.master == "local[*]"

    # Initialize SparkSession with custom parameters
    def test_initialize_spark_session_with_custom_parameters(self):
        # Create an instance of SparkInitializer with custom parameters
        spark_initializer = SparkInitializer(
            app_name="MyCustomApp",
            master="local[2]",
            config={"spark.executor.memory": "2g"},
        )

        # Get the SparkSession object
        spark_session = spark_initializer.get_spark_session

        # Check if the SparkSession object is not None
        assert spark_session is not None

        # Check if the application name is set correctly
        assert spark_session.conf.get("spark.app.name") == "MyCustomApp"

        # Check if the master URL is set correctly
        assert spark_session.conf.get("spark.master") == "local[2]"

        # Check if the additional configuration options are set correctly
        assert spark_session.conf.get("spark.executor.memory") == "2g"

    # Get existing SparkSession instance
    def test_get_existing_spark_session(self):
        # Create an instance of SparkInitializer
        spark_initializer = SparkInitializer()

        # Get the SparkSession object
        spark_session = spark_initializer.get_spark_session

        # Check if the SparkSession object is not None
        assert spark_session is not None

        # Check if the SparkSession object is an instance of SparkSession
        assert isinstance(spark_session, SparkSession)

    # Create multiple instances of SparkInitializer and get the same SparkSession object
    def test_multiple_instances_same_spark_session(self):
        # Create multiple instances of SparkInitializer
        spark_init_1 = SparkInitializer()
        spark_init_2 = SparkInitializer()

        # Get the SparkSession object from each instance
        spark_session_1 = spark_init_1.get_spark_session
        spark_session_2 = spark_init_2.get_spark_session

        # Check if both instances have the same SparkSession object
        assert spark_session_1 == spark_session_2

    # Create a new instance of SparkInitializer with default arguments
    def test_create_instance_with_default_arguments(self):
        spark_initializer = SparkInitializer()
        assert isinstance(spark_initializer, SparkInitializer)
        assert isinstance(spark_initializer.get_spark_session, SparkSession)
        assert spark_initializer.get_spark_session.appName == "MySparkApp"
        assert spark_initializer.get_spark_session.master == "local[*]"
        assert spark_initializer.get_spark_session.config == {}

    # Empty app_name parameter
    def test_empty_app_name_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer("", "local[*]")

    # Non-string master parameter
    def test_non_string_master_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer(master=123)

    # Empty master parameter
    def test_empty_master_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer(master="")
        with pytest.raises(ValueError):
            SparkInitializer(master=None)

    # Non-string app_name parameter
    def test_non_string_app_name_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer(123, "local[*]")

    # Non-dictionary config parameter
    def test_non_dictionary_config_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer("MySparkApp", "local[*]", "config")

    # Initialize SparkSession with invalid config parameter
    def test_initialize_spark_session_with_invalid_config_parameter(self):
        with pytest.raises(ValueError):
            SparkInitializer(config="invalid_config")

    # Create a new instance of SparkInitializer with empty app_name and master arguments
    def test_empty_app_name_and_master(self):
        with pytest.raises(ValueError):
            SparkInitializer("", "")

    # Create a new instance of SparkInitializer with non-string app_name and master arguments
    def test_create_instance_with_non_string_arguments(self):
        with pytest.raises(ValueError):
            SparkInitializer(123, "local[*]")
        with pytest.raises(ValueError):
            SparkInitializer("MySparkApp", 123)

    # Create a new instance of SparkInitializer with non-dictionary config argument
    def test_create_instance_with_non_dictionary_config(self):
        with pytest.raises(ValueError):
            SparkInitializer(config="not a dictionary")

    # Access the SparkSession object using get_spark_session property
    def test_access_spark_session(self):
        # Create an instance of SparkInitializer
        spark_initializer = SparkInitializer()

        # Access the SparkSession object using get_spark_session property
        spark_session = spark_initializer.get_spark_session

        # Check if the returned object is an instance of SparkSession
        assert isinstance(spark_session, SparkSession)

        # Check if the SparkSession object is not None
        assert spark_session is not None

    # Create a new instance of SparkInitializer with custom arguments
    def test_create_new_instance_with_custom_arguments(self):
        # Create a new instance of SparkInitializer with custom arguments
        spark_initializer = SparkInitializer(
            app_name="MyApp", master="local[2]", config={"key": "value"}
        )

        # Check if the instance is of type SparkInitializer
        assert isinstance(spark_initializer, SparkInitializer)

        # Check if the SparkSession object is not None
        assert spark_initializer.get_spark_session is not None

        # Check if the SparkSession object is of type SparkSession
        assert isinstance(spark_initializer.get_spark_session, SparkSession)

        # Check if the SparkSession object has the correct app name
        assert spark_initializer.get_spark_session.appName == "MyApp"

        # Check if the SparkSession object has the correct master URL
        assert spark_initializer.get_spark_session.master == "local[2]"

        # Check if the SparkSession object has the correct configuration
        assert spark_initializer.get_spark_session.conf.get("key") == "value"

    # Create a new instance of SparkInitializer with a non-existent configuration option
    def test_new_instance_with_nonexistent_config_option(self):
        with pytest.raises(ValueError):
            SparkInitializer(config={"nonexistent_option": "value"})

    # Create multiple instances of SparkInitializer and ensure they are the same object
    def test_multiple_instances_same_object(self):
        spark_init_1 = SparkInitializer()
        spark_init_2 = SparkInitializer()
        assert spark_init_1.get_spark_session == spark_init_2.get_spark_session

    # Check if SparkSession is a singleton object
    def test_spark_session_singleton(self):
        # Create two instances of SparkInitializer
        spark_init_1 = SparkInitializer()
        spark_init_2 = SparkInitializer()

        # Check if both instances refer to the same SparkSession object
        assert spark_init_1.get_spark_session == spark_init_2.get_spark_session

    # Check if SparkSession is created only once
    def test_spark_session_created_once(self):
        # Create two instances of SparkInitializer
        spark_init_1 = SparkInitializer()
        spark_init_2 = SparkInitializer()

        # Check if the SparkSession objects are the same
        assert spark_init_1.get_spark_session == spark_init_2.get_spark_session

    # Create a new instance of SparkInitializer with custom configuration options
    def test_create_instance_with_custom_config(self):
        config = {"spark.executor.memory": "2g", "spark.executor.cores": "4"}
        spark_initializer = SparkInitializer("MyApp", "local[*]", config)
        spark_session = spark_initializer.get_spark_session

        assert spark_session.appName == "MyApp"
        assert spark_session.master == "local[*]"
        assert spark_session.conf.get("spark.executor.memory") == "2g"
        assert spark_session.conf.get("spark.executor.cores") == "4"

    # Initialize SparkSession with additional configuration options
    def test_initialize_spark_session_with_config(self):
        config = {"spark.executor.memory": "2g", "spark.executor.cores": "4"}
        spark_initializer = SparkInitializer(config=config)
        spark_session = spark_initializer.get_spark_session
        assert spark_session.conf.get("spark.executor.memory") == "2g"
        assert spark_session.conf.get("spark.executor.cores") == "4"

    # Create a new instance of SparkInitializer with a SparkSession already initialized
    def test_create_instance_with_initialized_spark_session(self):
        # Create a SparkSession object
        spark = SparkSession.builder.appName("TestApp").master("local[*]").getOrCreate()

        # Create an instance of SparkInitializer
        spark_initializer = SparkInitializer()

        # Check if the SparkSession object is the same as the one in SparkInitializer
        assert spark_initializer.get_spark_session == spark

    # Check if SparkSession is initialized with correct parameters
    def test_spark_session_initialization(self):
        # Create an instance of SparkInitializer
        spark_initializer = SparkInitializer(
            app_name="TestApp",
            master="local[2]",
            config={"spark.executor.memory": "2g"},
        )

        # Get the SparkSession object
        spark_session = spark_initializer.get_spark_session

        # Check if the SparkSession object is not None
        assert spark_session is not None

        # Check if the SparkSession object has the correct application name
        assert spark_session.sparkContext.appName == "TestApp"

        # Check if the SparkSession object has the correct master URL
        assert spark_session.sparkContext.master == "local[2]"

        # Check if the SparkSession object has the correct configuration
        assert spark_session.conf.get("spark.executor.memory") == "2g"
