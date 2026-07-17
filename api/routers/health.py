"""
Health check API Router.
"""

from datetime import UTC, datetime

from fastapi import APIRouter, status

from api.constants import DEFAULT_RESPONSES
from api.logger import get_logger

logger = get_logger(__name__)


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    summary="Application health check",
    description=(
        "Verify that the HELIX AI Shop API is running and ready to accept requests."
    ),
    operation_id="healthCheck",
    status_code=status.HTTP_200_OK,
    responses={
        **DEFAULT_RESPONSES,
        200: {
            "description": "Application is healthy.",
            "content": {
                "application/json": {
                    "example": {
                        "status": "healthy",
                        "application": "HELIX AI Shop API",
                        "timestamp": "2026-07-17T10:30:45Z",
                    }
                }
            },
        },
    },
)
def health():
    """
    Health check endpoint.
    """

    logger.info("GET /health request received.")

    response = {
        "status": "healthy",
        "application": "HELIX AI Shop API",
        "timestamp": (
            datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        ),
    }

    logger.info("GET /health completed successfully.")

    return response
