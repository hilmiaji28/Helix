"""
=========================================================
HELIX Executive Dashboard
=========================================================
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
from components.charts import (
    boxplot,
    histogram,
)
from components.metrics import four_metrics
from components.sidebar import render_sidebar

import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📈",
    layout="wide",
)

render_sidebar()

st.title("📈 Executive Dashboard")

st.caption("Business overview of HELIX AI Shop")

st.divider()

# ==========================================================
# DATA
# ==========================================================

DATA_PATH = Path("data/processed/revenue_final_dataset.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

# ==========================================================
# KPI
# ==========================================================

total_customer = len(df)

total_revenue = df["Purchase_Amount"].sum()

avg_purchase = df["Purchase_Amount"].mean()

total_city = df["City"].nunique()

four_metrics(
    (
        "Revenue",
        f"${total_revenue:,.0f}",
    ),
    (
        "Customers",
        f"{total_customer:,}",
    ),
    (
        "Average Purchase",
        f"${avg_purchase:.2f}",
    ),
    (
        "Cities",
        total_city,
    ),
)

st.divider()

# ==========================================================
# DATA PREVIEW
# ==========================================================

left, right = st.columns([3, 1])

with left:
    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
    )

with right:
    st.subheader("Dataset")

    st.info(
        f"""
Rows

{df.shape[0]:,}

Columns

{df.shape[1]}

Missing

{df.isna().sum().sum()}
"""
    )

# ==========================================================
# NUMERICAL SUMMARY
# ==========================================================

st.divider()

st.subheader("Numerical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True,
)

# ==========================================================
# DISTRIBUTION
# ==========================================================

st.divider()

st.subheader("Purchase Amount Distribution")

fig = histogram(
    df,
    "Purchase_Amount",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ==========================================================
# OUTLIER
# ==========================================================

st.subheader("Purchase Amount Boxplot")

fig = boxplot(
    df,
    "Purchase_Amount",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ==========================================================
# PRODUCT CATEGORY ANALYSIS
# ==========================================================

st.divider()

st.subheader("📦 Revenue by Product Category")

category_summary = (
    df.groupby("Product_Category")["Purchase_Amount"]
    .sum()
    .reset_index()
    .sort_values(
        by="Purchase_Amount",
        ascending=False,
    )
)

fig = px.bar(
    category_summary,
    x="Product_Category",
    y="Purchase_Amount",
    color="Purchase_Amount",
    text_auto=".2s",
    template="plotly_white",
)

fig.update_layout(
    height=500,
    xaxis_title="Product Category",
    yaxis_title="Revenue",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ==========================================================
# PAYMENT METHOD
# ==========================================================

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("💳 Payment Method")

    payment = df["Payment_Method"].value_counts().reset_index()

    payment.columns = [
        "Payment_Method",
        "Count",
    ]

    fig = px.pie(
        payment,
        names="Payment_Method",
        values="Count",
        hole=0.45,
    )

    fig.update_layout(
        height=450,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("📱 Device Type")

    device = df["Device_Type"].value_counts().reset_index()

    device.columns = [
        "Device",
        "Count",
    ]

    fig = px.bar(
        device,
        x="Device",
        y="Count",
        color="Count",
        text_auto=True,
        template="plotly_white",
    )

    fig.update_layout(
        height=450,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

# ==========================================================
# CITY ANALYSIS
# ==========================================================

st.divider()

st.subheader("🌍 Top Revenue by City")

city = (
    df.groupby("City")["Purchase_Amount"]
    .sum()
    .reset_index()
    .sort_values(
        by="Purchase_Amount",
        ascending=False,
    )
)

fig = px.bar(
    city,
    x="City",
    y="Purchase_Amount",
    color="Purchase_Amount",
    text_auto=".2s",
    template="plotly_white",
)

fig.update_layout(
    height=500,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ==========================================================
# GENDER
# ==========================================================

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("👤 Gender")

    gender = df["Gender"].value_counts().reset_index()

    gender.columns = [
        "Gender",
        "Count",
    ]

    fig = px.pie(
        gender,
        names="Gender",
        values="Count",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("⭐ Customer Rating")

    fig = px.histogram(
        df,
        x="Customer_Rating",
        nbins=10,
        template="plotly_white",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

# ==========================================================
# RETURNING CUSTOMER
# ==========================================================

st.divider()

st.subheader("🔄 Returning Customer")

returning = df["Is_Returning_Customer"].value_counts().reset_index()

returning.columns = [
    "Returning",
    "Count",
]

fig = px.pie(
    returning,
    names="Returning",
    values="Count",
    hole=0.5,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ==========================================================
# DELIVERY TIME
# ==========================================================

st.divider()

st.subheader("🚚 Delivery Time")

fig = px.box(
    df,
    y="Delivery_Time_Days",
    template="plotly_white",
)

fig.update_layout(
    height=450,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ==========================================================
# CORRELATION
# ==========================================================

st.divider()

st.subheader("📊 Correlation Matrix")

numeric = df.select_dtypes(include="number")

corr = numeric.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues",
)

fig.update_layout(
    height=700,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.divider()

st.caption("HELIX AI SHOP • Executive Dashboard • 2026")
