import random
import string
import time
import json
from datetime import datetime
from kafka3 import KafkaProducer

user_ids = list(range(1, 10))
recipients_ids = list(range(1, 10))


def generate_data() -> dict:
    random_user_id = random.choice(user_ids)

    recipients_list_copy = recipients_ids.copy()
    recipients_list_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipients_list_copy)

    message = "".join(random.choice(string.ascii_letters) for i in range(32))

    return {
        "user_id": random_user_id,
        "recipient_id": random_recipient_id,
        "message": message,
    }


def serializer(message):
    return json.dumps(message).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=["localhost:29092"], value_serializer=serializer
)

if __name__ == "__main__":
    dummy_msg = generate_data()
    kafka_topic = "kafka_test_topic"
    producer.send(kafka_topic, dummy_msg)
