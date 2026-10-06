"""FastAPI application entry point."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import get_settings
from app.core.logging_config import configure_logging

configure_logging()

settings = get_settings()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Run startup and shutdown logic for the application."""
    logger.info("Starting %s", settings.app_name)
    logger.info("Environment: %s", settings.environment)

    yield

    logger.info("Shutting down %s", settings.app_name)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Backend foundation for an enterprise knowledge search "
        "and retrieval system using RAG."
    ),
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(
    router,
    prefix=settings.api_prefix,
)


@app.get("/", tags=["System"])
def root() -> dict[str, str]:
    """Return a basic welcome response."""
    return {
        "message": "Enterprise Knowledge RAG Backend is running.",
        "docs": "/docs",
        "health": f"{settings.api_prefix}/health",
    }