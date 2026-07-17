"""
=========================================================
HELIX AI SHOP
About
=========================================================
"""

from components.sidebar import render_sidebar

import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
)

render_sidebar()

st.title("ℹ️ About HELIX AI Shop")

st.caption("End-to-End AI Platform for Business Analytics & Revenue Prediction")

st.divider()

left, right = st.columns([2, 1])

with left:
    st.markdown(
        """
## HELIX AI SHOP

HELIX AI Shop merupakan platform Artificial Intelligence
yang mengintegrasikan Data Engineering,
Machine Learning,
Business Analytics,
serta API Deployment
ke dalam satu aplikasi yang modern.

Project ini dibuat sebagai implementasi
End-to-End AI Engineering menggunakan
best practice industri.
"""
    )

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        """
### Backend

- FastAPI
- Uvicorn
- Pydantic
- Python
"""
    )

with c2:
    st.info(
        """
### Machine Learning

- CatBoost
- Scikit-Learn
- Pandas
- NumPy
"""
    )

with c3:
    st.info(
        """
### Frontend

- Streamlit
- Plotly
- CSS
- Requests
"""
    )

st.divider()

st.subheader("🏗 System Architecture")

st.code(
    """

Streamlit UI
      │
      ▼
 FastAPI REST API
      │
      ▼
 Machine Learning Model
      │
      ▼
 Prediction Result
      │
      ▼
 Business Recommendation

"""
)

st.divider()

st.subheader("🚀 Main Features")

left, right = st.columns(2)

with left:
    st.success(
        """
✅ Executive Dashboard

✅ Business Analytics

✅ Revenue Prediction


"""
    )

with right:
    st.success(
        """
✅ Model Performance


✅ Download Report

"""
    )

st.divider()

st.subheader("📂 Project Structure")

st.code(
    """

HELIX

api/

streamlit/

models/

data/

notebooks/

tests/

docker/

.github/

"""
)

st.divider()

st.subheader("👨‍💻 Developer")

st.markdown(
    """

### Hilmi Aji

AI Engineer

Business Analytics

Machine Learning Engineer

Python Developer

Results-driven professional with experience
in Machine Learning,
Business Analytics,
Data Engineering,
and AI Deployment.

"""
)

st.divider()

st.subheader("📬 Contact")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
Email

hilmiaji248@gmail.com
"""
    )

with col2:
    st.info(
        """
LinkedIn

linkedin.com/in/hilmiaji
"""
    )

with col3:
    st.info(
        """
GitHub

github.com/hilmiaji28
"""
    )
