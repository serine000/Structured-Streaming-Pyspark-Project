import json
import pytest
from kafka3 import KafkaConsumer


class TestKafkaConsumer:
    def setup_method(self):
        kafka_topic = "kafka_test_topic"
        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers="localhost:29092",
            auto_offset_reset="earliest",
        )
        for message in consumer:
            self._test_msg = json.loads(message.value.decode("ascii"))
            break

    # Initialize SparkSession with default parameters
    def test_kafka_consumer(self):
        assert isinstance(self._test_msg, dict)
        assert len(self._test_msg) == 3
        assert isinstance(self._test_msg.get("user_id"), int)
        assert isinstance(self._test_msg.get("recipient_id"), int)
        assert isinstance(self._test_msg.get("message"), str)
