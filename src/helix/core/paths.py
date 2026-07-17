from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

FEATURE_DIR = DATA_DIR / "features"

PREDICTION_DIR = DATA_DIR / "predictions"

MODEL_DIR = ROOT_DIR / "models"

ARTIFACT_DIR = ROOT_DIR / "artifacts"

REPORT_DIR = ROOT_DIR / "reports"

MLRUN_DIR = ROOT_DIR / "mlruns"
