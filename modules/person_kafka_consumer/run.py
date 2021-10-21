# Built-in packages

# Third-party packages
from dotenv import load_dotenv
load_dotenv()

# Local packages
from person_app import create_app


app = create_app()

if __name__ == "__main__":
    app.run()
