from __future__ import annotations

from helix.ml.common import BaseEngine

from .config import ForecastConfig
from .pipeline import ForecastPipeline
from .predictor import ForecastPredictor
from .trainer import ForecastTrainer


class ForecastEngine(BaseEngine):
    def __init__(
        self,
        config: ForecastConfig,
    ):
        trainer = ForecastTrainer(config)

        predictor = ForecastPredictor()

        pipeline = ForecastPipeline(
            trainer=trainer,
            predictor=predictor,
            n_splits=config.n_splits,
        )

        super().__init__(pipeline)
