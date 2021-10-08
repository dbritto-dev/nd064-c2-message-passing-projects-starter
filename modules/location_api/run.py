# Built-in packages
import logging

# Third-party packages
from dotenv import load_dotenv

# Local packages
from location_app import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(f'* Running on 127.0.0.1:8080')

    app.start()
    app.wait_for_termination()
