# Built-in packages
import json

# Third-party packages
from flask import g
from kafka import KafkaProducer

# Local packages
from person_database import db
from person_dto import PersonCreateDTO
from person_model import PersonModel
from person_kafka import KAFKA_TOPIC


class PersonRepository:
    @staticmethod
    def create(person_create_dto: PersonCreateDTO) -> PersonModel:
        kafka_data = json.dumps(person_create_dto).encode()
        kafka_producer: KafkaProducer = g.kafka_producer
        kafka_producer.send(KAFKA_TOPIC, kafka_data)

    @staticmethod
    def retrieve(person_id: int) -> PersonModel:
        return db.session.query(PersonModel).get(person_id)

    @staticmethod
    def retrieve_all() -> list[PersonModel]:
        return db.session.query(PersonModel).all()
