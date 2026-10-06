"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings.

    Values are loaded from the environment and, when available, from
    the .env file in the project root.
    """

    app_name: str = Field(
        default="Enterprise Knowledge RAG Backend",
        validation_alias="APP_NAME",
    )
    app_version: str = Field(
        default="0.1.0",
        validation_alias="APP_VERSION",
    )
    environment: str = Field(
        default="development",
        validation_alias="ENVIRONMENT",
    )
    debug: bool = Field(
        default=True,
        validation_alias="DEBUG",
    )
    api_prefix: str = Field(
        default="/api/v1",
        validation_alias="API_PREFIX",
    )
    log_level: str = Field(
        default="INFO",
        validation_alias="LOG_LEVEL",
    )
    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/enterprise_rag",
        validation_alias="DATABASE_URL",
    )
    secret_key: str = Field(
        default="development-only-secret-change-before-production",
        validation_alias="SECRET_KEY",
    )
    cors_origins: str = Field(
        default="http://localhost:3000,http://localhost:5173",
        validation_alias="CORS_ORIGINS",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        """Return configured CORS origins as a cleaned list."""
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    """Return one cached Settings instance for the application."""
    return Settings()