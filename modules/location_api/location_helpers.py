# Built-in packages

# Third-party packages
from geoalchemy2.shape import to_shape
from google.protobuf.timestamp_pb2 import Timestamp


# Local packages
from location_pb2 import Location, Coordinate
from location_model import LocationModel


def from_instance_to_grpc(instance: LocationModel) -> Location:
    location_id = instance.id
    location_person_id = instance.person_id
    location_coordinate_shape = to_shape(instance.coordinate)
    location_coordinate = Coordinate(
        latitude=str(location_coordinate_shape.x),
        longitude=str(location_coordinate_shape.y),
    )
    location_creation_time = Timestamp(seconds=int(instance.creation_time.timestamp()))
    location = Location(
        id=location_id,
        person_id=location_person_id,
        coordinate=location_coordinate,
        creation_time=location_creation_time,
    )
    return location


def from_instances_to_grpc(instances: list[LocationModel]) -> list[Location]:
    return list(map(from_instance_to_grpc, instances))
