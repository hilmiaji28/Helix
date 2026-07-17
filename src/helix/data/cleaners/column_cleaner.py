import re

import pandas as pd

from .base import BaseCleaner


class ColumnCleaner(BaseCleaner):
    """
    Standardize column names.
    """

    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        columns = []

        for col in df.columns:
            col = col.strip().lower()

            col = re.sub(r"\s+", "_", col)

            col = re.sub(r"[^a-z0-9_]", "", col)

            columns.append(col)

        df.columns = columns

        return df
