"""
Dashboard Metrics
"""

import streamlit as st


def four_metrics(
    m1,
    m2,
    m3,
    m4,
):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(*m1)

    with c2:
        st.metric(*m2)

    with c3:
        st.metric(*m3)

    with c4:
        st.metric(*m4)
