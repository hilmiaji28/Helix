"""
HELIX Base Trainer.

Abstract base class for all machine learning trainers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import pandas as pd

from .serialization import ModelSerializer


class BaseTrainer(ABC):
    """
    Base trainer for every machine learning task.

    Responsibilities
    ----------------
    - Build estimator
    - Train estimator
    - Save model
    - Load model

    Child classes only need to implement
    `build_estimator()`.
    """

    def __init__(self) -> None:
        self.model: Any | None = None

    # =====================================================
    # Estimator
    # =====================================================

    @abstractmethod
    def build_estimator(self) -> Any:
        """
        Build and return a machine learning estimator.

        Returns
        -------
        Any
            Scikit-learn compatible estimator.
        """
        raise NotImplementedError

    # =====================================================
    # Training
    # =====================================================

    def train(
        self,
        X: pd.DataFrame,
        y: pd.Series | None = None,
    ) -> Any:
        """
        Train estimator.

        Parameters
        ----------
        X : pd.DataFrame
            Feature matrix.

        y : pd.Series | None, default=None
            Target vector.
            Can be None for unsupervised learning.

        Returns
        -------
        Any
            Trained estimator.
        """

        estimator = self.build_estimator()

        if y is None:
            estimator.fit(X)
        else:
            estimator.fit(X, y)

        self.model = estimator

        return estimator

    # sklearn-style alias
    fit = train

    # =====================================================
    # Persistence
    # =====================================================

    def save(
        self,
        path: str | Path,
    ) -> None:
        """
        Save trained model.
        """

        if self.model is None:
            raise RuntimeError("Model has not been trained.")

        ModelSerializer.save_model(
            self.model,
            path,
        )

    def load(
        self,
        path: str | Path,
    ) -> Any:
        """
        Load trained model.
        """

        self.model = ModelSerializer.load_model(
            path,
        )

        return self.model

    # =====================================================
    # Utilities
    # =====================================================

    def reset(self) -> None:
        """
        Remove current model from memory.
        """

        self.model = None

    @property
    def is_trained(self) -> bool:
        """
        Returns
        -------
        bool
            True if trainer already has a model.
        """

        return self.model is not None

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(self) -> str:
        model_name = type(self.model).__name__ if self.model is not None else "None"

        return (
            f"{self.__class__.__name__}(trained={self.is_trained}, model={model_name})"
        )
