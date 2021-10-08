# Built-in packages
from concurrent.futures import ThreadPoolExecutor

# Third-party packages
from grpc import Server, server

# Local packages
from location_controller import register_api
from location_database import register_db


def create_app() -> Server:
    grpc_server = server(ThreadPoolExecutor(max_workers=10))
    register_db()
    register_api(grpc_server)
    grpc_server.add_insecure_port("[::]:8080")

    return grpc_server
