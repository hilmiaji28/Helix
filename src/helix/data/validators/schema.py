import pandas as pd

from .base import BaseValidator


class SchemaValidator(BaseValidator):
    def validate(
        self,
        df: pd.DataFrame,
    ):
        invalid = []

        for col in df.columns:
            if not col.strip():
                invalid.append(col)

        return {"invalid_columns": invalid}
