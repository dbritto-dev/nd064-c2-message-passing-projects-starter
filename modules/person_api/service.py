# Built-in packages

# Third-party packages
from werkzeug.exceptions import BadRequest, NotFound

# Local packages
from model import Person
from schema import PersonSchema
from dto import PersonCreateDTO
from repository import PersonRepository


class PersonService:
    @staticmethod
    def create(person_create_dto: PersonCreateDTO) -> Person:
        validation_results = PersonSchema().validate(person_create_dto)
        if validation_results:
            raise BadRequest(f"Invalid payload: {validation_results}")
        person_created = PersonRepository.create(person_create_dto)
        return person_created

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = PersonRepository.retrieve(person_id)
        if not person:
            raise NotFound(f"Person {person_id} doesn't exist")
        return person

    @staticmethod
    def retrieve_all() -> list[Person]:
        persons = PersonRepository.retrieve_all()
        return persons
