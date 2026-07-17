"""
Recommendation Box
"""

import streamlit as st


def show_recommendation(
    prediction,
):
    st.markdown("---")

    st.subheader("AI Recommendation")

    if prediction is None:
        st.info("Prediction belum tersedia.")

        return

    if prediction > 1000:
        st.success(
            """
Customer diprediksi memiliki
nilai transaksi tinggi.

Rekomendasi:

• Berikan Premium Offer

• Upselling

• Loyalty Program
"""
        )

    elif prediction > 500:
        st.warning(
            """
Customer kategori sedang.

Rekomendasi:

• Cross Selling

• Voucher

• Bundling
"""
        )

    else:
        st.error(
            """
Customer berpotensi
berbelanja rendah.

Rekomendasi:

• Diskon

• Flash Sale

• Free Shipping
"""
        )
