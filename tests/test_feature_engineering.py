"""
Unit tests for FeatureEngineering.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from api.feature_engineering import FeatureEngineering

# ==========================================================
# Fixtures
# ==========================================================


@pytest.fixture(scope="module")
def feature_engineering():
    """
    Create a FeatureEngineering instance using project artifacts.
    """

    artifacts = Path("artifacts")

    return FeatureEngineering(
        feature_columns_path=artifacts / "feature_columns.pkl",
        frequency_maps_path=artifacts / "frequency_maps.pkl",
        preprocessing_metadata_path=artifacts / "preprocessing_metadata.pkl",
    )


@pytest.fixture
def valid_payload():
    """
    Valid input payload.
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
# Initialization
# ==========================================================


def test_feature_engineering_initialization(
    feature_engineering,
):
    """
    FeatureEngineering should load all artifacts.
    """

    assert feature_engineering.feature_columns is not None

    assert feature_engineering.frequency_maps is not None

    assert feature_engineering.preprocessing_metadata is not None


# ==========================================================
# Transform
# ==========================================================


def test_transform_returns_dataframe(
    feature_engineering,
    valid_payload,
):
    """
    Transform should return a DataFrame.
    """

    result = feature_engineering.transform(valid_payload)

    assert isinstance(result, pd.DataFrame)

    assert len(result) == 1


def test_transform_has_expected_columns(
    feature_engineering,
    valid_payload,
):
    """
    Output columns must match training columns.
    """

    result = feature_engineering.transform(valid_payload)

    assert list(result.columns) == (feature_engineering.feature_columns)


def test_transform_has_no_missing_columns(
    feature_engineering,
    valid_payload,
):
    """
    Every expected feature should exist.
    """

    result = feature_engineering.transform(valid_payload)

    for column in feature_engineering.feature_columns:
        assert column in result.columns


# ==========================================================
# Validation
# ==========================================================


def test_missing_required_column(
    feature_engineering,
    valid_payload,
):
    """
    Missing required input should raise ValueError.
    """

    payload = valid_payload.copy()

    payload.pop("Age")

    with pytest.raises(ValueError):
        feature_engineering.transform(payload)


# ==========================================================
# Date Features
# ==========================================================


def test_date_features_created(
    feature_engineering,
    valid_payload,
):
    """
    Date-derived features should be generated.
    """

    result = feature_engineering.transform(valid_payload)

    for column in [
        "Month",
        "Day",
        "Weekday",
        "Quarter",
    ]:
        assert column in result.columns


# ==========================================================
# Feature Order
# ==========================================================


def test_feature_order(
    feature_engineering,
    valid_payload,
):
    """
    Output feature order must match training.
    """

    result = feature_engineering.transform(valid_payload)

    assert result.columns.tolist() == feature_engineering.feature_columns
