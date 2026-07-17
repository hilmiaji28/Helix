"""
Unit tests for prediction endpoints.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from api.services import prediction_service

# ==========================================================
# Prediction Endpoint
# ==========================================================


def test_predict_success(
    client,
    prediction_payload,
    monkeypatch,
):
    """
    Test successful prediction request.
    """

    monkeypatch.setattr(
        prediction_service,
        "predict",
        lambda payload: {"predicted_purchase_amount": 842.57},
    )

    response = client.post(
        "/predict",
        json=prediction_payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_purchase_amount" in data

    assert data["predicted_purchase_amount"] == 842.57


# ==========================================================
# Validation Error
# ==========================================================


def test_predict_invalid_payload(client):
    """
    Empty payload should return validation error.
    """

    response = client.post(
        "/predict",
        json={},
    )

    assert response.status_code == 422


# ==========================================================
# Missing Required Field
# ==========================================================


def test_predict_missing_field(
    client,
    prediction_payload,
):
    """
    Missing required field should return validation error.
    """

    payload = prediction_payload.copy()

    payload.pop("Age")

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 422


# ==========================================================
# Service Invocation
# ==========================================================


def test_prediction_service_called(
    client,
    prediction_payload,
    monkeypatch,
):
    """
    Prediction service should be called exactly once.
    """

    service = MagicMock()

    service.predict.return_value = {"predicted_purchase_amount": 842.57}

    monkeypatch.setattr(
        prediction_service,
        "predict",
        service.predict,
    )

    response = client.post(
        "/predict",
        json=prediction_payload,
    )

    assert response.status_code == 200

    service.predict.assert_called_once()


# ==========================================================
# Middleware Headers
# ==========================================================


def test_prediction_response_headers(
    client,
    prediction_payload,
    monkeypatch,
):
    """
    Middleware should attach request headers.
    """

    monkeypatch.setattr(
        prediction_service,
        "predict",
        lambda payload: {"predicted_purchase_amount": 842.57},
    )

    response = client.post(
        "/predict",
        json=prediction_payload,
    )

    assert response.status_code == 200

    assert "X-Request-ID" in response.headers

    assert "X-Process-Time-ms" in response.headers
