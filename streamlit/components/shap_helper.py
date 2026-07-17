"""
SHAP Helper
"""

from pathlib import Path

import joblib
import pandas as pd
import shap

MODEL_PATH = Path("models/catboost_model.pkl")


model = joblib.load(MODEL_PATH)


def load_sample():
    return pd.read_csv("data/processed/test_prediction.csv")


def global_shap():
    df = load_sample()

    X = df.drop(columns=["Purchase_Amount"])

    explainer = shap.TreeExplainer(model)

    values = explainer.shap_values(X)

    return explainer, values, X


def local_shap(index):
    df = load_sample()

    X = df.drop(columns=["Purchase_Amount"])

    explainer = shap.TreeExplainer(model)

    values = explainer.shap_values(X)

    return explainer, values[index], X.iloc[index]
