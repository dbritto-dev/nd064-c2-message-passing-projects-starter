# Built-in packages

# Third-party packages
from flask import Flask
from flask_cors import CORS

# Local packages


def register_cors(app: Flask):
    CORS(app)
