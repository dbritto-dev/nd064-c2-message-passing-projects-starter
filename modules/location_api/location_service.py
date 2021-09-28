import location_repository
import location_pb2 as location_types


class LocationService:
    @location_repository.inject_repository
    def __init__(self, repository: location_repository.LocationRepository):
        self.repository = repository

    def create_location(self, create_location_dto: dict) -> location_types.Location:
        return self.repository.create_location(create_location_dto)

    def retrieve_location(self, retrieve_location_dto: dict) -> location_types.Location:
        return self.repository.retrieve_location(retrieve_location_dto)


def inject_service(init_func):
    def _inject_service(self, **kwargs):
        service = LocationService()
        init_func(self, **{"service": service, **kwargs})

    return _inject_service
