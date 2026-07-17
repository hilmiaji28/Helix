from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
)


@dataclass(slots=True)
class ForecastResult:
    mae: float

    rmse: float

    mape: float

    smape: float


class ForecastMetrics:
    @staticmethod
    def evaluate(
        y_true,
        y_pred,
        **kwargs,
    ):
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

        denominator = (np.abs(y_true) + np.abs(y_pred)) / 2

        smape = np.mean(np.abs(y_true - y_pred) / denominator)

        return ForecastResult(
            mae=mae,
            rmse=rmse,
            mape=mape,
            smape=smape,
        )
