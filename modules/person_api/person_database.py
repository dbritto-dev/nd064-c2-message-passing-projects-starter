# Built-in packages
import os

# Third-party packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Local packages

db = SQLAlchemy()

DB_USER = os.getenv("DB_USERNAME")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")


def register_db(app: Flask) -> None:
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
