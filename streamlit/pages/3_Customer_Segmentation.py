"""
=========================================================
HELIX AI SHOP
Customer Segmentation
=========================================================
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
from components.metrics import four_metrics
from components.sidebar import render_sidebar

import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide",
)

render_sidebar()

st.title("👥 Customer Segmentation")

st.caption("Analyze customer behavior using AI clustering.")

st.divider()

DATA_PATH = Path("data/processed/customer_segment.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

segment_count = df["Segment"].nunique()

customer = len(df)

avg_purchase = df["Purchase_Amount"].mean()

revenue = df["Purchase_Amount"].sum()

four_metrics(
    (
        "Segments",
        segment_count,
    ),
    (
        "Customers",
        customer,
    ),
    (
        "Average Purchase",
        f"${avg_purchase:.2f}",
    ),
    (
        "Revenue",
        f"${revenue:,.0f}",
    ),
)

st.divider()

st.subheader("Customer Segment Distribution")

segment = df["Segment"].value_counts().reset_index()

segment.columns = [
    "Segment",
    "Count",
]

fig = px.pie(
    segment,
    names="Segment",
    values="Count",
    hole=0.45,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.subheader("Revenue by Segment")

summary = df.groupby("Segment")["Purchase_Amount"].sum().reset_index()

fig = px.bar(
    summary,
    x="Segment",
    y="Purchase_Amount",
    color="Purchase_Amount",
    text_auto=True,
    template="plotly_white",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

rating = df.groupby("Segment")["Customer_Rating"].mean().reset_index()

fig = px.bar(
    rating,
    x="Segment",
    y="Customer_Rating",
    color="Customer_Rating",
    template="plotly_white",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

fig = px.scatter(
    df,
    x="PCA1",
    y="PCA2",
    color="Segment",
    hover_data=[
        "Purchase_Amount",
        "Age",
        "City",
    ],
    template="plotly_white",
)

fig.update_layout(
    height=650,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

profile = (
    df.groupby("Segment")
    .agg(
        {
            "Purchase_Amount": "mean",
            "Age": "mean",
            "Customer_Rating": "mean",
        }
    )
    .round(2)
)

st.subheader("Segment Profile")

st.dataframe(
    profile,
    use_container_width=True,
)

st.divider()

st.subheader("AI Insight")

top_segment = summary.sort_values(
    "Purchase_Amount",
    ascending=False,
).iloc[0]["Segment"]

st.success(
    f"""

### Executive Summary

Highest Revenue Segment

**{top_segment}**

Recommendation

• Increase loyalty rewards

• Personalized campaign

• Premium recommendation

• Exclusive voucher

"""
)

csv = df.to_csv(
    index=False,
).encode()

st.download_button(
    "Download Segment Data",
    csv,
    file_name="customer_segment.csv",
    mime="text/csv",
)
