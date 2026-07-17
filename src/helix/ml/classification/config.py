"""
HELIX Classification Configuration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ClassificationConfig:
    """
    Configuration for classification engine.
    """

    # General
    random_state: int = 42
    test_size: float = 0.2

    # Parallel
    n_jobs: int = -1

    # Algorithm
    algorithm: str = "random_forest"

    # Hyperparameters
    model_params: dict[str, Any] = field(default_factory=dict)

    # Save
    save_model: bool = True

    # MLflow
    enable_mlflow: bool = True

    # Dataset
    target_column: str = "target"

    feature_columns: list[str] = field(default_factory=list)

    # Experiment
    experiment_name: str = "Classification"

    run_name: str = "Baseline"
