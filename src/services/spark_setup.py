from pyspark.sql import SparkSession


class SparkInitializer:
    """
    The `SparkInitializer` class is a singleton class that initializes
    and provides access to a SparkSession object in PySpark.
    """

    __instance = None  # Singleton instance

    def __new__(
        cls, app_name: str = "MySparkApp", master: str = "local[*]", config: dict = None
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
        if not isinstance(app_name, str) or not isinstance(master, str):
            raise ValueError("app_name and master must be non-empty strings")
        if not app_name or not master:
            raise ValueError("app_name and master cannot be empty strings")
        if cls._instance is None:
            cls._instance = super(SparkInitializer, cls).__new__(cls)
            cls._instance = cls.init_spark_session(app_name, master, config)
        return cls._instance

    @staticmethod
    def init_spark_session(app_name: str, master: str, config):
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

        if not isinstance(config, dict):
            raise ValueError("config parameter must be a dictionary")

        spark = SparkSession.builder.appName(app_name).master(master)

        if config:
            for key, value in config.items():
                spark = spark.config(key, value)

        return spark.getOrCreate()

    @property
    def get_spark_session(self):
        """
        Returns the SparkSession object.

        Returns:
            SparkSession: The SparkSession object.
        """
        return self._instance
