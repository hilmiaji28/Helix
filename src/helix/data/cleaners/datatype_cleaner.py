import pandas as pd

from .base import BaseCleaner


class DatatypeCleaner(BaseCleaner):
    """
    Convert obvious datatypes.
    """

    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        for col in df.columns:
            if "date" in col.lower():
                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce",
                )

        return df
