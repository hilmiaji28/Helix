from pathlib import Path

import joblib
import pandas as pd

# ==========================================================
# CONFIG
# ==========================================================

DATA_PATH = Path("data/processed/revenue_final_dataset_v2.csv")

MODEL_PATH = Path("models/best_tuned_model.pkl")

ARTIFACT_DIR = Path("artifacts")

ARTIFACT_DIR.mkdir(exist_ok=True)

TARGET = "Total_Amount"

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv(DATA_PATH)

X = df.drop(columns=[TARGET])

# ==========================================================
# FEATURE COLUMNS
# ==========================================================

joblib.dump(list(X.columns), ARTIFACT_DIR / "feature_columns.pkl")

print("feature_columns.pkl saved")

# ==========================================================
# FEATURE METADATA
# ==========================================================

feature_metadata = {
    "categorical": [
        "Gender",
        "City",
        "Product_Category",
        "Payment_Method",
        "Device_Type",
        "Age_Group",
    ],
    "numerical": [
        c
        for c in X.columns
        if c
        not in [
            "Gender",
            "City",
            "Product_Category",
            "Payment_Method",
            "Device_Type",
            "Age_Group",
        ]
    ],
}

joblib.dump(feature_metadata, ARTIFACT_DIR / "feature_metadata.pkl")

print("feature_metadata.pkl saved")

# ==========================================================
# FREQUENCY ENCODING
# ==========================================================

frequency_maps = {}

for col in ["City", "Product_Category", "Payment_Method", "Device_Type"]:
    frequency_maps[col] = df[col].value_counts(normalize=True).to_dict()

joblib.dump(frequency_maps, ARTIFACT_DIR / "frequency_maps.pkl")

print("frequency_maps.pkl saved")

# ==========================================================
# LOAD MODEL
# ==========================================================

pipeline = joblib.load(MODEL_PATH)

preprocessor = pipeline.named_steps["preprocessor"]

metadata = {
    "feature_order": list(X.columns),
    "pipeline_type": type(pipeline).__name__,
    "preprocessor_type": type(preprocessor).__name__,
}

joblib.dump(metadata, ARTIFACT_DIR / "preprocessing_metadata.pkl")

print("preprocessing_metadata.pkl saved")

print("=" * 60)

print("ALL PREPROCESSING ARTIFACTS EXPORTED")

print("=" * 60)
