import pandas as pd


class AnalyticsService:
    """
    Base class for analytics services.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
