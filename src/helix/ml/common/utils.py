"""
HELIX ML Utilities.
"""

from __future__ import annotations

import pandas as pd


def validate_dataframe(
    df: pd.DataFrame,
) -> None:
    """
    Validate dataframe input.
    """

    if not isinstance(
        df,
        pd.DataFrame,
    ):
        raise TypeError("Input must be pandas.DataFrame.")

    if df.empty:
        raise ValueError("DataFrame is empty.")


def validate_target(
    y: pd.Series | None,
) -> None:
    """
    Validate target.
    """

    if y is None:
        raise ValueError("Target cannot be None.")

    if len(y) == 0:
        raise ValueError("Target is empty.")
