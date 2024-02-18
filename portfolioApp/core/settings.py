import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv('APP_NAME')


settings = Settings()

print(settings.APP_NAME)
