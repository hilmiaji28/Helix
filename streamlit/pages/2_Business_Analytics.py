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
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Business Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_sidebar()

# =====================================================
# HEADER
# =====================================================

st.title("📊 Business Analytics")

st.caption("Interactive Business Analytics Dashboard")

st.divider()

# =====================================================
# DATA
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "processed" / "revenue_final_dataset_v2.csv"

# =====================================================
# LOAD DATA
# =====================================================


@st.cache_data(show_spinner=False)
def load_data():
    if not DATA_PATH.exists():
        st.error(
            f"""
Dataset tidak ditemukan.

Lokasi:

{DATA_PATH}
"""
        )

        st.stop()

    df = pd.read_csv(DATA_PATH)

    return df


df = load_data()

# =====================================================
# DATA VALIDATION
# =====================================================

required_columns = [
    "Total_Amount",
    "City",
    "Product_Category",
    "Payment_Method",
    "Device_Type",
    "Customer_Rating",
    "Month",
    "Gender",
    "Is_Returning_Customer",
]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    st.error(
        f"""
Dataset tidak sesuai.

Kolom berikut tidak ditemukan:

{missing}
"""
    )

    st.stop()

# =====================================================
# SIDEBAR FILTER
# =====================================================

st.sidebar.markdown("---")

st.sidebar.subheader("🔎 Analytics Filter")

city = st.sidebar.multiselect("City", sorted(df["City"].unique()))

category = st.sidebar.multiselect(
    "Product Category", sorted(df["Product_Category"].unique())
)

payment = st.sidebar.multiselect(
    "Payment Method", sorted(df["Payment_Method"].unique())
)

device = st.sidebar.multiselect("Device Type", sorted(df["Device_Type"].unique()))

gender = st.sidebar.multiselect("Gender", sorted(df["Gender"].unique()))

filtered = df.copy()

if city:
    filtered = filtered[filtered["City"].isin(city)]

if category:
    filtered = filtered[filtered["Product_Category"].isin(category)]

if payment:
    filtered = filtered[filtered["Payment_Method"].isin(payment)]

if device:
    filtered = filtered[filtered["Device_Type"].isin(device)]

if gender:
    filtered = filtered[filtered["Gender"].isin(gender)]

# =====================================================
# KPI
# =====================================================

total_revenue = filtered["Total_Amount"].sum()

average_revenue = filtered["Total_Amount"].mean()

total_customer = len(filtered)

total_city = filtered["City"].nunique()

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

# =====================================================
# MONTHLY REVENUE TREND
# =====================================================

st.subheader("📈 Monthly Revenue Trend")

month_map = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

trend = (
    filtered.groupby("Month", as_index=False)["Total_Amount"].sum().sort_values("Month")
)

trend["Month_Name"] = trend["Month"].map(month_map)

fig = px.line(
    trend,
    x="Month_Name",
    y="Total_Amount",
    markers=True,
    template="plotly_white",
)

fig.update_traces(
    line=dict(width=3),
    marker=dict(size=8),
)

fig.update_layout(
    height=480,
    xaxis_title="Month",
    yaxis_title="Revenue",
    hovermode="x unified",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.write("")

# =====================================================
# CATEGORY & PAYMENT
# =====================================================

left, right = st.columns(2)

with left:
    st.subheader("📦 Revenue by Product Category")

    category_df = (
        filtered.groupby("Product_Category")["Total_Amount"]
        .sum()
        .reset_index()
        .sort_values(
            by="Total_Amount",
            ascending=False,
        )
    )

    fig = px.bar(
        category_df,
        x="Product_Category",
        y="Total_Amount",
        color="Total_Amount",
        text_auto=".2s",
        template="plotly_white",
    )

    fig.update_layout(
        height=450,
        coloraxis_showscale=False,
        xaxis_title="Product Category",
        yaxis_title="Revenue",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("💳 Payment Distribution")

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
        template="plotly_white",
    )

    fig.update_layout(
        height=450,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.write("")

# =====================================================
# CUSTOMER ANALYSIS
# =====================================================

left, right = st.columns(2)

with left:
    st.subheader("⭐ Customer Rating")

    fig = px.histogram(
        filtered,
        x="Customer_Rating",
        nbins=10,
        color="Customer_Rating",
        template="plotly_white",
    )

    fig.update_layout(
        height=430,
        xaxis_title="Rating",
        yaxis_title="Customers",
        coloraxis_showscale=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("🔄 Returning Customer")

    returning = filtered["Is_Returning_Customer"].value_counts().reset_index()

    returning.columns = [
        "Returning",
        "Count",
    ]

    fig = px.pie(
        returning,
        names="Returning",
        values="Count",
        hole=0.45,
        template="plotly_white",
    )

    fig.update_layout(
        height=430,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.write("")

# =====================================================
# TOP REVENUE BY CITY
# =====================================================

st.subheader("🏙️ Revenue by City")

city_df = (
    filtered.groupby("City")["Total_Amount"]
    .sum()
    .reset_index()
    .sort_values(
        by="Total_Amount",
        ascending=False,
    )
)

fig = px.bar(
    city_df,
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

# =====================================================
# FILTERED DATASET
# =====================================================

st.subheader("Filtered Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True,
    height=450,
)

st.write("")

# =====================================================
# BUSINESS INSIGHT
# =====================================================

st.subheader("🧠 Business Insight")

top_city = filtered.groupby("City")["Total_Amount"].sum().idxmax()

top_category = filtered.groupby("Product_Category")["Total_Amount"].sum().idxmax()

top_payment = filtered["Payment_Method"].value_counts().idxmax()

avg_rating = filtered["Customer_Rating"].mean()

avg_delivery = filtered["Delivery_Time_Days"].mean()

with st.container(border=True):
    st.markdown(
        f"""
### Executive Summary

**Revenue**

- Total Revenue : **${total_revenue:,.0f}**
- Average Revenue : **${average_revenue:,.2f}**

**Top Performance**

- Top City : **{top_city}**
- Best Product Category : **{top_category}**
- Most Used Payment : **{top_payment}**

**Customer Experience**

- Average Rating : **{avg_rating:.2f}/5**
- Average Delivery Time : **{avg_delivery:.2f} Days**

### Recommendations

- Prioritaskan promosi di **{top_city}** karena menghasilkan revenue tertinggi.
- Tingkatkan stok pada kategori **{top_category}**.
- Optimalkan metode pembayaran **{top_payment}**.
- Pertahankan rating pelanggan di atas **4.0** untuk menjaga kepuasan pelanggan.
"""
    )

st.write("")

# =====================================================
# FOOTER
# =====================================================

st.divider()

left, center, right = st.columns([2, 2, 1])

with left:
    st.caption("© 2026 HELIX AI SHOP")

    st.caption("Enterprise Machine Learning Platform")

with center:
    st.caption("Business Analytics")

    st.caption("Revenue Analytics")

with right:
    st.success("Ready")

st.caption("Built with Streamlit • Plotly • Pandas • FastAPI")
