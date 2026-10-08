"""System API routes."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.db.database import get_db

router = APIRouter()
settings = get_settings()


@router.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    """Return the API health status."""
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


@router.get("/health/database", tags=["System"])
def database_health_check(db: Session = Depends(get_db)) -> dict[str, str]:
    """Verify that the API can execute a query against PostgreSQL."""
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "postgresql",
        "message": "Database connection is working.",
    }