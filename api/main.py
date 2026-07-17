"""
Main entry point for HELIX AI Shop API.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.config import settings
from api.docs import configure_openapi
from api.exceptions import register_exception_handlers
from api.loader import resource_loader
from api.logger import get_logger
from api.middleware import register_middlewares
from api.routers.health import router as health_router
from api.routers.predict import router as predict_router

logger = get_logger(__name__)


# ==========================================================
# Application Lifespan
# ==========================================================


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    logger.info("=" * 60)
    logger.info(
        "Starting %s...",
        settings.app_name,
    )
    logger.info("=" * 60)

    try:
        resource_loader.load()

        logger.info(
            "%s started successfully.",
            settings.app_name,
        )

        yield

    finally:
        logger.info("=" * 60)
        logger.info(
            "Shutting down %s...",
            settings.app_name,
        )
        logger.info("=" * 60)


# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    docs_url=(settings.docs_url if settings.enable_swagger else None),
    redoc_url=(settings.redoc_url if settings.enable_redoc else None),
    openapi_url=settings.openapi_url,
    debug=settings.debug,
    lifespan=lifespan,
)


# ==========================================================
# OpenAPI Configuration
# ==========================================================

configure_openapi(app)


# ==========================================================
# Exception Handlers
# ==========================================================

register_exception_handlers(app)


# ==========================================================
# Middleware
# ==========================================================

register_middlewares(app)


# ==========================================================
# Routers
# ==========================================================

app.include_router(
    health_router,
)

app.include_router(
    predict_router,
)


# ==========================================================
# Root Endpoint
# ==========================================================


@app.get(
    "/",
    tags=["Health"],
    summary="API Information",
)
async def root():
    """
    Root endpoint.
    """

    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "status": "running",
        "docs": settings.docs_url if settings.enable_swagger else None,
    }
