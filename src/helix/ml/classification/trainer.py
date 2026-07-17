"""
HELIX Classification Trainer.
"""

from __future__ import annotations

from sklearn.base import ClassifierMixin
from sklearn.ensemble import (
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression

try:
    from xgboost import XGBClassifier
except ImportError:
    XGBClassifier = None

try:
    from lightgbm import LGBMClassifier
except ImportError:
    LGBMClassifier = None

try:
    from catboost import CatBoostClassifier
except ImportError:
    CatBoostClassifier = None

from helix.ml.common import BaseTrainer

from .config import ClassificationConfig


class ClassificationTrainer(BaseTrainer):
    """
    Classification trainer.

    Only responsible for creating estimator.
    """

    def __init__(
        self,
        config: ClassificationConfig,
    ) -> None:
        super().__init__()

        self.config = config

    def build_estimator(self) -> ClassifierMixin:
        algorithm = self.config.algorithm.lower()

        if algorithm == "random_forest":
            return RandomForestClassifier(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "extra_trees":
            return ExtraTreesClassifier(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "gradient_boosting":
            return GradientBoostingClassifier(
                random_state=self.config.random_state,
                **self.config.model_params,
            )

        if algorithm == "logistic_regression":
            return LogisticRegression(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "xgboost":
            if XGBClassifier is None:
                raise ImportError("xgboost is not installed.")

            return XGBClassifier(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                eval_metric="logloss",
                **self.config.model_params,
            )

        if algorithm == "lightgbm":
            if LGBMClassifier is None:
                raise ImportError("lightgbm is not installed.")

            return LGBMClassifier(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "catboost":
            if CatBoostClassifier is None:
                raise ImportError("catboost is not installed.")

            return CatBoostClassifier(
                random_seed=self.config.random_state,
                verbose=False,
                **self.config.model_params,
            )

        raise ValueError(f"Unsupported algorithm: {algorithm}")
