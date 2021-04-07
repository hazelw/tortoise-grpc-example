import os


TORTOISE_CONFIG = {
    "connections": {
        "models": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("TORTOISE_HOST"),
                "port": os.getenv("TORTOISE_PORT"),
                "user": os.getenv("TORTOISE_USER"),
                "password": os.getenv("TORTOISE_PASSWORD"),
                "database": os.getenv("TORTOISE_DATABASE"),
                "timeout": float(os.getenv("TORTOISE_TIMEOUT")) / 1000,
                "command_timeout": float(os.getenv("TORTOISE_COMMAND_TIMEOUT")) / 1000,
            }
        }
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models"],
            "default_connection": "models",
        }
    },
    "use_tz": False,
    "timezone": "UTC"
}
