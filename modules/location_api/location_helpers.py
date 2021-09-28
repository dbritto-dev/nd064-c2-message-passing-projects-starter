# Built-in packages

# Third-party packages

# Local packages
import location_dto
import location_pb2 as location_types


def from_document_to_grpc_location(
    location_data: location_dto.LocationData,
) -> location_types.Location:
    return location_types.Location(
        id=str(location_data.get("_id")),
        person_id=location_data.get("person_id"),
        coordinate=location_data.get("coordinate"),
        creation_time=location_data.get("creation_time"),
    )
