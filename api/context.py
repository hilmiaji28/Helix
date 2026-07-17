"""
Request context utilities.

This module stores request-scoped information using ContextVar,
allowing every incoming request to have its own isolated context.

Currently supported:
- Request ID
"""

from __future__ import annotations

from contextvars import ContextVar

# ==========================================================
# Request Context
# ==========================================================

_request_id: ContextVar[str] = ContextVar(
    "request_id",
    default="-",
)


# ==========================================================
# Public API
# ==========================================================


def set_request_id(request_id: str) -> None:
    """
    Store the request ID for the current request context.
    """

    _request_id.set(request_id)


def get_request_id() -> str:
    """
    Return the current request ID.

    Returns:
        str: Request ID for the active request.
    """

    return _request_id.get()


def clear_request_id() -> None:
    """
    Reset the request ID.

    This is mainly used after a request has finished.
    """

    _request_id.set("-")
