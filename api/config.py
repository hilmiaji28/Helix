"""
Application configuration for HELIX AI Shop API.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ======================================================
    # Application
    # ======================================================

    app_name: str = Field(alias="APP_NAME")

    app_version: str = Field(alias="APP_VERSION")

    app_description: str = Field(alias="APP_DESCRIPTION")

    app_env: Literal[
        "development",
        "staging",
        "production",
    ] = Field(alias="APP_ENV")

    debug: bool = Field(alias="DEBUG")

    # ======================================================
    # Server
    # ======================================================

    host: str = Field(alias="HOST")

    port: int = Field(alias="PORT")

    # ======================================================
    # API Documentation
    # ======================================================

    docs_url: str = Field(alias="DOCS_URL")

    redoc_url: str = Field(alias="REDOC_URL")

    openapi_url: str = Field(alias="OPENAPI_URL")

    # ======================================================
    # Logging
    # ======================================================

    log_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = Field(alias="LOG_LEVEL")

    # ======================================================
    # Machine Learning Artifacts
    # ======================================================

    model_path: str = Field(alias="MODEL_PATH")

    feature_columns_path: str = Field(alias="FEATURE_COLUMNS_PATH")

    feature_metadata_path: str = Field(alias="FEATURE_METADATA_PATH")

    frequency_maps_path: str = Field(alias="FREQUENCY_MAPS_PATH")

    preprocessing_metadata_path: str = Field(alias="PREPROCESSING_METADATA_PATH")

    # ======================================================
    # Machine Learning
    # ======================================================

    target_column: str = Field(alias="TARGET_COLUMN")

    # ======================================================
    # API
    # ======================================================

    api_prefix: str = Field(alias="API_PREFIX")

    # ======================================================
    # Optional Features
    # ======================================================

    enable_metrics: bool = Field(alias="ENABLE_METRICS")

    enable_request_logging: bool = Field(alias="ENABLE_REQUEST_LOGGING")

    enable_swagger: bool = Field(alias="ENABLE_SWAGGER")

    enable_redoc: bool = Field(alias="ENABLE_REDOC")

    cors_origins: str = Field(alias="CORS_ORIGINS")

    rate_limit_enabled: bool = Field(alias="RATE_LIMIT_ENABLED")

    cache_enabled: bool = Field(alias="CACHE_ENABLED")


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """
    return Settings()


settings = get_settings()
