# Built-in packages
import logging

# Third-party packages
from flask import request, Flask
from flask_accepts import accepts, responds
from flask_restx import Api, Resource
from werkzeug.exceptions import BadRequest, NotFound

# Local packages
from model import Person
from schema import PersonSchema
from service import PersonService
from dto import PersonCreateDTO


api = Api(title="Person API", version="1.0.0")
ns = api.namespace("persons", description="Person CRUD operations")

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("person-api")


@ns.errorhandler(BadRequest)
def handle_bad_request(error):
    logger.warning(str(error))
    return {"message": str(error)}, 400


@ns.errorhandler(NotFound)
def handle_no_result_exception(error):
    logger.warning(str(error))
    return {"message": str(error)}, 404


@ns.route("/")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema, api=api)
    @responds(schema=PersonSchema, api=api)
    def post(self) -> Person:
        payload: PersonCreateDTO = request.get_json()
        person: Person = PersonService.create(payload)
        return person

    @responds(schema=PersonSchema(many=True))
    def get(self) -> list[Person]:
        persons: list[Person] = PersonService.retrieve_all()
        return persons


@ns.route("/<int:person_id>")
@ns.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema, api=api)
    def get(self, person_id: int) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person


def register_api(app: Flask):
    app.config["ERROR_INCLUDE_MESSAGE"] = False

    api.init_app(app)
