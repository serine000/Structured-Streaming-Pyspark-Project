from pyspark.sql import SparkSession


class SparkInitializer:
    """
    The `SparkInitializer` class is a singleton class that initializes
    and provides access to a SparkSession object in PySpark.
    """

    __instance = None

    def __new__(
        cls,
        app_name: str = "MySparkApp",
        master: str = "local[*]",
        config: dict = None,
    ):
        """
        Creates a new instance of the class if it doesn't already exist.
        Initializes the SparkSession object by calling the `init_spark_session` method.

        Args:
            app_name (str): The name of the Spark application.
            master (str): The master URL for the Spark application.
            config (dict): Additional configuration options for the SparkSession.

        Returns:
            SparkInitializer: The singleton instance of the class.
        """
        if cls.__instance is None:
            cls.__instance = super(SparkInitializer, cls).__new__(cls)
        return cls.__instance

    def __init__(
        self,
        app_name: str = "MySparkApp",
        master: str = "local[*]",
        config: dict = None,
    ):
        self._spark_session = self.init_spark_session(app_name, master, config)

    @staticmethod
    def init_spark_session(app_name: str, master: str, config: dict = None):
        """
        Initializes the SparkSession object with the provided application name and master URL.
        Allows additional configuration options to be passed through the `config` parameter.

        Args:
            app_name (str): The name of the Spark application.
            master (str): The master URL for the Spark application.
            config (dict): Additional configuration options for the SparkSession.

        Returns:
            SparkSession: The initialized SparkSession object.
        """

        spark = SparkSession.builder.appName(app_name).master(master)

        if config:
            for key, value in config.items():
                spark = spark.config(key, value)

        return spark.getOrCreate()

    @property
    def spark_session(self):
        """
        Returns the SparkSession object.

        Returns:
            SparkSession: The SparkSession object.
        """
        return self._spark_session
