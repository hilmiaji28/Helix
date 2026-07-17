"""
Classification Metrics.
"""

from __future__ import annotations

from dataclasses import dataclass

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


@dataclass(slots=True)
class ClassificationResult:
    accuracy: float

    precision: float

    recall: float

    f1: float

    roc_auc: float | None = None


class ClassificationMetrics:
    """
    Classification evaluation.
    """

    @staticmethod
    def evaluate(
        y_true,
        y_pred,
        y_score=None,
        **kwargs,
    ) -> ClassificationResult:
        accuracy = accuracy_score(
            y_true,
            y_pred,
        )

        precision = precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        recall = recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        f1 = f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        roc_auc = None

        if y_score is not None:
            try:
                roc_auc = roc_auc_score(
                    y_true,
                    y_score,
                    multi_class="ovr",
                )

            except Exception:
                roc_auc = None

        return ClassificationResult(
            accuracy=accuracy,
            precision=precision,
            recall=recall,
            f1=f1,
            roc_auc=roc_auc,
        )
