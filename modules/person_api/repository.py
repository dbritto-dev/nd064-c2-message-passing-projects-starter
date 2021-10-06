# Built-in packages

# Third-party packages

# Local packages
from dto import PersonCreateDTO
from model import Person
from database import db
from schema import PersonSchema


class PersonRepository:
    @staticmethod
    def create(person_create_dto: PersonCreateDTO) -> Person:
        person = PersonSchema().load(person_create_dto)

        db.session.add(person)
        db.session.commit()

        return person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        return db.session.query(Person).get(person_id)

    @staticmethod
    def retrieve_all() -> list[Person]:
        return db.session.query(Person).all()
