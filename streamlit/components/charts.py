"""
Reusable Charts
"""

import plotly.express as px


def histogram(
    df,
    column,
):
    fig = px.histogram(
        df,
        x=column,
        template="plotly_white",
    )

    fig.update_layout(
        height=420,
    )

    return fig


def boxplot(
    df,
    column,
):
    fig = px.box(
        df,
        y=column,
        template="plotly_white",
    )

    fig.update_layout(
        height=420,
    )

    return fig


def scatter(
    df,
    x,
    y,
):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        template="plotly_white",
    )

    fig.update_layout(
        height=450,
    )

    return fig


def correlation(
    corr_df,
):
    fig = px.imshow(
        corr_df,
        text_auto=True,
        color_continuous_scale="Blues",
    )

    return fig
