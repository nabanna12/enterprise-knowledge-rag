"""Logging configuration for the backend."""

import logging
import sys

from app.core.config import get_settings


def configure_logging() -> None:
    """Configure application-wide logging."""
    settings = get_settings()

    logging.basicConfig(
        level=settings.log_level.upper(),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )

    logging.getLogger("uvicorn.access").setLevel(settings.log_level.upper())
    logging.getLogger("uvicorn.error").setLevel(settings.log_level.upper())