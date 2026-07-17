"""
Global exception handlers for HELIX AI Shop API.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.logger import get_logger

logger = get_logger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all global exception handlers.
    """

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        logger.warning(
            "Validation error on %s %s",
            request.method,
            request.url.path,
        )

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "error": "ValidationError",
                "detail": exc.errors(),
            },
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ):
        logger.warning(
            "HTTPException on %s %s : %s",
            request.method,
            request.url.path,
            exc.detail,
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": "HTTPException",
                "detail": exc.detail,
            },
        )

    @app.exception_handler(RuntimeError)
    async def runtime_exception_handler(
        request: Request,
        exc: RuntimeError,
    ):
        logger.error(
            "RuntimeError on %s %s : %s",
            request.method,
            request.url.path,
            str(exc),
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "RuntimeError",
                "detail": str(exc),
            },
        )

    @app.exception_handler(FileNotFoundError)
    async def file_not_found_handler(
        request: Request,
        exc: FileNotFoundError,
    ):
        logger.error(
            "Missing file on %s %s : %s",
            request.method,
            request.url.path,
            str(exc),
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "FileNotFoundError",
                "detail": str(exc),
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            "Unhandled exception on %s %s",
            request.method,
            request.url.path,
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "InternalServerError",
                "detail": "Unexpected server error.",
            },
        )
