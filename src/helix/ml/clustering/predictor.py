import joblib

from helix.core.config import settings


class RevenuePredictor:
    def __init__(self):
        self.model = joblib.load(settings.MODEL_DIR / "revenue_model.pkl")

    def predict(
        self,
        X,
    ):
        return self.model.predict(X)
