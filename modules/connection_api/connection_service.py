# Built-in packages
import os
import logging
import datetime
import typing

# Third-party packages
# from geoalchemy2.functions import ST_AsText, ST_Point
# from sqlalchemy.sql import text
from grpc import insecure_channel

# Local packages
# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger("udaconnect-api")
from requests import get
from location_pb2 import (
    Location,
    Coordinate,
    RetrieveAllRequest,
    RetrieveAllResponse,
    RetrieveFilteredRequest,
    RetrieveFilteredResponse,
)
from location_pb2_grpc import LocationServiceStub
from google.protobuf.timestamp_pb2 import Timestamp


LOCATION_API_ENDPOINT = os.getenv("LOCATION_API_ENDPOINT")
PERSON_API_ENDPOINT = os.getenv("PERSON_API_ENDPOINT")


class ConnectionService:
    @staticmethod
    def find_contacts(
        person_id: int,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        meters=5,
    ) -> list[typing.Any]:
        """
        Finds all Person who have been within a given distance of a given Person within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """
        location_api_stub = LocationServiceStub(insecure_channel(LOCATION_API_ENDPOINT))

        location_api_response: RetrieveAllResponse = location_api_stub.RetrieveAll(
            RetrieveAllRequest(
                person_id=person_id,
                start_date=Timestamp(seconds=int(start_date.timestamp())),
                end_date=Timestamp(seconds=int(end_date.timestamp())),
            )
        )
        coordinates = map(lambda item: item.coordinate, location_api_response.locations)

        # Cache all users in memory for quick lookup}
        person_api_response = get(f"{PERSON_API_ENDPOINT}/persons/")
        person_map: dict[str, dict] = {
            person.get("id"): person for person in person_api_response.json()
        }

        # # Prepare arguments for queries
        result: list[typing.Any] = []

        for coordinate in coordinates:
            logging.info(coordinate)

            location_api_response: RetrieveFilteredResponse = (
                location_api_stub.RetrieveFiltered(
                    RetrieveFilteredRequest(
                        person_id=person_id,
                        coordinate=coordinate,
                        start_date=Timestamp(seconds=int(start_date.timestamp())),
                        end_date=Timestamp(seconds=int(end_date.timestamp())),
                        meters=meters,
                    )
                )
            )
            locations: list[Location] = location_api_response.locations
            for location in locations:
                result.append(
                    {
                        "person": person_map[location.person_id],
                        "location": {
                            "id": location.id,
                            "person_id": location.person_id,
                            "latitude": location.coordinate.latitude,
                            "longitude": location.coordinate.longitude,
                            "creation_time": datetime.datetime.fromtimestamp(
                                location.creation_time.seconds
                            ).isoformat(),
                        },
                    }
                )

        return result
