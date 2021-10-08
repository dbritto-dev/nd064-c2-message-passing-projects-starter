# Built-in packages

# Third-party packages

# Local packages
from location_dto import CreateLocationDTO, RetrieveLocationDTO, RetrieveLocationsDTO
from location_repository import LocationRepository
from location_model import LocationModel


class LocationService:
    @staticmethod
    def create(create_location_dto: CreateLocationDTO) -> LocationModel:
        location = LocationRepository.create(create_location_dto)
        return location

    @staticmethod
    def retrieve(retrieve_location_dto: RetrieveLocationDTO) -> LocationModel:
        location = LocationRepository.retrieve(retrieve_location_dto)
        if not location:
            raise Exception(f"Location not found")
        return location

    @staticmethod
    def retrieve_all(
        retrieve_locations_dto: RetrieveLocationsDTO,
    ) -> list[LocationModel]:
        locations = LocationRepository.retrieve_all(retrieve_locations_dto)
        return locations
