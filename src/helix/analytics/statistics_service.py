from .base import AnalyticsService


class StatisticsService(AnalyticsService):
    def describe(self):
        return self.df.describe()

    def missing_values(self):
        return self.df.isna().sum()

    def duplicate_rows(self):
        return int(self.df.duplicated().sum())

    def correlation(self):
        return self.df.corr(numeric_only=True)
