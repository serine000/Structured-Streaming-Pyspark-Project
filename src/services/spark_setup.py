from pyspark.sql import SparkSession

class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SparkInitializer(metaclass=SingletonMeta):
    """
    The `SparkInitializer` class is a singleton class that initializes
    and provides access to a SparkSession object in PySpark.
    """

    def __init__(self, app_name="MySparkApp", master="local[*]", config=None):
        """
        Initializes the SparkSession object by calling the `init_spark_session` method.

        Args:
            app_name (str): The name of the Spark application.
            master (str): The master URL for the Spark application.
            config (dict): Additional configuration options for the SparkSession.
        """
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
            if not isinstance(config, dict):
                raise ValueError("config parameter must be a dictionary")
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
