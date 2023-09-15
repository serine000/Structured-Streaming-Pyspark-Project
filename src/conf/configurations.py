from data_access.repository.stream_factories.kafka_stream_factory import (
    KafkaStreamFactory,
)


general_configs = {
    "input_stream": "kafka",
    "kafka": KafkaStreamFactory(),
}

kafka_configs = {
    "kafka_bootstrap_servers": 1,
    "kafka_format": "",
    "kafka_topic_subscribe": "",
    "kafka_starting_offset": 3,
}
