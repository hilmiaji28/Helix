import pandas as pd


class OutlierValidator:
    def validate(
        self,
        df: pd.DataFrame,
    ):
        numeric = df.select_dtypes(include="number")

        result = {}

        for col in numeric.columns:
            q1 = numeric[col].quantile(0.25)

            q3 = numeric[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr

            upper = q3 + 1.5 * iqr

            count = ((numeric[col] < lower) | (numeric[col] > upper)).sum()

            result[col] = int(count)

        return result
