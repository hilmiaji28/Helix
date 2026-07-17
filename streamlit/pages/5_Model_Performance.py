"""
=========================================================
HELIX AI SHOP
Model Performance
=========================================================
"""

from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
from components.metrics import four_metrics
from components.sidebar import render_sidebar
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

import streamlit as st

st.set_page_config(
    page_title="Model Performance",
    page_icon="📉",
    layout="wide",
)

render_sidebar()

st.title("📉 Model Performance")

st.caption("Evaluate Machine Learning Model")

st.divider()

DATA_PATH = Path("data/processed/test_prediction.csv")

MODEL_PATH = Path("models/catboost_model.pkl")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_dataset():
    return pd.read_csv(DATA_PATH)


model = load_model()

df = load_dataset()

X = df.drop(columns=["Purchase_Amount"])

y = df["Purchase_Amount"]

prediction = model.predict(X)

mae = mean_absolute_error(
    y,
    prediction,
)

rmse = (
    mean_squared_error(
        y,
        prediction,
    )
    ** 0.5
)

r2 = r2_score(y, prediction)

four_metrics(
    (
        "MAE",
        f"{mae:.2f}",
    ),
    (
        "RMSE",
        f"{rmse:.2f}",
    ),
    (
        "R²",
        f"{r2:.3f}",
    ),
    (
        "Prediction",
        len(prediction),
    ),
)

st.divider()

compare = pd.DataFrame(
    {
        "Actual": y,
        "Prediction": prediction,
    }
)

fig = px.scatter(
    compare,
    x="Actual",
    y="Prediction",
    trendline="ols",
    template="plotly_white",
)

fig.update_layout(
    height=650,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

compare["Error"] = compare["Actual"] - compare["Prediction"]

fig = px.histogram(
    compare,
    x="Error",
    nbins=40,
    template="plotly_white",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

fig = px.scatter(
    compare,
    x="Prediction",
    y="Error",
    template="plotly_white",
)

fig.add_hline(
    y=0,
    line_dash="dash",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.subheader("Prediction Result")

st.dataframe(
    compare,
    height=500,
    use_container_width=True,
)

csv = compare.to_csv(
    index=False,
).encode()

st.download_button(
    "⬇ Download Prediction Result",
    csv,
    file_name="prediction_result.csv",
    mime="text/csv",
)
