from __future__ import annotations

import pandas as pd

from helix.core.logging import get_logger
from helix.data.cleaners.pipeline import CleaningPipeline
from helix.data.loaders.csv_loader import CSVLoader
from helix.data.profilers.pipeline import ProfilingPipeline
from helix.data.stores.feature_store import FeatureStore
from helix.data.validators.pipeline import ValidationPipeline

logger = get_logger(__name__)


class DataPipeline:
    """
    Main Data Pipeline.

    Pipeline Flow

    Raw CSV
        ↓
    Validation
        ↓
    Cleaning
        ↓
    Profiling
        ↓
    Feature Store
    """

    def __init__(self):
        self.validator = ValidationPipeline()

        self.cleaner = CleaningPipeline()

        self.profiler = ProfilingPipeline()

        self.store = FeatureStore()

    def run(
        self,
        filename: str,
    ) -> pd.DataFrame:
        logger.info("=" * 60)

        logger.info("HELIX DATA PIPELINE")

        logger.info("=" * 60)

        loader = CSVLoader(filename)

        df = loader.load()

        logger.info("Running validation...")

        self.validator.run(df)

        logger.info("Validation passed.")

        logger.info("Cleaning dataset...")

        df = self.cleaner.run(df)

        logger.info("Generating data profile...")

        self.profiler.run(df)

        logger.info("Saving processed dataset...")

        self.store.save_dataframe(
            "processed_dataset",
            df,
        )

        logger.info("Pipeline finished.")

        return df
