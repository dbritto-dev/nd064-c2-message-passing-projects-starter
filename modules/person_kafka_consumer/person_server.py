# Built-in packages
import json

# Third-party packages
from kafka.consumer.fetcher import ConsumerRecord

# Local packages
from person_kafka import brk
from person_service import PersonService


class Server:
    def run(self) -> None:
        for message in brk.kafka_consumer:
            try:
                person_create_dto = json.loads(bytes(message.value).decode("utf-8"))
                _ = PersonService.create(person_create_dto)
            except Exception as e:
                pass
