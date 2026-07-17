from .base import AnalyticsService


class EDAService(AnalyticsService):
    def numeric_columns(self):
        return self.df.select_dtypes(include="number").columns.tolist()

    def categorical_columns(self):
        return self.df.select_dtypes(exclude="number").columns.tolist()

    def unique_values(self):
        result = {}

        for col in self.categorical_columns():
            result[col] = self.df[col].nunique()

        return result
