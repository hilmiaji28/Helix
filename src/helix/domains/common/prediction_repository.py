"""
HELIX Prediction Repository.
"""

from __future__ import annotations

from typing import Any

import pandas as pd


class PredictionRepository:
    """
    Base repository for prediction persistence.
    """

    def save_prediction(
        self,
        prediction: pd.DataFrame,
    ) -> None:
        """
        Persist prediction.

        Override for database implementation.
        """

        return None

    def load_prediction_history(
        self,
    ) -> list[Any]:
        """
        Load historical predictions.
        """

        return []
