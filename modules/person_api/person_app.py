# Built-in packages

# Third-party packages
from flask import Flask

# Local packages


def create_app() -> Flask:
    from person_cors import register_cors
    from person_controller import register_api
    from person_database import register_db
    from person_health_check import register_health_check
    from person_kafka import register_kafka

    app = Flask(__name__)

    register_cors(app)
    register_api(app)
    register_db(app)
    register_health_check(app)
    register_kafka(app)

    return app
