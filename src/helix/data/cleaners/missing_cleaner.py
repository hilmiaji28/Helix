import pandas as pd

from .base import BaseCleaner


class MissingCleaner(BaseCleaner):
    """
    Only remove completely empty rows.
    Feature imputation happens later
    inside FeaturePipeline.
    """

    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        return df.dropna(how="all")
