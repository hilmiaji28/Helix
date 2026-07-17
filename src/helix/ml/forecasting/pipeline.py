from __future__ import annotations

from sklearn.model_selection import TimeSeriesSplit

from helix.ml.common import BasePipeline

from .metrics import ForecastMetrics


class ForecastPipeline(BasePipeline):
    def __init__(
        self,
        trainer,
        predictor,
        n_splits: int = 5,
    ):
        super().__init__(
            trainer=trainer,
            predictor=predictor,
        )

        self.n_splits = n_splits

    def split(
        self,
        X,
        y,
    ):
        splitter = TimeSeriesSplit(
            n_splits=self.n_splits,
        )

        train_idx, test_idx = list(splitter.split(X))[-1]

        return (
            X.iloc[train_idx],
            X.iloc[test_idx],
            y.iloc[train_idx],
            y.iloc[test_idx],
        )

    def evaluate(
        self,
        y_true,
        y_pred,
        **kwargs,
    ):
        return ForecastMetrics.evaluate(
            y_true,
            y_pred,
        )
