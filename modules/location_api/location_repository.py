# Built-in packages
import logging

# Third-party packages
from sqlalchemy import cast, func, text
from geoalchemy2.types import Geography
from geoalchemy2.functions import (
    ST_MakePoint,
    ST_DWithin,
    ST_SetSRID,
)

# Local packages
from location_database import db
from location_dto import (
    CreateLocationDTO,
    RetrieveLocationDTO,
    RetrieveLocationsDTO,
    RetrieveLocationsFilteredDTO,
)
from location_schema import LocationSchema
from location_model import LocationModel


class LocationRepository:
    @staticmethod
    def create(create_location_dto: CreateLocationDTO) -> LocationModel:
        location = LocationSchema(load_instance=True).load(
            create_location_dto, session=db.session
        )
        db.session.add(location)
        db.session.commit()

        return location

    @staticmethod
    def retrieve(location_id: int) -> LocationModel:
        return db.session.query(LocationModel).get(location_id)

    @staticmethod
    def retrieve_all(
        retrieve_locations_dto: RetrieveLocationsDTO,
    ) -> list[LocationModel]:
        person_id = retrieve_locations_dto.get("person_id")
        start_date = retrieve_locations_dto.get("start_date")
        end_date = retrieve_locations_dto.get("end_date")
        return (
            db.session.query(LocationModel)
            .filter(LocationModel.person_id == person_id if person_id else True)
            .filter(
                LocationModel.creation_time >= func.to_date(start_date, "YYYY-MM-DD")
                if start_date
                else True
            )
            .filter(
                LocationModel.creation_time < func.to_date(end_date, "YYYY-MM-DD")
                if end_date
                else True
            )
            .all()
        )

    @staticmethod
    def retrieve_filtered(
        retrieve_locations_filtered_dto: RetrieveLocationsFilteredDTO,
    ):
        person_id = retrieve_locations_filtered_dto.get("person_id")
        latitude = retrieve_locations_filtered_dto.get("coordinate").get("latitude")
        longitude = retrieve_locations_filtered_dto.get("coordinate").get("longitude")
        meters = retrieve_locations_filtered_dto.get("meters")
        start_date = retrieve_locations_filtered_dto.get("start_date")
        end_date = retrieve_locations_filtered_dto.get("end_date")
        locations = (
            db.session.query(LocationModel)
            .filter(
                ST_DWithin(
                    cast(LocationModel.coordinate, Geography),
                    cast(
                        ST_SetSRID(ST_MakePoint(latitude, longitude), 4326), Geography
                    ),
                    meters,
                )
            )
            .filter(LocationModel.person_id != person_id)
            .filter(
                LocationModel.creation_time >= func.to_date(start_date, "YYYY-MM-DD")
            )
            .filter(LocationModel.creation_time < func.to_date(end_date, "YYYY-MM-DD"))
            .all()
        )
        return locations
