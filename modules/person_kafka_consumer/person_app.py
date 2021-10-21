# Built-in packages
import os

# Third-party packages


# Local packages
from person_server import Server


def create_app() -> Server:
    from person_database import register_db
    from person_kafka import register_kafka

    server = Server()

    register_db()
    register_kafka()

    return server
