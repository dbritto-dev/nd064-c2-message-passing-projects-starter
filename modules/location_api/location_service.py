# Built-in packages

# Third-party packages
from werkzeug.exceptions import NotFound

# Local packages
from location_dto import (
    CreateLocationDTO,
    RetrieveLocationsDTO,
    RetrieveLocationsFilteredDTO,
)
from location_repository import LocationRepository
from location_model import LocationModel


class LocationService:
    @staticmethod
    def create(create_location_dto: CreateLocationDTO) -> LocationModel:
        location = LocationRepository.create(create_location_dto)
        return location

    @staticmethod
    def retrieve(location_id: int) -> LocationModel:
        location = LocationRepository.retrieve(location_id)
        if not location:
            raise NotFound(f"Location not found")
        return location

    @staticmethod
    def retrieve_all(
        retrieve_locations_dto: RetrieveLocationsDTO,
    ) -> list[LocationModel]:
        locations = LocationRepository.retrieve_all(retrieve_locations_dto)
        return locations

    def retrieve_filtered(
        retrieve_locations_filtered_dto: RetrieveLocationsFilteredDTO,
    ) -> list[LocationModel]:
        locations = LocationRepository.retrieve_filtered(
            retrieve_locations_filtered_dto
        )
        return locations
