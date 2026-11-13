import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set (check your .env file)")

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["database.models"],
            "migrations": "database.migrations",  # dotted path to the package
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}