"""
HELIX Base Engine.

Public API for all machine learning engines.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from .base_pipeline import BasePipeline, PipelineResult


class BaseEngine:
    """
    Public API for every ML engine.
    """

    def __init__(
        self,
        pipeline: BasePipeline,
    ) -> None:
        self._pipeline = pipeline
        self._last_result: PipelineResult | None = None

    # =====================================================
    # Training
    # =====================================================

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series | None = None,
        save_path: str | Path | None = None,
    ) -> PipelineResult:
        self._last_result = self._pipeline.fit(
            X=X,
            y=y,
            save_path=save_path,
        )

        return self._last_result

    # =====================================================
    # Prediction
    # =====================================================

    def predict(
        self,
        X: pd.DataFrame,
    ):
        return self._pipeline.predict(X)

    def predict_dataframe(
        self,
        X: pd.DataFrame,
        column: str = "prediction",
    ):
        return self._pipeline.predict_dataframe(
            X,
            column,
        )

    def predict_with_input(
        self,
        X: pd.DataFrame,
        column: str = "prediction",
    ):
        return self._pipeline.predict_with_input(
            X,
            column,
        )

    # =====================================================
    # Persistence
    # =====================================================

    def save(
        self,
        path: str | Path,
    ) -> None:
        self._pipeline.trainer.save(path)

    def load(
        self,
        path: str | Path,
    ) -> Any:
        model = self._pipeline.trainer.load(path)
        self._pipeline.predictor.set_model(model)

        return model

    # =====================================================
    # Metadata
    # =====================================================

    @property
    def model(self):
        return self._pipeline.model

    @property
    def config(self):
        return self._pipeline.config

    @property
    def is_trained(self):
        return self._pipeline.is_trained

    @property
    def result(self) -> PipelineResult | None:
        return self._last_result

    # =====================================================
    # Evaluation
    # =====================================================

    def score(self):
        if self._last_result is None:
            return None

        return self._last_result.metrics

    # =====================================================
    # Utilities
    # =====================================================

    def reset(self) -> None:
        self._pipeline.trainer.reset()
        self._pipeline.predictor.reset()
        self._last_result = None

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(self) -> str:
        model_name = type(self.model).__name__ if self.model is not None else "None"

        return (
            f"{self.__class__.__name__}(trained={self.is_trained}, model={model_name})"
        )
