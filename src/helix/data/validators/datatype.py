import pandas as pd

from .base import BaseValidator


class DatatypeValidator(BaseValidator):
    def validate(
        self,
        df: pd.DataFrame,
    ):
        return {"dtypes": df.dtypes.astype(str).to_dict()}
