import os

import pymongo


def inject_model(init_func):
    def _inject_model(self, **kwargs):
        client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
        database = client[os.getenv("MONGODB_DB_NAME", "person_api_db")]
        model = database[os.getenv("MONGODB_DB_COLLECTION_NAME", "persons")]
        init_func(self, **{"model": model, **kwargs})

    return _inject_model
