"""
Application middleware for HELIX AI Shop API.
"""

from __future__ import annotations

import time
import uuid

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from api.config import settings
from api.context import (
    clear_request_id,
    set_request_id,
)
from api.logger import get_logger

logger = get_logger(__name__)


# ==========================================================
# Request Logging Middleware
# ==========================================================


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware responsible for:

    - Request ID generation
    - Request logging
    - Response logging
    - Processing time measurement
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        request_id = str(uuid.uuid4())

        set_request_id(request_id)

        start_time = time.perf_counter()

        client = request.client.host if request.client else "unknown"

        logger.info("=" * 60)
        logger.info(
            "Request Started | id=%s",
            request_id,
        )
        logger.info(
            "%s %s",
            request.method,
            request.url.path,
        )
        logger.info(
            "Client=%s",
            client,
        )

        try:
            response = await call_next(request)

        finally:
            duration_ms = (time.perf_counter() - start_time) * 1000

            logger.info(
                "Request Finished | id=%s",
                request_id,
            )

            logger.info(
                "Status=%s",
                getattr(
                    response,
                    "status_code",
                    "unknown",
                ),
            )

            logger.info(
                "Duration=%.2f ms",
                duration_ms,
            )

            logger.info("=" * 60)

            clear_request_id()

        response.headers["X-Request-ID"] = request_id

        response.headers["X-Process-Time-ms"] = f"{duration_ms:.2f}"

        return response


# ==========================================================
# Security Headers Middleware
# ==========================================================


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Add common HTTP security headers.
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"

        response.headers["X-Frame-Options"] = "DENY"

        response.headers["Referrer-Policy"] = "same-origin"

        response.headers["X-XSS-Protection"] = "1; mode=block"

        return response


# ==========================================================
# Middleware Registration
# ==========================================================


def register_middlewares(app: FastAPI) -> None:
    """
    Register all application middleware.
    """

    app.add_middleware(
        SecurityHeadersMiddleware,
    )

    if settings.enable_request_logging:
        app.add_middleware(
            RequestLoggingMiddleware,
        )
