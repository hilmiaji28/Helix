"""
HELIX Engine Registry.
"""

from __future__ import annotations

from enum import Enum

from helix.ml.classification import (
    ClassificationConfig,
    ClassificationEngine,
)
from helix.ml.clustering import (
    ClusteringConfig,
    ClusteringEngine,
)
from helix.ml.forecasting import (
    ForecastConfig,
    ForecastEngine,
)
from helix.ml.regression import (
    RegressionConfig,
    RegressionEngine,
)


class TaskType(str, Enum):
    """
    Supported machine learning tasks.
    """

    REGRESSION = "regression"
    CLASSIFICATION = "classification"
    FORECASTING = "forecasting"
    CLUSTERING = "clustering"


ENGINE_REGISTRY: dict[
    TaskType,
    tuple[type[object], type[object]],
] = {
    TaskType.REGRESSION: (
        RegressionEngine,
        RegressionConfig,
    ),
    TaskType.CLASSIFICATION: (
        ClassificationEngine,
        ClassificationConfig,
    ),
    TaskType.FORECASTING: (
        ForecastEngine,
        ForecastConfig,
    ),
    TaskType.CLUSTERING: (
        ClusteringEngine,
        ClusteringConfig,
    ),
}
