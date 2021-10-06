# Built-in packages

# Third-party packages
from flask import Flask

# Local packages


def create_app():
    from cors import register_cors
    from controller import register_api
    from database import register_db

    app = Flask(__name__)

    register_cors(app)
    register_api(app)
    register_db(app)

    return app
