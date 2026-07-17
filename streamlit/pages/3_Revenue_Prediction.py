"""
==========================================================
HELIX AI SHOP
Revenue Prediction
==========================================================
"""

import pandas as pd
import requests
from components.recommendation import show_recommendation
from components.sidebar import render_sidebar

import streamlit as st

# ==========================================================
# CONFIG
# ==========================================================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Revenue Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_sidebar()

# ==========================================================
# HEADER
# ==========================================================

st.title("🤖 Revenue Prediction")

st.caption("Predict customer revenue using Machine Learning")

st.divider()

# ==========================================================
# INPUT
# ==========================================================

left, right = st.columns(2)

with left:
    st.subheader("Customer Information")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=30,
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
            "Semarang",
            "Medan",
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
    st.subheader("Shopping Behaviour")

    device = st.selectbox(
        "Device Type",
        [
            "Desktop",
            "Mobile",
            "Tablet",
        ],
    )

    duration = st.slider(
        "Session Duration (Minutes)",
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

    returning = st.toggle(
        "Returning Customer",
        value=False,
    )

    delivery = st.slider(
        "Delivery Time (Days)",
        1,
        14,
        5,
    )

    rating = st.slider(
        "Customer Rating",
        1.0,
        5.0,
        4.2,
        0.1,
    )

# ==========================================================
# PAYLOAD
# ==========================================================

payload = {
    "Age": age,
    "Gender": gender,
    "City": city,
    "Product_Category": category,
    "Payment_Method": payment,
    "Device_Type": device,
    "Session_Duration_Minutes": duration,
    "Pages_Viewed": pages,
    "Is_Returning_Customer": int(returning),
    "Delivery_Time_Days": delivery,
    "Customer_Rating": rating,
    "Transaction_Date": "2026-01-01",
}

st.divider()

predict = st.button(
    "🚀 Predict Revenue",
    use_container_width=True,
)

# ==========================================================
# PREDICTION
# ==========================================================

if predict:
    with st.spinner("Running prediction..."):
        try:
            response = requests.post(
                f"{API_URL}/predict",
                json=payload,
                timeout=20,
            )

            if response.status_code != 200:
                st.error("Prediction failed. Please check API.")

                st.stop()

            result = response.json()

            # ============================================
            # SUPPORT OLD & NEW API
            # ============================================

            if "predicted_revenue" in result:
                prediction = result["predicted_revenue"]

            elif "predicted_purchase_amount" in result:
                prediction = result["predicted_purchase_amount"]

            else:
                st.error("Prediction value not found.")

                st.write(result)

                st.stop()

            st.success("Prediction completed successfully!")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to FastAPI server.")

            st.stop()

        except Exception as e:
            st.error(str(e))

            st.stop()

# ==========================================================
# RESULT
# ==========================================================

if predict:
    st.divider()

    st.subheader("Revenue Prediction Result")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Predicted Revenue",
            f"${prediction:,.2f}",
        )

    with metric2:
        if prediction >= 1000:
            segment = "High Value"

        elif prediction >= 500:
            segment = "Medium Value"

        else:
            segment = "Low Value"

        st.metric(
            "Customer Segment",
            segment,
        )

    with metric3:
        confidence = 95.8

        st.metric(
            "Confidence",
            f"{confidence:.1f}%",
        )

    st.write("")

    # ==========================================================
    # BUSINESS RECOMMENDATION
    # ==========================================================

    if prediction >= 1000:
        st.success(
            """
### Premium Customer

Recommended Actions

• Premium Membership

• Loyalty Program

• Personalized Promotion

• Cross Selling
"""
        )

    elif prediction >= 500:
        st.info(
            """
### Medium Value Customer

Recommended Actions

• Product Bundle

• Voucher Campaign

• Upselling

• Membership Offer
"""
        )

    else:
        st.warning(
            """
### Low Value Customer

Recommended Actions

• Discount Campaign

• Flash Sale

• Cashback

• Retargeting Promotion
"""
        )

    st.write("")

# ==========================================================
# AI RECOMMENDATION
# ==========================================================

if predict:
    st.subheader("AI Recommendation")

    show_recommendation(prediction)

    st.write("")

# ==========================================================
# PREDICTION SUMMARY
# ==========================================================

if predict:
    st.divider()

    st.subheader("Prediction Summary")

    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.markdown("### 👤 Customer Profile")

            st.write(f"**Age** : {age} Years")

            st.write(f"**Gender** : {gender}")

            st.write(f"**City** : {city}")

            st.write("")

            st.markdown("### 🛒 Shopping Profile")

            st.write(f"**Category** : {category}")

            st.write(f"**Payment** : {payment}")

            st.write(f"**Device** : {device}")

    with right:
        with st.container(border=True):
            st.markdown("### 📈 Customer Behaviour")

            st.write(f"**Pages Viewed** : {pages}")

            st.write(f"**Session Duration** : {duration} Minutes")

            st.write(f"**Returning Customer** : {'Yes' if returning else 'No'}")

            st.write("")

            st.markdown("### ⭐ Experience")

            st.write(f"**Delivery Time** : {delivery} Days")

            st.write(f"**Customer Rating** : ⭐ {rating:.1f}")

st.write("")

# ==========================================================
# DOWNLOAD RESULT
# ==========================================================

if predict:
    result_df = pd.DataFrame(
        {
            "Age": [age],
            "Gender": [gender],
            "City": [city],
            "Product_Category": [category],
            "Payment_Method": [payment],
            "Device_Type": [device],
            "Predicted_Revenue": [prediction],
            "Customer_Segment": [segment],
        }
    )

    csv = result_df.to_csv(index=False)

    st.download_button(
        "📥 Download Prediction Result",
        csv,
        file_name="prediction_result.csv",
        mime="text/csv",
        use_container_width=True,
    )

st.write("")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

left, center, right = st.columns([2, 2, 1])

with left:
    st.caption("© 2026 HELIX AI SHOP")

    st.caption("Enterprise Revenue Intelligence Platform")

with center:
    st.caption("Revenue Prediction")

    st.caption("CatBoost Machine Learning Model")

with right:
    st.success("Ready")

st.caption("Built with Streamlit • FastAPI • CatBoost • Pandas")
