"""
Regression configuration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RegressionConfig:
    """
    Configuration for regression engine.
    """

    # General
    random_state: int = 42
    test_size: float = 0.2
    validation_size: float = 0.2

    # Training
    cv: int = 5
    n_jobs: int = -1

    # Model
    algorithm: str = "xgboost"

    model_params: dict[str, Any] = field(default_factory=dict)

    # Save
    save_model: bool = True
    save_metrics: bool = True

    # MLflow
    enable_mlflow: bool = True

    # Feature
    target_column: str = "target"

    feature_columns: list[str] = field(default_factory=list)

    # Experiment
    experiment_name: str = "Regression"

    run_name: str = "Baseline"
