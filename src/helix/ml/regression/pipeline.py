"""
HELIX Regression Pipeline
"""

from __future__ import annotations

from helix.ml.common import BasePipeline

from .metrics import RegressionMetrics


class RegressionPipeline(BasePipeline):
    def evaluate(
        self,
        y_true,
        y_pred,
        **kwargs,
    ):
        return RegressionMetrics.evaluate(
            y_true=y_true,
            y_pred=y_pred,
            n_features=kwargs["n_features"],
        )
