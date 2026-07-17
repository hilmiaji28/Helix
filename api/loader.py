"""
Resource loader for HELIX AI Shop API.

Responsible for loading:
- Trained model
- Feature columns
- Feature metadata
- Frequency maps
- Preprocessing metadata
- Feature engineering artifacts
"""

from typing import Any

import joblib

from api.config import settings
from api.feature_engineering import FeatureEngineering
from api.logger import get_logger

logger = get_logger(__name__)


class ResourceLoader:
    """
    Singleton resource loader.

    All resources are loaded once during application startup
    and reused for every request.
    """

    def __init__(self) -> None:
        self.model: Any | None = None

        self.feature_columns: list[str] | None = None

        self.feature_metadata: dict | None = None

        self.frequency_maps: dict | None = None

        self.preprocessing_metadata: dict | None = None

        self.feature_engineering: FeatureEngineering | None = None

    def load(self) -> None:
        """
        Load all application resources.

        Resources are loaded only once during application startup.
        """

        if self.model is not None and self.feature_engineering is not None:
            logger.info("Resources already loaded.")
            return

        logger.info("=" * 60)
        logger.info("Loading HELIX resources...")
        logger.info("=" * 60)

        # ==================================================
        # Load trained model
        # ==================================================

        logger.info("Loading trained model...")

        self.model = joblib.load(settings.model_path)

        logger.info("Model loaded successfully.")

        # ==================================================
        # Load feature columns
        # ==================================================

        logger.info("Loading feature columns...")

        self.feature_columns = joblib.load(settings.feature_columns_path)

        logger.info("Feature columns loaded.")

        # ==================================================
        # Load feature metadata
        # ==================================================

        logger.info("Loading feature metadata...")

        self.feature_metadata = joblib.load(settings.feature_metadata_path)

        logger.info("Feature metadata loaded.")

        # ==================================================
        # Load frequency maps
        # ==================================================

        logger.info("Loading frequency maps...")

        self.frequency_maps = joblib.load(settings.frequency_maps_path)

        logger.info("Frequency maps loaded.")

        # ==================================================
        # Load preprocessing metadata
        # ==================================================

        logger.info("Loading preprocessing metadata...")

        self.preprocessing_metadata = joblib.load(settings.preprocessing_metadata_path)

        logger.info("Preprocessing metadata loaded.")

        # ==================================================
        # Initialize Feature Engineering
        # ==================================================

        logger.info("Initializing Feature Engineering...")

        self.feature_engineering = FeatureEngineering(
            feature_columns_path=settings.feature_columns_path,
            frequency_maps_path=settings.frequency_maps_path,
            preprocessing_metadata_path=settings.preprocessing_metadata_path,
        )

        logger.info("Feature Engineering initialized.")

        logger.info("All HELIX resources loaded successfully.")
        logger.info("=" * 60)

    # ======================================================
    # Getters
    # ======================================================

    def get_model(self) -> Any:
        """
        Return the trained model.
        """
        if self.model is None:
            raise RuntimeError("Model has not been loaded.")

        return self.model

    def get_feature_columns(self) -> list[str]:
        """
        Return feature columns.
        """
        if self.feature_columns is None:
            raise RuntimeError("Feature columns have not been loaded.")

        return self.feature_columns

    def get_feature_metadata(self) -> dict:
        """
        Return feature metadata.
        """
        if self.feature_metadata is None:
            raise RuntimeError("Feature metadata has not been loaded.")

        return self.feature_metadata

    def get_frequency_maps(self) -> dict:
        """
        Return frequency maps.
        """
        if self.frequency_maps is None:
            raise RuntimeError("Frequency maps have not been loaded.")

        return self.frequency_maps

    def get_preprocessing_metadata(self) -> dict:
        """
        Return preprocessing metadata.
        """
        if self.preprocessing_metadata is None:
            raise RuntimeError("Preprocessing metadata has not been loaded.")

        return self.preprocessing_metadata

    def get_feature_engineering(
        self,
    ) -> FeatureEngineering:
        """
        Return FeatureEngineering instance.
        """
        if self.feature_engineering is None:
            raise RuntimeError("FeatureEngineering has not been initialized.")

        return self.feature_engineering


resource_loader = ResourceLoader()
