import plotly.express as px

from .base import AnalyticsService


class VisualizationService(AnalyticsService):
    def histogram(
        self,
        column,
    ):
        return px.histogram(
            self.df,
            x=column,
        )

    def boxplot(
        self,
        column,
    ):
        return px.box(
            self.df,
            y=column,
        )

    def pie(
        self,
        column,
    ):
        return px.pie(
            self.df,
            names=column,
        )

    def bar(
        self,
        x,
        y,
    ):
        return px.bar(
            self.df,
            x=x,
            y=y,
        )

    def scatter(
        self,
        x,
        y,
    ):
        return px.scatter(
            self.df,
            x=x,
            y=y,
        )
