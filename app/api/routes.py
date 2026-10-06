"""Basic API routes for the backend foundation."""

from datetime import datetime, timezone

from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()
settings = get_settings()


@router.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    """Return the current health status of the API."""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/info", tags=["System"])
def application_info() -> dict[str, str]:
    """Return basic non-sensitive application information."""
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }