"""
Shared pytest fixtures for HELIX AI Shop API.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from api.loader import resource_loader
from api.main import app

# ==========================================================
# Test Client
# ==========================================================


@pytest.fixture(scope="session")
def client() -> TestClient:
    """
    FastAPI test client.
    """
    return TestClient(app)


# ==========================================================
# Prediction Payload
# ==========================================================


@pytest.fixture
def prediction_payload() -> dict:
    """
    Valid prediction payload.
    """

    return {
        "Age": 30,
        "Gender": "Male",
        "City": "Bandung",
        "Product_Category": "Electronics",
        "Payment_Method": "Credit Card",
        "Device_Type": "Mobile",
        "Session_Duration_Minutes": 25,
        "Pages_Viewed": 15,
        "Is_Returning_Customer": 1,
        "Delivery_Time_Days": 2,
        "Customer_Rating": 5,
        "Transaction_Date": "2025-08-20",
    }


# ==========================================================
# Feature Engineering Output
# ==========================================================


@pytest.fixture
def transformed_features() -> pd.DataFrame:
    """
    Mock feature engineering output.
    """

    return pd.DataFrame(
        {
            "feature_1": [1.0],
            "feature_2": [2.0],
            "feature_3": [3.0],
        }
    )


# ==========================================================
# Mock Model
# ==========================================================


@pytest.fixture
def mock_model():
    """
    Mock trained ML model.
    """

    model = MagicMock()

    model.predict.return_value = [842.57]

    return model


# ==========================================================
# Mock Feature Engineering
# ==========================================================


@pytest.fixture
def mock_feature_engineering(
    transformed_features,
):
    """
    Mock FeatureEngineering instance.
    """

    fe = MagicMock()

    fe.transform.return_value = transformed_features

    return fe


# ==========================================================
# Mock Resource Loader
# ==========================================================


@pytest.fixture
def mock_resource_loader(
    monkeypatch,
    mock_model,
    mock_feature_engineering,
):
    """
    Replace ResourceLoader dependencies with mocks.
    """

    monkeypatch.setattr(
        resource_loader,
        "get_model",
        lambda: mock_model,
    )

    monkeypatch.setattr(
        resource_loader,
        "get_feature_engineering",
        lambda: mock_feature_engineering,
    )

    return resource_loader
