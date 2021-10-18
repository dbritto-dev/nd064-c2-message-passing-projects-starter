# Built-in packages


# Third-party packages
from grpc import Server, ServicerContext, StatusCode


# Local packages
from location_pb2_grpc import (
    LocationServiceServicer as BaseLocationServiceServicer,
    add_LocationServiceServicer_to_server,
)
from location_pb2 import (
    CreateRequest,
    CreateResponse,
    RetrieveRequest,
    RetrieveResponse,
    RetrieveAllRequest,
    RetrieveAllResponse,
    RetrieveFilteredRequest,
    RetrieveFilteredResponse,
)
from location_dto import (
    get_create_location_dto,
    get_retrieve_locations_dto,
    get_retrieve_locations_filtered_dto,
)
from location_service import LocationService
from location_helpers import from_instance_to_grpc, from_instances_to_grpc
from health_pb2 import HealthCheckRequest, HealthCheckResponse
from health_pb2_grpc import (
    HealthServicer as BaseHealthServicer,
    add_HealthServicer_to_server,
)


def register_api(grpc_server: Server):
    class LocationServiceServicer(BaseLocationServiceServicer):
        def Create(
            self, request: CreateRequest, context: ServicerContext
        ) -> CreateResponse:
            try:
                create_location_dto = get_create_location_dto(request)
                instance = LocationService.create(create_location_dto)
                location = from_instance_to_grpc(instance)
                return CreateResponse(location=location)
            except Exception as e:
                context.set_details(str(e))
                context.set_code(StatusCode.INTERNAL)
                return CreateResponse()

        def Retrieve(
            self, request: RetrieveRequest, context: ServicerContext
        ) -> RetrieveResponse:
            try:
                instance = LocationService.retrieve(request.id)
                location = from_instance_to_grpc(instance)
                return RetrieveResponse(location=location)
            except Exception as e:
                context.set_details(str(e))
                context.set_code(StatusCode.NOT_FOUND)
                return RetrieveResponse()

        def RetrieveAll(
            self, request: RetrieveAllRequest, context: ServicerContext
        ) -> RetrieveAllResponse:
            retrieve_locations_dto = get_retrieve_locations_dto(request)
            instances = LocationService.retrieve_all(retrieve_locations_dto)
            locations = from_instances_to_grpc(instances)
            return RetrieveAllResponse(locations=locations)

        def RetrieveFiltered(
            self, request: RetrieveFilteredRequest, context: ServicerContext
        ):
            retrieve_locations_filtered_dto = get_retrieve_locations_filtered_dto(
                request
            )
            instances = LocationService.retrieve_filtered(
                retrieve_locations_filtered_dto
            )
            locations = from_instances_to_grpc(instances)
            return RetrieveFilteredResponse(locations=locations)

    class HealthServicer(BaseHealthServicer):
        def Check(self, request: HealthCheckResponse, context: ServicerContext):
            return HealthCheckResponse(status=HealthCheckResponse.SERVING)

    add_LocationServiceServicer_to_server(LocationServiceServicer(), grpc_server)
    add_HealthServicer_to_server(HealthServicer(), grpc_server)
