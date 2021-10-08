# Built-in packages
import typing
import datetime


# Third-party packages
from geoalchemy2.functions import ST_Point


# Local packages
from location_pb2 import CreateRequest, RetrieveRequest, RetrieveAllRequest


class CreateLocationDTO(typing.TypedDict):
    person_id: int
    coordinate: ST_Point


def get_create_location_dto(create_request: CreateRequest) -> CreateLocationDTO:
    return {
        "person_id": create_request.person_id,
        "coordinate": ST_Point(
            create_request.coordinate.latitude, create_request.coordinate.longitude
        ),
    }


class RetrieveLocationDTO(typing.TypedDict):
    id: int


def get_retrieve_location_dto(retrieve_request: RetrieveRequest) -> RetrieveLocationDTO:
    return {"id": retrieve_request.id}


class RetrieveLocationsDTO(typing.TypedDict):
    person_id: typing.Optional[int]
    start_date: typing.Optional[datetime.datetime]
    end_date: typing.Optional[datetime.datetime]


def get_retrieve_locations_dto(
    retrieve_locations_request: RetrieveAllRequest,
) -> RetrieveLocationsDTO:
    return {
        "person_id": (
            retrieve_locations_request.person_id
            if retrieve_locations_request.person_id
            else None
        ),
        "start_date": (
            datetime.datetime.fromtimestamp(
                retrieve_locations_request.start_date.seconds
            ).isoformat()
            if retrieve_locations_request.start_date.seconds > 0
            else None
        ),
        "end_date": (
            datetime.datetime.fromtimestamp(
                retrieve_locations_request.end_date.seconds
            ).isoformat()
            if retrieve_locations_request.end_date.seconds > 0
            else None
        ),
    }
