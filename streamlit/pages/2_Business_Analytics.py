"""
=====================================================
HELIX AI SHOP
Business Analytics
=====================================================
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
from components.metrics import four_metrics
from components.sidebar import render_sidebar

import streamlit as st

# =====================================================
# PAGE
# =====================================================

st.set_page_config(
    page_title="Business Analytics",
    page_icon="📊",
    layout="wide",
)

render_sidebar()

st.title("📊 Business Analytics")

st.caption("Interactive business analysis dashboard")

st.divider()

# =====================================================
# DATA
# =====================================================

DATA_PATH = Path("data/processed/revenue_final_dataset.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

# =====================================================
# FILTER
# =====================================================

st.sidebar.markdown("---")
st.sidebar.header("🔎 Analytics Filter")

city = st.sidebar.multiselect(
    "City",
    sorted(df["City"].unique()),
)

category = st.sidebar.multiselect(
    "Product Category",
    sorted(df["Product_Category"].unique()),
)

payment = st.sidebar.multiselect(
    "Payment Method",
    sorted(df["Payment_Method"].unique()),
)

device = st.sidebar.multiselect(
    "Device Type",
    sorted(df["Device_Type"].unique()),
)

filtered = df.copy()

if city:
    filtered = filtered[filtered["City"].isin(city)]

if category:
    filtered = filtered[filtered["Product_Category"].isin(category)]

if payment:
    filtered = filtered[filtered["Payment_Method"].isin(payment)]

if device:
    filtered = filtered[filtered["Device_Type"].isin(device)]

four_metrics(
    (
        "Revenue",
        f"${filtered['Purchase_Amount'].sum():,.0f}",
    ),
    (
        "Customers",
        f"{len(filtered):,}",
    ),
    (
        "Average",
        f"${filtered['Purchase_Amount'].mean():.2f}",
    ),
    (
        "Cities",
        filtered["City"].nunique(),
    ),
)

st.divider()

st.subheader("📈 Revenue Trend")

trend = filtered.groupby("Transaction_Date")["Purchase_Amount"].sum().reset_index()

fig = px.line(
    trend,
    x="Transaction_Date",
    y="Purchase_Amount",
    markers=True,
    template="plotly_white",
)

fig.update_layout(
    height=500,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

left, right = st.columns(2)

with left:
    st.subheader("Revenue by Category")

    category_df = (
        filtered.groupby("Product_Category")["Purchase_Amount"].sum().reset_index()
    )

    fig = px.bar(
        category_df,
        x="Product_Category",
        y="Purchase_Amount",
        color="Purchase_Amount",
        text_auto=".2s",
        template="plotly_white",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("Payment Distribution")

    payment_df = filtered["Payment_Method"].value_counts().reset_index()

    payment_df.columns = [
        "Payment",
        "Count",
    ]

    fig = px.pie(
        payment_df,
        names="Payment",
        values="Count",
        hole=0.45,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Customer Rating")

    fig = px.histogram(
        filtered,
        x="Customer_Rating",
        nbins=10,
        template="plotly_white",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("Returning Customer")

    returning = filtered["Is_Returning_Customer"].value_counts().reset_index()

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

st.divider()

st.subheader("🏆 Top City Revenue")

city_df = (
    filtered.groupby("City")["Purchase_Amount"]
    .sum()
    .reset_index()
    .sort_values(
        by="Purchase_Amount",
        ascending=False,
    )
)

fig = px.bar(
    city_df,
    x="City",
    y="Purchase_Amount",
    color="Purchase_Amount",
    text_auto=".2s",
    template="plotly_white",
)

fig.update_layout(
    height=550,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.divider()

st.subheader("Filtered Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    height=400,
)

st.divider()

st.subheader("🧠 Business Insights")

revenue = filtered["Purchase_Amount"].sum()
avg_purchase = filtered["Purchase_Amount"].mean()
top_city = filtered.groupby("City")["Purchase_Amount"].sum().idxmax()
top_category = filtered.groupby("Product_Category")["Purchase_Amount"].sum().idxmax()

st.success(
    f"""
### Executive Summary

- Total Revenue: **${revenue:,.0f}**
- Average Purchase: **${avg_purchase:.2f}**
- Top Performing City: **{top_city}**
- Best Selling Category: **{top_category}**

#### Recommendations

- Fokuskan promosi pada **{top_city}** karena memberikan kontribusi revenue tertinggi.
- Tingkatkan stok dan kampanye untuk kategori **{top_category}**.
- Gunakan filter di panel kiri untuk membandingkan performa antar kota, kategori produk, metode pembayaran, dan perangkat yang digunakan pelanggan.
"""
)
