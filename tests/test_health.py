"""Tests for the initial system endpoints."""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint() -> None:
    """The root endpoint should confirm that the API is running."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["docs"] == "/docs"


def test_health_endpoint() -> None:
    """The health endpoint should return a healthy status."""
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_info_endpoint() -> None:
    """The info endpoint should return application metadata."""
    response = client.get("/api/v1/info")

    assert response.status_code == 200
    assert "application" in response.json()
    assert "version" in response.json()
    assert "environment" in response.json()