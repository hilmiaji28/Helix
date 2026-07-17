"""
Standard response builders for HELIX AI Shop API.
"""

from typing import Any

from fastapi.responses import JSONResponse


def success_response(
    data: Any,
    message: str = "Request completed successfully.",
    status_code: int = 200,
) -> JSONResponse:
    """
    Build a standardized success response.
    """

    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data,
        },
    )


def created_response(
    data: Any,
    message: str = "Resource created successfully.",
) -> JSONResponse:
    """
    Build a standardized resource created response.
    """

    return success_response(
        data=data,
        message=message,
        status_code=201,
    )


def accepted_response(
    data: Any,
    message: str = "Request accepted.",
) -> JSONResponse:
    """
    Build a standardized accepted response.
    """

    return success_response(
        data=data,
        message=message,
        status_code=202,
    )


def no_content_response() -> JSONResponse:
    """
    Build a standardized no-content response.
    """

    return JSONResponse(
        status_code=204,
        content=None,
    )


def error_response(
    error: str,
    detail: Any,
    status_code: int,
) -> JSONResponse:
    """
    Build a standardized error response.
    """

    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": error,
            "detail": detail,
        },
    )
