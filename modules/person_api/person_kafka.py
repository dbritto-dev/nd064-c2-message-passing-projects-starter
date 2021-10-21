# Built-in packages
import os

# Third-party packages
from flask import g, Flask
from kafka import KafkaProducer

# Local packages

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")


def register_kafka(app: Flask) -> None:
    @app.before_request
    def _before_request() -> None:  # noqa
        g.kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
