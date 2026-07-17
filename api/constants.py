"""
Application constants for HELIX AI Shop API.
"""

from typing import Final

# ==========================================================
# OpenAPI Tags
# ==========================================================

TAGS_METADATA: Final[list[dict]] = [
    {
        "name": "Health",
        "description": (
            "Health check endpoints used to verify that the "
            "application is running correctly."
        ),
    },
    {
        "name": "Prediction",
        "description": (
            "Endpoints for predicting customer purchase amount "
            "using the trained machine learning model."
        ),
    },
]


# ==========================================================
# Default API Responses
# ==========================================================

DEFAULT_RESPONSES: Final[dict[int, dict[str, str]]] = {
    200: {"description": "Request completed successfully."},
    400: {"description": "Bad request."},
    404: {"description": "Resource not found."},
    422: {"description": "Validation error."},
    500: {"description": "Internal server error."},
}
