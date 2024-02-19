import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv('APP_NAME')


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings")
    return settings


settings = get_settings()

print(settings.APP_NAME)
