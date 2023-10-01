from conf.configurations import kafka_configs, general_configs


class ConfigurationManager:
    @classmethod
    def get_kafka_configuration(cls, key: str):
        return kafka_configs.get(key, "")

    @classmethod
    def get_general_configuration(cls, key: str):
        return general_configs.get(key, "")
