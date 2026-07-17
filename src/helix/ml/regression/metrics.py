"""
Regression Metrics.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)


@dataclass(slots=True)
class RegressionResult:
    mae: float

    rmse: float

    mape: float

    r2: float

    adjusted_r2: float


class RegressionMetrics:
    """
    Regression evaluation.
    """

    @staticmethod
    def evaluate(
        y_true,
        y_pred,
        n_features: int,
    ) -> RegressionResult:
        mae = mean_absolute_error(
            y_true,
            y_pred,
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_true,
                y_pred,
            )
        )

        mape = mean_absolute_percentage_error(
            y_true,
            y_pred,
        )

        r2 = r2_score(
            y_true,
            y_pred,
        )

        n = len(y_true)

        adjusted_r2 = 1 - ((1 - r2) * (n - 1) / (n - n_features - 1))

        return RegressionResult(
            mae=mae,
            rmse=rmse,
            mape=mape,
            r2=r2,
            adjusted_r2=adjusted_r2,
        )
