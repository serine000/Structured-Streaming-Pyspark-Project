import os
import time
import json
import random
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer


# ENV variables
kafka_topic = os.getenv('KAFKA_TOPIC') #'first_python_topic'


# Serialize message as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        # Generate message 
        dummy_message = generate_message()

        # Send it to our topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send(kafka_topic, dummy_message)

        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)