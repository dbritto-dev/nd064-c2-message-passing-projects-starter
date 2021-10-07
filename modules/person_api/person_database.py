# Built-in packages
import os

# Third-party packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Local packages

db = SQLAlchemy()


def register_db(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
