import pandas as pd

from .base import BaseValidator


class DuplicateValidator(BaseValidator):
    def validate(
        self,
        df: pd.DataFrame,
    ):
        duplicate = int(df.duplicated().sum())

        return {"duplicates": duplicate}
