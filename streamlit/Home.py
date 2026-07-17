"""
=========================================================
HELIX AI SHOP
Enterprise Dashboard
Home.py
=========================================================
"""

from datetime import datetime
from pathlib import Path

import requests

import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="HELIX AI SHOP",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LOAD CSS
# ==========================================================

BASE_DIR = Path(__file__).parent


def load_css():
    css_path = BASE_DIR / "assets" / "style.css"

    if css_path.exists():
        with css_path.open(encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )


load_css()

# ==========================================================
# CONFIGURATION
# ==========================================================

API_URL = "http://127.0.0.1:8000"

APP_NAME = "HELIX AI SHOP"

VERSION = "1.0.0"

MODEL_NAME = "CatBoost"

PYTHON_VERSION = "3.12"

# ==========================================================
# SESSION STATE
# ==========================================================

if "api_status" not in st.session_state:
    st.session_state.api_status = "Offline"

if "api_icon" not in st.session_state:
    st.session_state.api_icon = "🔴"

# ==========================================================
# API HEALTH CHECK
# ==========================================================


def check_api():
    try:
        response = requests.get(
            API_URL,
            timeout=2,
        )

        if response.status_code == 200:
            st.session_state.api_status = "Online"
            st.session_state.api_icon = "🟢"

        else:
            st.session_state.api_status = "Offline"
            st.session_state.api_icon = "🔴"

    except Exception:
        st.session_state.api_status = "Offline"
        st.session_state.api_icon = "🔴"


check_api()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    st.title("📊 HELIX AI SHOP")

    st.caption("Enterprise Machine Learning Platform")

    st.divider()

    if st.session_state.api_status == "Online":
        st.success(f"{st.session_state.api_icon} API Connected")

    else:
        st.error(f"{st.session_state.api_icon} API Offline")

    st.divider()

    st.subheader("Modules")

    st.markdown(
        """
- 📈 Executive Dashboard
- 📊 Business Analytics
- 🤖 Revenue Prediction
- 📉 Model Performance
- ℹ️ About
"""
    )

    st.divider()

    st.subheader("Environment")

    st.write(f"**Model** : {MODEL_NAME}")

    st.write(f"**Python** : {PYTHON_VERSION}")

    st.write(f"**Version** : {VERSION}")

    st.divider()

    st.caption("© 2026 HELIX AI SHOP")

# ==========================================================
# COMMON VARIABLES
# ==========================================================

current_time = datetime.now().strftime("%H:%M")

today = datetime.now().strftime("%d %B %Y")

# ==========================================================
# HERO
# ==========================================================

hero = st.container(border=True)

with hero:
    st.title("HELIX AI SHOP")

    st.caption(
        "End-to-End Machine Learning Platform for Revenue Prediction & Business Analytics"
    )

    st.write("")

    left, right = st.columns([3, 1])

    with left:
        st.write(
            """
HELIX membantu perusahaan mengubah data menjadi
insight melalui Business Analytics, Machine Learning,
dan Executive Dashboard yang terintegrasi.

Platform ini dirancang untuk memberikan
prediksi, visualisasi, dan monitoring model
dalam satu aplikasi.
"""
        )

    with right:
        st.info(
            f"""
📅 **Today**

{today}

🕒 **Updated**

{current_time}

🤖 **Model**

{MODEL_NAME}
"""
        )

st.write("")

# ==========================================================
# KPI
# ==========================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        label="API Status",
        value=st.session_state.api_status,
    )

with kpi2:
    st.metric(
        label="Model",
        value=MODEL_NAME,
    )

with kpi3:
    st.metric(
        label="Python",
        value=PYTHON_VERSION,
    )

with kpi4:
    st.metric(
        label="Updated",
        value=current_time,
    )

st.write("")

# ==========================================================
# WELCOME
# ==========================================================

left, right = st.columns([2, 1])

with left:
    with st.container(border=True):
        st.subheader("Welcome to HELIX")

        st.write(
            """
HELIX merupakan platform Enterprise Machine Learning
yang dikembangkan untuk membantu perusahaan
mengambil keputusan berbasis data.

Platform ini menggabungkan Business Analytics,
Revenue Prediction, dan Model Monitoring dalam satu dashboard.
"""
        )

        st.write("### Platform Features")

        st.markdown(
            """
- 📈 Revenue Prediction
- 📊 Business Analytics
- 📉 Model Performance
- ⚡ FastAPI Backend
- 🎈 Streamlit Dashboard
"""
        )

with right:
    with st.container(border=True):
        st.subheader("Project Information")

        st.write("**Developer**")
        st.write("Hilmi Aji")

        st.divider()

        st.write("**Backend**")
        st.write("FastAPI")

        st.divider()

        st.write("**Frontend**")
        st.write("Streamlit")

        st.divider()

        st.write("**Machine Learning**")
        st.write("CatBoost")

        st.divider()

        st.write("**Version**")
        st.write(VERSION)

st.write("")

# ==========================================================
# TECHNOLOGY STACK & SYSTEM OVERVIEW
# ==========================================================

st.subheader("Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    with st.container(border=True):
        st.markdown("### ⚡ Backend")
        st.write("FastAPI")
        st.caption("REST API Service")

with tech2:
    with st.container(border=True):
        st.markdown("### 🤖 Machine Learning")
        st.write("CatBoost")
        st.caption("Revenue Prediction")

with tech3:
    with st.container(border=True):
        st.markdown("### 🎈 Frontend")
        st.write("Streamlit")
        st.caption("Interactive Dashboard")

with tech4:
    with st.container(border=True):
        st.markdown("### 🐍 Language")
        st.write("Python 3.12")
        st.caption("Data & AI")

st.write("")

# ==========================================================
# SYSTEM OVERVIEW
# ==========================================================

left, right = st.columns([2, 1])

with left:
    with st.container(border=True):
        st.subheader("System Overview")

        st.markdown(
            """
HELIX AI SHOP dibangun sebagai platform end-to-end
untuk mendukung analisis bisnis dan prediksi berbasis
Machine Learning.

Alur kerja platform terdiri dari:

1. Data Collection
2. Data Preparation
3. Business Analytics
4. Machine Learning Prediction
5. Executive Dashboard
6. Decision Support
"""
        )

with right:
    with st.container(border=True):
        st.subheader("Application Status")

        st.success("✅ Dashboard Ready")

        st.success(
            "✅ API Connected"
            if st.session_state.api_status == "Online"
            else "❌ API Offline"
        )

        st.success("✅ Machine Learning")

        st.success("✅ Business Analytics")

st.write("")

# ==========================================================
# PROJECT OBJECTIVES
# ==========================================================

with st.container(border=True):
    st.subheader("Project Objectives")

    obj1, obj2, obj3 = st.columns(3)

    with obj1:
        st.markdown("### 📊 Analytics")

        st.write(
            """
Visualisasi KPI,
dashboard interaktif,
dan insight bisnis.
"""
        )

    with obj2:
        st.markdown("### 🤖 Prediction")

        st.write(
            """
Prediksi revenue
menggunakan
Machine Learning.
"""
        )

    with obj3:
        st.markdown("### 🚀 Decision Support")

        st.write(
            """
Membantu stakeholder
mengambil keputusan
berbasis data.
"""
        )

st.write("")

# ==========================================================
# PLATFORM SUMMARY
# ==========================================================

with st.container(border=True):
    st.subheader("Platform Summary")

    st.write(
        """
HELIX AI SHOP merupakan platform Enterprise Machine Learning
yang mengintegrasikan Business Analytics, Revenue Prediction, dan Model Monitoring dalam satu aplikasi.

Platform ini dibangun dengan arsitektur modern menggunakan
FastAPI sebagai backend, Streamlit sebagai frontend, serta
CatBoost sebagai model Machine Learning utama.
"""
    )

st.write("")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

footer_left, footer_center, footer_right = st.columns([2, 2, 1])

with footer_left:
    st.caption("© 2026 HELIX AI SHOP")

    st.caption("Enterprise Machine Learning Platform")

with footer_center:
    st.caption(f"Version : {VERSION}")

    st.caption(f"Model : {MODEL_NAME}")

with footer_right:
    if st.session_state.api_status == "Online":
        st.success("🟢 Online")
    else:
        st.error("🔴 Offline")

st.write("")

st.caption("Built with ❤️ using Streamlit, FastAPI, CatBoost, and Python.")
