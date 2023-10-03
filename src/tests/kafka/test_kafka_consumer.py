import json
import pytest
from kafka3 import KafkaConsumer


class TestKafkaConsumer:
    # Initialize SparkSession with default parameters
    def test_kafka_consumer(self):
        kafka_topic = "kafka_test_topic"
        consumer = KafkaConsumer(
            kafka_topic, bootstrap_servers="kafka:9092", auto_offset_reset="earliest"
        )

    for message in consumer:
        test_msg = message.value.decode("ascii")
    assert isinstance(test_msg, dict)
    assert len(test_msg) == 3
    assert isinstance(test_msg.get("user_id"), int)
    assert isinstance(test_msg.get("recipient_id"), int)
    assert isinstance(test_msg.get("message"), str)
