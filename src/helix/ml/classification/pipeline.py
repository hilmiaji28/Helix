"""
HELIX Classification Pipeline.
"""

from __future__ import annotations

from helix.ml.common import BasePipeline

from .metrics import ClassificationMetrics


class ClassificationPipeline(BasePipeline):
    """
    Classification pipeline.
    """

    def evaluate(
        self,
        y_true,
        y_pred,
        **kwargs,
    ):
        y_score = None

        try:
            y_score = self.predictor.predict_proba(kwargs["X_test"])

        except Exception:
            y_score = None

        return ClassificationMetrics.evaluate(
            y_true=y_true,
            y_pred=y_pred,
            y_score=y_score,
        )
