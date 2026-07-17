import pandas as pd

from .base import BaseCleaner


class DuplicateCleaner(BaseCleaner):
    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        return df.drop_duplicates()
