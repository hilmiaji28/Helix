"""
Reusable Sidebar
"""

import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.title("📊 HELIX AI SHOP")
        st.caption("Enterprise Machine Learning Platform")

        st.markdown("---")

        st.markdown(
            """
## HELIX AI SHOP

Machine Learning Platform
"""
        )

        st.write("")

        st.success(
            st.session_state.get(
                "api_status",
                "Unknown",
            )
        )

        st.write("")

        st.markdown(
            """
### Modules

🏠 Home

📈 Executive Dashboard

📊 Business Analytics

🤖 Revenue Prediction

📉 Model Performance

ℹ️ About
"""
        )

        st.write("")

        st.caption("Version 1.0")
