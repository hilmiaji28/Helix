"""
HELIX Classification Engine.
"""

from __future__ import annotations

from helix.ml.common import BaseEngine

from .config import ClassificationConfig
from .pipeline import ClassificationPipeline
from .predictor import ClassificationPredictor
from .trainer import ClassificationTrainer


class ClassificationEngine(BaseEngine):
    """
    Classification Engine.
    """

    def __init__(
        self,
        config: ClassificationConfig,
    ) -> None:
        trainer = ClassificationTrainer(config)

        predictor = ClassificationPredictor()

        pipeline = ClassificationPipeline(
            trainer=trainer,
            predictor=predictor,
            test_size=config.test_size,
            random_state=config.random_state,
        )

        super().__init__(pipeline)
