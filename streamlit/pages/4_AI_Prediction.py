"""
==========================================================
HELIX AI SHOP
AI Prediction
==========================================================
"""

import requests
from components.recommendation import show_recommendation
from components.sidebar import render_sidebar

import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI Prediction",
    page_icon="🤖",
    layout="wide",
)

render_sidebar()

st.title("🤖 AI Purchase Prediction")

st.caption("Predict customer purchase amount using Machine Learning.")

st.divider()

left, right = st.columns(2)

with left:
    age = st.number_input(
        "Age",
        18,
        80,
        30,
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
        ],
    )

    city = st.selectbox(
        "City",
        [
            "Bandung",
            "Jakarta",
            "Surabaya",
            "Medan",
            "Semarang",
        ],
    )

    category = st.selectbox(
        "Product Category",
        [
            "Electronics",
            "Fashion",
            "Home",
            "Beauty",
            "Sports",
        ],
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Cash",
            "Credit Card",
            "E-Wallet",
        ],
    )

with right:
    device = st.selectbox(
        "Device",
        [
            "Desktop",
            "Mobile",
            "Tablet",
        ],
    )

    duration = st.slider(
        "Session Duration",
        1,
        120,
        30,
    )

    pages = st.slider(
        "Pages Viewed",
        1,
        50,
        10,
    )

    returning = st.selectbox(
        "Returning Customer",
        [
            0,
            1,
        ],
    )

    delivery = st.slider(
        "Delivery Time",
        1,
        14,
        5,
    )

    rating = st.slider(
        "Customer Rating",
        1.0,
        5.0,
        4.2,
    )

payload = {
    "Age": age,
    "Gender": gender,
    "City": city,
    "Product_Category": category,
    "Payment_Method": payment,
    "Device_Type": device,
    "Session_Duration_Minutes": duration,
    "Pages_Viewed": pages,
    "Is_Returning_Customer": returning,
    "Delivery_Time_Days": delivery,
    "Customer_Rating": rating,
    "Transaction_Date": "2026-01-01",
}

st.divider()

predict = st.button("🚀 Predict Purchase Amount")

if predict:
    with st.spinner("Predicting..."):
        try:
            response = requests.post(
                f"{API_URL}/predict",
                json=payload,
                timeout=20,
            )

            if response.status_code == 200:
                result = response.json()

                prediction = result["predicted_purchase_amount"]

                st.success("Prediction Successful!")

            else:
                prediction = None

                st.error("Prediction Failed")

        except Exception as e:
            prediction = None

            st.error(e)

if predict and prediction is not None:
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Purchase",
            f"${prediction:,.2f}",
        )

    with col2:
        if prediction > 1000:
            st.metric(
                "Customer Segment",
                "High Value",
            )

        elif prediction > 500:
            st.metric(
                "Customer Segment",
                "Medium Value",
            )

        else:
            st.metric(
                "Customer Segment",
                "Low Value",
            )

if predict and prediction is not None:
    show_recommendation(prediction)

if predict:
    st.divider()

    st.subheader("Prediction Summary")

    st.json(payload)

st.divider()

st.caption("HELIX AI SHOP • AI Prediction • 2026")
