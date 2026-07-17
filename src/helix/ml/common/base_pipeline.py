"""
HELIX Base Pipeline.

Generic machine learning workflow.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.model_selection import train_test_split

from .base_predictor import BasePredictor
from .base_trainer import BaseTrainer


@dataclass(slots=True)
class PipelineResult:
    """
    Result returned by every pipeline.
    """

    estimator: Any
    metrics: Any
    config: Any


class BasePipeline(ABC):
    """
    Generic supervised machine learning pipeline.
    """

    def __init__(
        self,
        trainer: BaseTrainer,
        predictor: BasePredictor,
        test_size: float = 0.2,
        random_state: int = 42,
    ) -> None:
        self.trainer = trainer
        self.predictor = predictor

        self.test_size = test_size
        self.random_state = random_state

    # =====================================================
    # Split
    # =====================================================

    def split(
        self,
        X: pd.DataFrame,
        y: pd.Series,
    ):
        return train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
        )

    # =====================================================
    # Training
    # =====================================================

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        save_path: str | Path | None = None,
    ) -> PipelineResult:
        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = self.split(X, y)

        estimator = self.trainer.fit(
            X_train,
            y_train,
        )

        self.predictor.set_model(estimator)

        prediction = self.predictor.predict(
            X_test,
        )

        metrics = self.evaluate(
            X_test=X_test,
            y_true=y_test,
            y_pred=prediction,
            n_features=X_train.shape[1],
        )

        if save_path is not None:
            self.trainer.save(save_path)

        return PipelineResult(
            estimator=estimator,
            metrics=metrics,
            config=self.config,
        )

    # =====================================================
    # Prediction
    # =====================================================

    def predict(
        self,
        X: pd.DataFrame,
    ):
        return self.predictor.predict(X)

    def predict_dataframe(
        self,
        X: pd.DataFrame,
        column: str = "prediction",
    ):
        return self.predictor.predict_dataframe(
            X,
            column,
        )

    def predict_with_input(
        self,
        X: pd.DataFrame,
        column: str = "prediction",
    ):
        return self.predictor.predict_with_input(
            X,
            column,
        )

    # =====================================================
    # Properties
    # =====================================================

    @property
    def model(self):
        return self.trainer.model

    @property
    def config(self):
        return self.trainer.config

    @property
    def is_trained(self):
        return self.trainer.is_trained

    # =====================================================
    # Evaluation
    # =====================================================

    @abstractmethod
    def evaluate(
        self,
        y_true,
        y_pred,
        **kwargs,
    ):
        """
        Task-specific evaluation.
        """
        raise NotImplementedError
