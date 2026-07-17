"""
Centralized logging configuration for HELIX AI Shop API.
"""

from __future__ import annotations

import logging
import sys

from api.config import settings
from api.context import get_request_id

# ==========================================================
# Request Context Filter
# ==========================================================


class RequestContextFilter(logging.Filter):
    """
    Inject request-specific information into every log record.
    """

    def filter(
        self,
        record: logging.LogRecord,
    ) -> bool:
        record.request_id = get_request_id()

        return True


# ==========================================================
# Logger Configuration
# ==========================================================

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | [%(request_id)s] | %(name)s | %(message)s"

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# ==========================================================
# Public Logger
# ==========================================================


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger instance.

    Every logger shares the same handler, formatter,
    and automatically includes the current request ID.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(settings.log_level.upper())

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(
        logging.Formatter(
            fmt=LOG_FORMAT,
            datefmt=DATE_FORMAT,
        )
    )

    handler.addFilter(RequestContextFilter())

    logger.addHandler(handler)

    logger.propagate = False

    return logger
