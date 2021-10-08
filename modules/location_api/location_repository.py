# Built-in packages

# Third-party packages

# Local packages
from location_database import db
from location_dto import CreateLocationDTO, RetrieveLocationDTO, RetrieveLocationsDTO
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
    def retrieve(retrieve_location_dto: RetrieveLocationDTO) -> LocationModel:
        location = (
            db.session.query(LocationModel)
            .filter(LocationModel.id == retrieve_location_dto.get("id"))
            .first()
        )
        return location

    @staticmethod
    def retrieve_all(
        retrieve_locations_dto: RetrieveLocationsDTO,
    ) -> list[LocationModel]:
        locations = (
            db.session.query(LocationModel)
            .filter(
                LocationModel.person_id == retrieve_locations_dto.get("person_id")
                if retrieve_locations_dto.get("person_id")
                else True
            )
            .filter(
                LocationModel.creation_time >= retrieve_locations_dto.get("start_date")
                if retrieve_locations_dto.get("start_date")
                else True
            )
            .filter(
                LocationModel.creation_time < retrieve_locations_dto.get("end_date")
                if retrieve_locations_dto.get("end_date")
                else True
            )
            .all()
        )
        return locations
