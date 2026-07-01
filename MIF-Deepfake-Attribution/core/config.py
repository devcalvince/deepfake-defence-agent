import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    APP_NAME = os.getenv("APP_NAME")

    APP_VERSION = os.getenv("APP_VERSION")

    DATABASE_URL = os.getenv("DATABASE_URL")

    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
    )

    AES_KEY = os.getenv("AES_KEY")

    BLOCKCHAIN_PROVIDER = os.getenv("BLOCKCHAIN_PROVIDER")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()