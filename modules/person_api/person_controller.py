# Built-in packages
import logging

# Third-party packages
from flask import request, Flask, Response
from flask_accepts import accepts, responds
from flask_restx import Api, Resource
from werkzeug.exceptions import BadRequest, NotFound

# Local packages
from person_model import PersonModel
from person_schema import PersonSchema
from person_service import PersonService
from person_dto import PersonCreateDTO


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
    def post(self) -> PersonModel:
        payload: PersonCreateDTO = request.get_json()
        PersonService.create(payload)
        return Response(status=202)

    @responds(schema=PersonSchema(many=True))
    def get(self) -> list[PersonModel]:
        persons = PersonService.retrieve_all()
        return persons


@ns.route("/<int:person_id>")
@ns.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema, api=api)
    def get(self, person_id: int) -> PersonModel:
        person = PersonService.retrieve(person_id)
        return person


def register_api(app: Flask) -> None:
    app.config["ERROR_INCLUDE_MESSAGE"] = False

    api.init_app(app)
