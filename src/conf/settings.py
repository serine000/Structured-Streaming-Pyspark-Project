from typing import Dict

from pydantic import BaseModel

from data_access.repository.stream_ports.kafka_stream_port import KafkaStreamPort
from data_access.abstract.abstract_stream_port import AbstractStreamPort

# def get_stream_options():
#     return {
#         "kafka": KafkaStreamPort(),
#         #"mongo": MongoStreamPort(),
#     } 
# class Settings(BaseModel):
#     stream_options: Dict[str, AbstractStreamPort] = get_stream_options()
#     input_stream: str = "kafka"


settings = {
        "input_stream": "kafka",
        "kafka": KafkaStreamPort(),
         #"mongo": MongoStreamPort(),
     } 