# Built-in packages


# Third-party packages
import grpc

# Local packages
import location_dto
import location_pb2 as location_types
import location_pb2_grpc as location_grpc
import location_service
import location_helpers


class LocationServiceServicer(location_grpc.LocationServiceServicer):
    @location_service.inject_service
    def __init__(self, service: location_service.LocationService):
        self.service = service

    def Create(
        self, request: location_types.CreateRequest, context: grpc.ServicerContext
    ):
        location_data = self.service.create_location(
            location_dto.get_create_location_dto(request)
        )
        location = location_helpers.from_document_to_grpc_location(location_data)
        return location_types.CreateResponse(location=location)

    def Retrieve(
        self, request: location_types.RetrieveRequest, context: grpc.ServicerContext
    ):
        location = location_types.Location()
        return location_types.RetrieveResponse(location=location)


async def serve() -> None:
    server = grpc.aio.server()
    location_grpc.add_LocationServiceServicer_to_server(
        LocationServiceServicer(), server
    )
    server.add_insecure_port("[::]:8080")
    await server.start()
    await server.wait_for_termination()
