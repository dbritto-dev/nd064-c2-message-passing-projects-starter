# Built-in packages

# Third-party packages

# Local packages
from person_database import db
from person_dto import PersonCreateDTO
from person_model import PersonModel
from person_schema import PersonSchema


class PersonRepository:
    @staticmethod
    def create(person_create_dto: PersonCreateDTO) -> PersonModel:
        person = PersonSchema(load_instance=True).load(
            person_create_dto, session=db.session
        )

        db.session.add(person)
        db.session.commit()

        return person
