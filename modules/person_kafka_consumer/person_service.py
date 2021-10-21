# Built-in packages

# Third-party packages
from werkzeug.exceptions import BadRequest

# Local packages
from person_database import db
from person_model import PersonModel
from person_schema import PersonSchema
from person_dto import PersonCreateDTO
from person_repository import PersonRepository


class PersonService:
    @staticmethod
    def create(person_create_dto: PersonCreateDTO) -> PersonModel:
        validation_results = PersonSchema().validate(
            person_create_dto, session=db.session
        )
        if validation_results:
            raise BadRequest(f"Invalid payload: {validation_results}")
        person_created = PersonRepository.create(person_create_dto)
        return person_created
