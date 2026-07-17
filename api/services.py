"""
Business services for HELIX AI Shop API.
"""

from api.loader import resource_loader
from api.logger import get_logger

logger = get_logger(__name__)


class PredictionService:
    """
    Service responsible for generating purchase predictions.
    """

    def predict(self, payload: dict) -> dict:
        """
        Run feature engineering and model prediction.
        """

        logger.info("Prediction request received.")

        model = resource_loader.get_model()

        feature_engineering = resource_loader.get_feature_engineering()

        logger.info("Running feature engineering...")

        features = feature_engineering.transform(payload)

        logger.info("Feature engineering completed.")

        logger.info("Running model prediction...")

        try:
            prediction = model.predict(features)[0]

        except Exception:
            logger.exception("Prediction service failed.")
            raise

        logger.info("Prediction completed successfully.")

        return {
            "predicted_purchase_amount": round(
                float(prediction),
                2,
            )
        }


prediction_service = PredictionService()
