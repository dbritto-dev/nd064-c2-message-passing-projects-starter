# Built-in packages
import asyncio
import logging

# Third-party packages
import dotenv

# Local packages
import location_server

dotenv.load_dotenv()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(location_server.serve())
