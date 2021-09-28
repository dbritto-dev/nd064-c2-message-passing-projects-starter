# Built-in packages
import typing

# Third-party packages


# Local packages
import location_pb2 as location_types


class CoordinateData(typing.TypedDict):
    latitude: str
    longitude: str


class LocationData(typing.TypedDict):
    id: str
    person_id: str
    coordinate: CoordinateData
    creation_time: str


def get_create_location_creation_time_dto(request: location_types.CreateRequest):
    return {
        "seconds": request.creation_time.seconds,
        "nanos": request.creation_time.nanos,
    }


def get_create_location_coordinate_dto(request: location_types.CreateRequest):
    return {
        "latitude": request.coordinate.latitude,
        "longitude": request.coordinate.longitude,
    }


def get_create_location_dto(request: location_types.CreateRequest) -> LocationData:
    return {
        "person_id": request.person_id,
        "coordinate": get_create_location_coordinate_dto(request),
        "creation_time": get_create_location_creation_time_dto(request),
    }


def get_retrieve_location_dto(request: location_types.RetrieveRequest) -> LocationData:
    return {
        "person_id": request.person_id,
        "coordinate": get_create_location_coordinate_dto(request),
        "creation_time": get_create_location_creation_time_dto(request),
    }
