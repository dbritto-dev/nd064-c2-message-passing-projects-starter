# Built-in packages
import logging

# Third-party packages
import dotenv
import waitress

# Local packages
from person_app import create_app

dotenv.load_dotenv()

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    waitress.serve(app)
