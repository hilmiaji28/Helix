"""
Reusable Sidebar
"""

import streamlit as st


def render_sidebar():
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

👥 Customer Segmentation

🤖 AI Prediction

📉 Model Performance

ℹ️ About
"""
        )

        st.write("")

        st.caption("Version 1.0")
