# Built-in packages

# Third-party packages
from flask import jsonify, Flask

# Local packages


def create_app() -> Flask:
    from connection_cors import register_cors
    from connection_controller import register_api

    app = Flask(__name__)

    register_cors(app)
    register_api(app)

    @app.route("/health")
    def _():
        return jsonify("healthy")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
