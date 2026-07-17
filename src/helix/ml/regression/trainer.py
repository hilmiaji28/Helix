"""
HELIX Regression Trainer
"""

from __future__ import annotations

from sklearn.base import RegressorMixin
from sklearn.ensemble import (
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

try:
    from xgboost import XGBRegressor
except ImportError:
    XGBRegressor = None

try:
    from lightgbm import LGBMRegressor
except ImportError:
    LGBMRegressor = None

try:
    from catboost import CatBoostRegressor
except ImportError:
    CatBoostRegressor = None

from helix.ml.common import BaseTrainer

from .config import RegressionConfig


class RegressionTrainer(BaseTrainer):
    """
    Regression trainer.

    Only responsible for creating estimator.
    Training, saving and loading are handled
    by BaseTrainer.
    """

    def __init__(
        self,
        config: RegressionConfig,
    ) -> None:
        super().__init__()

        self.config = config

    def build_estimator(self) -> RegressorMixin:
        algorithm = self.config.algorithm.lower()

        if algorithm == "random_forest":
            return RandomForestRegressor(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "extra_trees":
            return ExtraTreesRegressor(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "gradient_boosting":
            return GradientBoostingRegressor(
                random_state=self.config.random_state,
                **self.config.model_params,
            )

        if algorithm == "xgboost":
            if XGBRegressor is None:
                raise ImportError("xgboost is not installed.")

            return XGBRegressor(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "lightgbm":
            if LGBMRegressor is None:
                raise ImportError("lightgbm is not installed.")

            return LGBMRegressor(
                random_state=self.config.random_state,
                n_jobs=self.config.n_jobs,
                **self.config.model_params,
            )

        if algorithm == "catboost":
            if CatBoostRegressor is None:
                raise ImportError("catboost is not installed.")

            return CatBoostRegressor(
                random_seed=self.config.random_state,
                verbose=False,
                **self.config.model_params,
            )

        raise ValueError(f"Unsupported algorithm: {algorithm}")
