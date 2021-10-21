# Built-in packages
import os

# Third-party packages
from kafka import KafkaConsumer

# Local packages

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")


class Broker:
    kafka_consumer: KafkaConsumer = None

    def init_kafka_consumer(self):
        print(KAFKA_TOPIC, KAFKA_SERVER)
        self.kafka_consumer = KafkaConsumer(
            KAFKA_TOPIC,
            group_id="person-api-kafka-consumer",
            bootstrap_servers=KAFKA_SERVER,
        )


brk = Broker()


def register_kafka() -> None:
    brk.init_kafka_consumer()
