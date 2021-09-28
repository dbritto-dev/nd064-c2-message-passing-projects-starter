import pymongo.collection
import location_model


class LocationRepository:
    @location_model.inject_model
    def __init__(self, model: pymongo.collection.Collection):
        self.model = model

    def create_location(self, create_location_dto: dict) -> dict:
        location = {**create_location_dto}
        self.model.insert_one(location)
        return location

    def retrieve_location(self, retrieve_location_dto: dict):
        location = self.model.find_one(retrieve_location_dto)
        return location


def inject_repository(init_func):
    def _inject_repository(self, **kwargs):
        repository = LocationRepository()
        init_func(self, **{"repository": repository, **kwargs})

    return _inject_repository
