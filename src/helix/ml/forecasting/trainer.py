"""
HELIX Forecast Trainer.

Forecasting uses the same regression estimators.
"""

from __future__ import annotations

from helix.ml.regression.trainer import RegressionTrainer


class ForecastTrainer(RegressionTrainer):
    """
    Forecast trainer.

    Reuses RegressionTrainer implementation.
    """

    pass
