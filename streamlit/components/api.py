"""
API Helper
"""

import requests

API_URL = "http://localhost:8000"


def get_health():
    try:
        response = requests.get(
            API_URL,
            timeout=5,
        )

        return response.json()

    except Exception:
        return None


def predict(payload):
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=payload,
            timeout=30,
        )

        if response.status_code == 200:
            return response.json()

        return None

    except Exception:
        return None
