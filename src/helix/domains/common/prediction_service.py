"""
HELIX Prediction Service.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from helix.ml.common import BaseEngine

from .prediction_repository import PredictionRepository
from .prediction_schema import PredictionResult


class PredictionService:
    """
    Generic prediction service.
    """

    def __init__(
        self,
        engine: BaseEngine,
        repository: PredictionRepository | None = None,
    ) -> None:
        self.engine = engine

        self.repository = repository or PredictionRepository()

    # =====================================================
    # Training
    # =====================================================

    def train(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        save_path: str | Path | None = None,
    ):
        return self.engine.fit(
            X,
            y,
            save_path,
        )

    # =====================================================
    # Prediction
    # =====================================================

    def predict(
        self,
        X: pd.DataFrame,
    ) -> PredictionResult:
        prediction = self.engine.predict_dataframe(
            X,
        )

        self.repository.save_prediction(
            prediction,
        )

        return PredictionResult(
            prediction=prediction,
            metrics=self.engine.score(),
        )

    # =====================================================
    # Metadata
    # =====================================================

    @property
    def model(self):
        return self.engine.model

    @property
    def config(self):
        return self.engine.config

    @property
    def metrics(self):
        return self.engine.score()

    @property
    def is_trained(self):
        return self.engine.is_trained
