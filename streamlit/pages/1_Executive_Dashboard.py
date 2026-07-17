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
    initial_sidebar_state="expanded",
)

# ==========================================================
# SIDEBAR
# ==========================================================

render_sidebar()

# ==========================================================
# HEADER
# ==========================================================

st.title("📈 Executive Dashboard")

st.caption("Business Overview & Revenue Analytics")

st.divider()

# ==========================================================
# DATA PATH
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "processed" / "revenue_final_dataset.csv"

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data(show_spinner=False)
def load_data():
    if not DATA_PATH.exists():
        st.error(
            f"""
Dataset tidak ditemukan.

Lokasi yang dicari:

{DATA_PATH}
"""
        )

        st.stop()

    return pd.read_csv(DATA_PATH)


df = load_data()

# ==========================================================
# BASIC VALIDATION
# ==========================================================

required_columns = [
    "Total_Amount",
    "City",
    "Gender",
    "Product_Category",
    "Payment_Method",
    "Device_Type",
    "Customer_Rating",
    "Delivery_Time_Days",
    "Is_Returning_Customer",
]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    st.error(
        f"""
Dataset tidak sesuai.

Kolom yang hilang:

{missing}
"""
    )

    st.stop()

# ==========================================================
# KPI CALCULATION
# ==========================================================

total_customer = len(df)

total_revenue = df["Total_Amount"].sum()

average_revenue = df["Total_Amount"].mean()

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
        "Average Revenue",
        f"${average_revenue:,.2f}",
    ),
    (
        "Cities",
        total_city,
    ),
)

st.divider()

# ==========================================================
# DATA OVERVIEW
# ==========================================================

left, right = st.columns([3, 1])

with left:
    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True,
    )

with right:
    st.subheader("Dataset Information")

    st.metric(
        "Rows",
        f"{df.shape[0]:,}",
    )

    st.metric(
        "Columns",
        df.shape[1],
    )

    st.metric(
        "Missing Values",
        int(df.isna().sum().sum()),
    )

    st.metric(
        "Unique Cities",
        df["City"].nunique(),
    )

st.write("")

# ==========================================================
# NUMERICAL SUMMARY
# ==========================================================

st.subheader("Numerical Summary")

numeric_df = df.select_dtypes(include="number")

st.dataframe(
    numeric_df.describe().T,
    use_container_width=True,
)

st.write("")

# ==========================================================
# REVENUE DISTRIBUTION
# ==========================================================

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue Distribution")

    fig = histogram(
        df,
        "Total_Amount",
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20,
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with col2:
    st.subheader("Revenue Boxplot")

    fig = boxplot(
        df,
        "Total_Amount",
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20,
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.write("")

# ==========================================================
# TOP PRODUCT CATEGORY
# ==========================================================

st.subheader("Revenue by Product Category")

category_summary = (
    df.groupby("Product_Category")["Total_Amount"]
    .sum()
    .reset_index()
    .sort_values(
        by="Total_Amount",
        ascending=False,
    )
)

fig = px.bar(
    category_summary,
    x="Product_Category",
    y="Total_Amount",
    color="Total_Amount",
    text_auto=".2s",
    template="plotly_white",
)

fig.update_layout(
    height=500,
    xaxis_title="Product Category",
    yaxis_title="Revenue",
    coloraxis_showscale=False,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.write("")

# ==========================================================
# PAYMENT METHOD & DEVICE TYPE
# ==========================================================

st.subheader("Customer Distribution")

left, right = st.columns(2)

with left:
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
        template="plotly_white",
    )

    fig.update_layout(height=430)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
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
        height=430,
        coloraxis_showscale=False,
        xaxis_title="",
        yaxis_title="Customers",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.write("")

# ==========================================================
# CITY REVENUE
# ==========================================================

st.subheader("Revenue by City")

city_summary = (
    df.groupby("City")["Total_Amount"]
    .sum()
    .reset_index()
    .sort_values(
        by="Total_Amount",
        ascending=False,
    )
)

fig = px.bar(
    city_summary,
    x="City",
    y="Total_Amount",
    color="Total_Amount",
    text_auto=".2s",
    template="plotly_white",
)

fig.update_layout(
    height=520,
    xaxis_title="City",
    yaxis_title="Revenue",
    coloraxis_showscale=False,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.write("")

# ==========================================================
# GENDER & CUSTOMER RATING
# ==========================================================

left, right = st.columns(2)

with left:
    st.subheader("Customer Gender")

    gender = df["Gender"].value_counts().reset_index()

    gender.columns = [
        "Gender",
        "Count",
    ]

    fig = px.pie(
        gender,
        names="Gender",
        values="Count",
        hole=0.40,
        template="plotly_white",
    )

    fig.update_layout(height=430)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("Customer Rating")

    fig = px.histogram(
        df,
        x="Customer_Rating",
        nbins=10,
        color="Customer_Rating",
        template="plotly_white",
    )

    fig.update_layout(
        height=430,
        xaxis_title="Rating",
        yaxis_title="Frequency",
        coloraxis_showscale=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.write("")

# ==========================================================
# RETURNING CUSTOMER
# ==========================================================

st.subheader("Returning Customer")

left, right = st.columns([1, 2])

with left:
    returning = df["Is_Returning_Customer"].value_counts().reset_index()

    returning.columns = [
        "Returning",
        "Count",
    ]

    fig = px.pie(
        returning,
        names="Returning",
        values="Count",
        hole=0.50,
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
    rating = df.groupby("Is_Returning_Customer")["Customer_Rating"].mean().reset_index()

    fig = px.bar(
        rating,
        x="Is_Returning_Customer",
        y="Customer_Rating",
        color="Customer_Rating",
        text_auto=".2f",
        template="plotly_white",
    )

    fig.update_layout(
        height=420,
        xaxis_title="Returning Customer",
        yaxis_title="Average Rating",
        coloraxis_showscale=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.write("")

# ==========================================================
# DELIVERY TIME
# ==========================================================

st.subheader("Delivery Time Distribution")

fig = px.box(
    df,
    y="Delivery_Time_Days",
    points="outliers",
    template="plotly_white",
)

fig.update_layout(
    height=450,
    yaxis_title="Delivery Time (Days)",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.write("")

# ==========================================================
# CORRELATION MATRIX
# ==========================================================

st.subheader("Correlation Matrix")

numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr(numeric_only=True)

fig = px.imshow(
    corr.round(2),
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="Blues",
)

fig.update_layout(
    height=700,
    margin=dict(
        l=20,
        r=20,
        t=50,
        b=20,
    ),
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.write("")

# ==========================================================
# QUICK DATA INSIGHT
# ==========================================================

with st.container(border=True):
    st.subheader("Dataset Insight")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Highest Revenue",
            f"${df['Total_Amount'].max():,.2f}",
        )

    with col2:
        st.metric(
            "Average Rating",
            f"{df['Customer_Rating'].mean():.2f}",
        )

    with col3:
        st.metric(
            "Average Delivery",
            f"{df['Delivery_Time_Days'].mean():.2f} Days",
        )

st.write("")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

left, center, right = st.columns([2, 2, 1])

with left:
    st.caption("© 2026 HELIX AI SHOP")

    st.caption("Enterprise Machine Learning Platform")

with center:
    st.caption("Executive Dashboard")

    st.caption("Revenue Analytics")

with right:
    st.success("Ready")

st.caption("Built with Streamlit • Plotly • Pandas • FastAPI")
