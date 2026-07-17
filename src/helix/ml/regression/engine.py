"""
HELIX Regression Engine
"""

from __future__ import annotations

from helix.ml.common import BaseEngine

from .config import RegressionConfig
from .pipeline import RegressionPipeline
from .predictor import RegressionPredictor
from .trainer import RegressionTrainer


class RegressionEngine(BaseEngine):
    """
    Regression Engine.
    """

    def __init__(
        self,
        config: RegressionConfig,
    ) -> None:
        trainer = RegressionTrainer(config)

        predictor = RegressionPredictor()

        pipeline = RegressionPipeline(
            trainer=trainer,
            predictor=predictor,
            test_size=config.test_size,
            random_state=config.random_state,
        )

        super().__init__(pipeline)
