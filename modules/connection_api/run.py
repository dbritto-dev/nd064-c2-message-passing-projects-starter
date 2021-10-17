# Built-in packages
import logging

# Third-party packages
from dotenv import load_dotenv
from waitress import serve

# Local packages
from connection_app import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve(app)
