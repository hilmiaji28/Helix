import joblib
from sklearn.model_selection import train_test_split

from helix.core.config import settings

from .dataset import RevenueDataset
from .model import create_model


class RevenueTrainer:
    def train(
        self,
        df,
    ):
        X, y, transformer = RevenueDataset().prepare(df)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=settings.TEST_SIZE,
            random_state=settings.RANDOM_STATE,
        )

        model = create_model()

        model.fit(
            X_train,
            y_train,
        )

        joblib.dump(
            model,
            settings.MODEL_DIR / "revenue_model.pkl",
        )

        joblib.dump(
            transformer,
            settings.MODEL_DIR / "revenue_transformer.pkl",
        )

        return (
            model,
            X_test,
            y_test,
        )
