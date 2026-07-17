"""
HELIX Base Predictor.

Generic predictor for all machine learning tasks.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from .utils import validate_dataframe


class BasePredictor:
    """
    Base predictor.

    Responsibilities
    ----------------
    - Store trained model
    - Perform prediction
    - Return prediction as DataFrame
    - Return prediction with original input
    - Predict probability (if supported)
    """

    def __init__(
        self,
        model: Any | None = None,
    ) -> None:
        self.model = model

    # =====================================================
    # Model Management
    # =====================================================

    def set_model(
        self,
        model: Any,
    ) -> None:
        """
        Assign trained model.
        """

        self.model = model

    def reset(self) -> None:
        """
        Remove model from predictor.
        """

        self.model = None

    @property
    def is_ready(self) -> bool:
        """
        Returns
        -------
        bool
            True if predictor already has a model.
        """

        return self.model is not None

    # =====================================================
    # Prediction
    # =====================================================

    def predict(
        self,
        X: pd.DataFrame,
    ):
        """
        Predict target values.
        """

        if self.model is None:
            raise RuntimeError("Predictor has no model.")

        validate_dataframe(X)

        return self.model.predict(X)

    def predict_dataframe(
        self,
        X: pd.DataFrame,
        column: str = "prediction",
    ) -> pd.DataFrame:
        """
        Return prediction as DataFrame.
        """

        prediction = self.predict(X)

        return pd.DataFrame(
            {
                column: prediction,
            },
            index=X.index,
        )

    def predict_with_input(
        self,
        X: pd.DataFrame,
        column: str = "prediction",
    ) -> pd.DataFrame:
        """
        Append prediction to original dataframe.
        """

        result = X.copy()

        result[column] = self.predict(X)

        return result

    # =====================================================
    # Probability
    # =====================================================

    def predict_proba(
        self,
        X: pd.DataFrame,
    ):
        """
        Predict class probabilities.

        Only available for classifiers.
        """

        if self.model is None:
            raise RuntimeError("Predictor has no model.")

        if not hasattr(
            self.model,
            "predict_proba",
        ):
            raise AttributeError(
                f"{type(self.model).__name__} does not support predict_proba()."
            )

        validate_dataframe(X)

        return self.model.predict_proba(X)

    # =====================================================
    # Callable
    # =====================================================

    def __call__(
        self,
        X: pd.DataFrame,
    ):
        """
        Allow predictor(X).
        """

        return self.predict(X)

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(self) -> str:
        model_name = type(self.model).__name__ if self.model is not None else "None"

        return f"{self.__class__.__name__}(ready={self.is_ready}, model={model_name})"
