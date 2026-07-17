"""
Unit tests for health endpoints.
"""

from __future__ import annotations

from api.config import settings

# ==========================================================
# Health Endpoint
# ==========================================================


def test_health_endpoint(client):
    """
    Test the health endpoint returns HTTP 200.
    """

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"

    assert data["application"] == settings.app_name

    assert "timestamp" in data


# ==========================================================
# Root Endpoint
# ==========================================================


def test_root_endpoint(client):
    """
    Test the root endpoint returns application metadata.
    """

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == settings.app_name

    assert data["version"] == settings.app_version

    assert data["environment"] == settings.app_env

    assert data["status"] == "running"


# ==========================================================
# OpenAPI
# ==========================================================


def test_openapi_endpoint(client):
    """
    Test OpenAPI schema endpoint.
    """

    response = client.get(settings.openapi_url)

    assert response.status_code == 200

    schema = response.json()

    assert "openapi" in schema

    assert schema["info"]["title"] == settings.app_name


# ==========================================================
# Swagger Documentation
# ==========================================================


def test_swagger_endpoint(client):
    """
    Swagger endpoint should be available when enabled.
    """

    if not settings.enable_swagger:
        return

    response = client.get(settings.docs_url)

    assert response.status_code == 200


# ==========================================================
# ReDoc Documentation
# ==========================================================


def test_redoc_endpoint(client):
    """
    ReDoc endpoint should be available when enabled.
    """

    if not settings.enable_redoc:
        return

    response = client.get(settings.redoc_url)

    assert response.status_code == 200
