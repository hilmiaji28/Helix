"""
Custom OpenAPI configuration for HELIX AI Shop API.
"""

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api.config import settings
from api.constants import TAGS_METADATA


def configure_openapi(app: FastAPI) -> None:
    """
    Configure a custom OpenAPI schema for the application.
    """

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title=settings.app_name,
            version=settings.app_version,
            description=settings.app_description,
            routes=app.routes,
            tags=TAGS_METADATA,
        )

        openapi_schema["info"]["x-logo"] = {
            "url": ("https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png")
        }

        openapi_schema["externalDocs"] = {
            "description": "HELIX AI Shop Documentation",
            "url": "https://github.com/",
        }

        app.openapi_schema = openapi_schema

        return app.openapi_schema

    app.openapi = custom_openapi
