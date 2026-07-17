"""
Feature Engineering Module

"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd


class FeatureEngineering:
    """
    Feature Engineering class.

    Output:
        pandas.DataFrame (1 row)

    yang sudah identik dengan feature training.
    """

    def __init__(
        self,
        feature_columns_path: str | Path,
        frequency_maps_path: str | Path,
        preprocessing_metadata_path: str | Path,
    ):
        self.feature_columns = joblib.load(feature_columns_path)

        self.frequency_maps = joblib.load(frequency_maps_path)

        self.preprocessing_metadata = joblib.load(preprocessing_metadata_path)

        self.feature_order = self.preprocessing_metadata["feature_order"]

        self.median_session = 15.0

        self.age_bins = [
            0,
            25,
            35,
            45,
            55,
            100,
        ]

        self.age_labels = [
            "18-25",
            "26-35",
            "36-45",
            "46-55",
            "55+",
        ]

    ####################################################################
    # Helper
    ####################################################################

    @staticmethod
    def _safe_divide(
        numerator: float,
        denominator: float,
    ) -> float:
        if denominator == 0:
            return 0.0

        return float(numerator) / float(denominator)

    @staticmethod
    def _month_sin(month: int):
        return math.sin(2 * math.pi * month / 12)

    @staticmethod
    def _month_cos(month: int):
        return math.cos(2 * math.pi * month / 12)

    @staticmethod
    def _weekday_sin(day: int):
        return math.sin(2 * math.pi * day / 7)

    @staticmethod
    def _weekday_cos(day: int):
        return math.cos(2 * math.pi * day / 7)

    def _frequency_lookup(
        self,
        mapping_name: str,
        value,
    ):
        mapping = self.frequency_maps.get(mapping_name, {})

        return mapping.get(value, 0)

    ####################################################################
    # DataFrame Builder
    ####################################################################

    @staticmethod
    def _build_dataframe(payload: dict[str, Any]) -> pd.DataFrame:
        return pd.DataFrame([payload])

    ####################################################################
    # Validation
    ####################################################################

    @staticmethod
    def _validate_required_columns(
        df: pd.DataFrame,
    ):
        required = [
            "Age",
            "Gender",
            "City",
            "Product_Category",
            "Payment_Method",
            "Device_Type",
            "Session_Duration_Minutes",
            "Pages_Viewed",
            "Is_Returning_Customer",
            "Delivery_Time_Days",
            "Customer_Rating",
            "Transaction_Date",
        ]

        missing = [c for c in required if c not in df.columns]

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    ####################################################################
    # Main Transform
    ####################################################################

    def transform(
        self,
        payload: dict[str, Any],
    ) -> pd.DataFrame:
        df = self._build_dataframe(payload)

        self._validate_required_columns(df)

        df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

        ####################################################################
        # Date Features
        ####################################################################

        df["Year"] = df["Transaction_Date"].dt.year

        df["Month"] = df["Transaction_Date"].dt.month

        df["Day"] = df["Transaction_Date"].dt.day

        df["Weekday"] = df["Transaction_Date"].dt.weekday

        df["Quarter"] = df["Transaction_Date"].dt.quarter

        df["Is_Weekend"] = (df["Weekday"] >= 5).astype(int)

        ####################################################################
        # Cyclical Features
        ####################################################################

        df["Month_Sin"] = df["Month"].apply(self._month_sin)

        df["Month_Cos"] = df["Month"].apply(self._month_cos)

        df["Weekday_Sin"] = df["Weekday"].apply(self._weekday_sin)

        df["Weekday_Cos"] = df["Weekday"].apply(self._weekday_cos)

        ####################################################################
        # Age Group
        ####################################################################

        df["Age_Group"] = pd.cut(
            df["Age"],
            bins=self.age_bins,
            labels=self.age_labels,
            include_lowest=True,
        )

        ####################################################################
        # Interaction Features
        ####################################################################

        df["Pages_Per_Minute"] = np.where(
            df["Session_Duration_Minutes"] == 0,
            0,
            (df["Pages_Viewed"] / df["Session_Duration_Minutes"]),
        )

        df["Engagement_Score"] = df["Pages_Viewed"] * df["Session_Duration_Minutes"]

        df["Rating_x_Returning"] = df["Customer_Rating"] * df["Is_Returning_Customer"]

        df["Age_x_Rating"] = df["Age"] * df["Customer_Rating"]

        df["Delivery_x_Session"] = (
            df["Delivery_Time_Days"] * df["Session_Duration_Minutes"]
        )

        ####################################################################
        # Rating per Delivery
        ####################################################################

        df["Rating_per_Delivery"] = np.where(
            df["Delivery_Time_Days"] == 0,
            0,
            (df["Customer_Rating"] / df["Delivery_Time_Days"]),
        )

        ####################################################################
        # Long Session
        ####################################################################

        df["Long_Session"] = (
            df["Session_Duration_Minutes"] > self.median_session
        ).astype(int)

        ####################################################################
        # Frequency Encoding
        ####################################################################

        df["City_Frequency"] = df["City"].apply(
            lambda x: self._frequency_lookup(
                "City",
                x,
            )
        )

        df["Product_Frequency"] = df["Product_Category"].apply(
            lambda x: self._frequency_lookup(
                "Product_Category",
                x,
            )
        )

        df["Payment_Frequency"] = df["Payment_Method"].apply(
            lambda x: self._frequency_lookup(
                "Payment_Method",
                x,
            )
        )

        df["Device_Frequency"] = df["Device_Type"].apply(
            lambda x: self._frequency_lookup(
                "Device_Type",
                x,
            )
        )

        ####################################################################
        # Cleanup
        ####################################################################

        df = df.drop(
            columns=["Transaction_Date"],
            errors="ignore",
        )

        ####################################################################
        # Ensure Training Columns Exist
        ####################################################################

        for column in self.feature_columns:
            if column not in df.columns:
                df[column] = np.nan

        ####################################################################
        # Remove Unexpected Columns
        ####################################################################

        extra_columns = [c for c in df.columns if c not in self.feature_columns]

        if extra_columns:
            df = df.drop(columns=extra_columns)

        ####################################################################
        # Reorder
        ####################################################################

        df = df[self.feature_columns]

        return df
