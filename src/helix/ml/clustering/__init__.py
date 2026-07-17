import joblib
import pandas as pd

from helix.core.config import settings


class RevenueInference:
    def __init__(self):
        self.transformer = joblib.load(settings.MODEL_DIR / "revenue_transformer.pkl")

        self.model = joblib.load(settings.MODEL_DIR / "revenue_model.pkl")

    def predict(
        self,
        df: pd.DataFrame,
    ):
        X = self.transformer.transform(df)

        return self.model.predict(X)
