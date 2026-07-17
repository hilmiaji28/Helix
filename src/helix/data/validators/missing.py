import pandas as pd

from .base import BaseValidator


class MissingValidator(BaseValidator):
    def validate(
        self,
        df: pd.DataFrame,
    ):
        missing = df.isna().sum()

        return {
            "total_missing": int(missing.sum()),
            "per_column": missing.to_dict(),
        }
