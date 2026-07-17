from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ForecastConfig:
    random_state: int = 42

    algorithm: str = "xgboost"

    horizon: int = 12

    n_splits: int = 5

    model_params: dict[str, Any] = field(default_factory=dict)

    save_model: bool = True

    enable_mlflow: bool = True

    target_column: str = "target"

    feature_columns: list[str] = field(default_factory=list)

    experiment_name: str = "Forecast"

    run_name: str = "Baseline"
