from helix.core.io import IOManager
from helix.core.paths import FEATURE_DIR

from .base import BaseStore


class FeatureStore(BaseStore):
    def save_dataframe(
        self,
        name,
        df,
    ):
        path = FEATURE_DIR / f"{name}.parquet"

        IOManager.save_parquet(
            df,
            path,
        )

    def load_dataframe(
        self,
        name,
    ):
        path = FEATURE_DIR / f"{name}.parquet"

        return IOManager.load_parquet(path)
