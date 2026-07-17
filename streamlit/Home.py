"""
=========================================================
HELIX AI SHOP
Home Dashboard
=========================================================
"""

from datetime import datetime

import requests

import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="HELIX AI Shop",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LOAD CSS
# ==========================================================


def load_css():
    with open("streamlit/assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )


load_css()

# ==========================================================
# API CONFIGURATION
# ==========================================================

API_URL = "http://localhost:8000"

# ==========================================================
# SESSION STATE
# ==========================================================

if "api_status" not in st.session_state:
    st.session_state.api_status = "Checking..."

if "prediction" not in st.session_state:
    st.session_state.prediction = None


# ==========================================================
# CHECK API STATUS
# ==========================================================


def check_api():
    try:
        response = requests.get(
            API_URL,
            timeout=3,
        )

        if response.status_code == 200:
            st.session_state.api_status = "🟢 Online"

        else:
            st.session_state.api_status = "🔴 Offline"

    except Exception:
        st.session_state.api_status = "🔴 Offline"


check_api()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    st.image(
        "streamlit/assets/logo.png",
        use_container_width=True,
    )

    st.markdown("---")

    st.markdown(
        """
## HELIX AI SHOP
Machine Learning Platform
"""
    )

    st.write("")

    st.success(st.session_state.api_status)

    st.write("")

    st.info(
        """
Current Features

✅ Revenue Prediction

✅ Business Analytics

✅ Customer Segmentation

✅ Executive Dashboard

✅ Model Monitoring
"""
    )

    st.write("")

    st.caption("Version 1.0")

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
<div class="hero-title">
HELIX AI SHOP
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero-subtitle">

End-to-End Machine Learning Platform
for Revenue Prediction & Business Analytics

</div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# ==========================================================
# KPI
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "API Status",
        st.session_state.api_status,
    )

with col2:
    st.metric(
        "Model",
        "CatBoost",
    )

with col3:
    st.metric(
        "Python",
        "3.12",
    )

with col4:
    st.metric(
        "Updated",
        datetime.now().strftime("%H:%M"),
    )

st.write("")
st.write("")

# ==========================================================
# INTRODUCTION
# ==========================================================

left, right = st.columns([2, 1])

with left:
    st.markdown(
        """
## Welcome to HELIX

HELIX adalah platform Machine Learning
yang dirancang untuk membantu bisnis
melakukan:

- Revenue Prediction
- Customer Analytics
- Customer Segmentation
- Executive Dashboard
- AI Decision Support

Platform ini dibangun menggunakan:

- FastAPI
- Streamlit
- CatBoost
- Scikit-Learn
- Plotly
- Docker
"""
    )

with right:
    st.info(
        """
### Project Information

Developer

Hilmi Aji

Backend

FastAPI

Frontend

Streamlit

Machine Learning

CatBoost
"""
    )

st.write("")
st.divider()

st.caption("HELIX AI SHOP © 2026 | Machine Learning Business Platform")
