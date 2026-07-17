"""
=========================================================
HELIX
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

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_sidebar()

# =====================================================
# HEADER
# =====================================================

st.title("📉 Model Performance")

st.caption("Machine Learning Evaluation Dashboard")

st.divider()

# =====================================================
# PATH
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "processed" / "revenue_final_dataset_v2.csv"

MODEL_PATH = BASE_DIR / "models" / "best_boosting_pipeline.pkl"

# =====================================================
# LOAD MODEL
# =====================================================


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(
            f"""
Model tidak ditemukan.

Lokasi:

{MODEL_PATH}
"""
        )

        st.stop()

    return joblib.load(MODEL_PATH)


# =====================================================
# LOAD DATASET
# =====================================================


@st.cache_data(show_spinner=False)
def load_dataset():
    if not DATA_PATH.exists():
        st.error(
            f"""
Dataset tidak ditemukan.

Lokasi:

{DATA_PATH}
"""
        )

        st.stop()

    return pd.read_csv(DATA_PATH)


# =====================================================
# LOAD RESOURCE
# =====================================================

model = load_model()

df = load_dataset()

# =====================================================
# VALIDATION
# =====================================================

TARGET = "Total_Amount"

if TARGET not in df.columns:
    st.error(f"Kolom target '{TARGET}' tidak ditemukan.")

    st.stop()

st.success("✅ Model dan dataset berhasil dimuat.")

X = df.drop(columns=[TARGET])

y = df[TARGET]

# =====================================================
# PREDICTION
# =====================================================

with st.spinner("Evaluating model..."):
    prediction = model.predict(X)

# =====================================================
# METRICS
# =====================================================

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

r2 = r2_score(
    y,
    prediction,
)

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
        "R² Score",
        f"{r2:.3f}",
    ),
    (
        "Predictions",
        f"{len(prediction):,}",
    ),
)

st.divider()

# =====================================================
# COMPARISON
# =====================================================

compare = pd.DataFrame(
    {
        "Actual Revenue": y,
        "Predicted Revenue": prediction,
    }
)

compare["Residual"] = compare["Actual Revenue"] - compare["Predicted Revenue"]

# =====================================================
# ACTUAL VS PREDICTED
# =====================================================

st.subheader("Actual vs Predicted Revenue")

fig = px.scatter(
    compare,
    x="Actual Revenue",
    y="Predicted Revenue",
    trendline="ols",
    template="plotly_white",
)

fig.update_layout(
    height=600,
    xaxis_title="Actual Revenue",
    yaxis_title="Predicted Revenue",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# =====================================================
# RESIDUAL DISTRIBUTION
# =====================================================

left, right = st.columns(2)

with left:
    st.subheader("Residual Distribution")

    fig = px.histogram(
        compare,
        x="Residual",
        nbins=40,
        template="plotly_white",
    )

    fig.update_layout(
        height=420,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("Residual Plot")

    fig = px.scatter(
        compare,
        x="Predicted Revenue",
        y="Residual",
        template="plotly_white",
    )

    fig.add_hline(
        y=0,
        line_dash="dash",
    )

    fig.update_layout(
        height=420,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.divider()

# =====================================================
# PREDICTION TABLE
# =====================================================

st.subheader("Prediction Result")

st.dataframe(
    compare.round(2),
    use_container_width=True,
    hide_index=True,
    height=500,
)

st.write("")

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

st.subheader("Feature Importance")

try:
    estimator = model

    if hasattr(model, "named_steps"):
        estimator = list(model.named_steps.values())[-1]

    if hasattr(estimator, "feature_importances_"):
        feature_names = X.columns

        importance = pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": estimator.feature_importances_,
            }
        ).sort_values(
            "Importance",
            ascending=False,
        )

        fig = px.bar(
            importance.head(15),
            x="Importance",
            y="Feature",
            orientation="h",
            template="plotly_white",
        )

        fig.update_layout(
            height=600,
            yaxis=dict(categoryorder="total ascending"),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:
        st.info("Feature importance tidak tersedia untuk model ini.")

except Exception as e:
    st.warning(f"Tidak dapat menampilkan feature importance.\n\n{e}")

st.write("")

# =====================================================
# DOWNLOAD
# =====================================================

csv = (
    compare.round(2)
    .to_csv(
        index=False,
    )
    .encode()
)

st.download_button(
    "📥 Download Prediction Result",
    csv,
    file_name="prediction_result.csv",
    mime="text/csv",
    use_container_width=True,
)

st.write("")

# =====================================================
# FOOTER
# =====================================================

st.divider()

left, center, right = st.columns([2, 2, 1])

with left:
    st.caption("© 2026 HELIX")

    st.caption("Enterprise Revenue Intelligence Platform")

with center:
    st.caption("Model Performance")

    st.caption("CatBoost Pipeline Evaluation")

with right:
    st.success("Ready")

st.caption("Built with Streamlit • CatBoost • Scikit-Learn • Plotly")
