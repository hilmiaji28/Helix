"""
Reusable Cards
"""

import streamlit as st


def metric_card(
    title: str,
    value,
    delta=None,
):
    st.metric(
        label=title,
        value=value,
        delta=delta,
    )


def info_card(
    title: str,
    content: str,
):
    st.markdown(
        f"""
### {title}

{content}
"""
    )


def success_card(message):
    st.success(message)


def warning_card(message):
    st.warning(message)


def error_card(message):
    st.error(message)
