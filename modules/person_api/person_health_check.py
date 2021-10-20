# Built-in packages

# Third-party packages
from flask import jsonify, Flask, Response

# Local packages


def register_health_check(app: Flask) -> None:
    @app.route("/health")
    def _health() -> Response:  # noqa
        return jsonify("healthy")
