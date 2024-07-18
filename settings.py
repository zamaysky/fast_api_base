from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: PostgresDsn

    model_config = SettingsConfigDict(case_sensitive=False, env_file="env")


settings = Settings()