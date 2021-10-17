# Built-in packages
import typing
import logging
import datetime
import os

# Third-party packages
from flask import request, Flask
from flask_accepts import accepts, responds
from flask_restx import Api, Resource
from werkzeug.exceptions import BadRequest, NotFound
from requests import get

# Local packages
# from connection_schema import ConnectionQuerySchema
from connection_service import ConnectionService
from connection_schema import ConnectionQuerySchema

DATE_FORMAT = "%Y-%m-%d"

api = Api(title="Connection API", version="1.0.0")
ns = api.namespace("connections", description="Connection CRUD operations")

# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger("connection-api")


@ns.errorhandler(BadRequest)
def handle_bad_request(error):
    # logger.warning(str(error))
    return {"message": str(error)}, 400


@ns.errorhandler(NotFound)
def handle_no_result_exception(error):
    # logger.warning(str(error))
    return {"message": str(error)}, 404


@ns.route("/<int:person_id>")
@ns.param("start_date", "Lower bound of date range", _in="query")
@ns.param("end_date", "Upper bound of date range", _in="query")
@ns.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @accepts(
        query_params_schema=ConnectionQuerySchema,
        api=api,
    )
    # @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id: int):
        start_date: datetime = request.parsed_query_params.get("start_date")
        end_date: datetime = request.parsed_query_params.get("end_date")
        distance: int = request.parsed_query_params.get("distance")

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )

        return results


def register_api(app: Flask) -> None:
    api.init_app(app)
