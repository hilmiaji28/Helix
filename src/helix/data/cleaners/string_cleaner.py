import pandas as pd

from .base import BaseCleaner


class StringCleaner(BaseCleaner):
    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        object_columns = df.select_dtypes(include="object").columns

        for col in object_columns:
            df[col] = df[col].astype(str).str.strip().replace("nan", None)

        return df
