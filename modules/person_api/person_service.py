# Built-in packages

# Third-party packages
from werkzeug.exceptions import BadRequest, NotFound

# Local packages
from person_database import db
from person_model import PersonModel
from person_schema import PersonSchema
from person_dto import PersonCreateDTO
from person_repository import PersonRepository


class PersonService:
    @staticmethod
    def create(person_create_dto: PersonCreateDTO) -> PersonModel:
        validation_results = PersonSchema().validate(person_create_dto, session=db.session)
        if validation_results:
            raise BadRequest(f"Invalid payload: {validation_results}")
        person_created = PersonRepository.create(person_create_dto)
        return person_created

    @staticmethod
    def retrieve(person_id: int) -> PersonModel:
        person = PersonRepository.retrieve(person_id)
        if not person:
            raise NotFound(f"Person {person_id} doesn't exist")
        return person

    @staticmethod
    def retrieve_all() -> list[PersonModel]:
        persons = PersonRepository.retrieve_all()
        return persons
