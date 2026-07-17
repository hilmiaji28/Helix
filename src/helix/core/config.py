from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "HELIX"

    RANDOM_STATE: int = 42

    TEST_SIZE: float = 0.20

    VALIDATION_SIZE: float = 0.20

    BASE_DIR: Path = Path(__file__).resolve().parents[3]

    DATA_DIR: Path = BASE_DIR / "data"

    RAW_DATA_DIR: Path = DATA_DIR / "01_raw"

    VALIDATED_DATA_DIR: Path = DATA_DIR / "02_validated"

    CLEAN_DATA_DIR: Path = DATA_DIR / "03_cleaned"

    FEATURE_DIR: Path = DATA_DIR / "04_feature"

    MODEL_INPUT_DIR: Path = DATA_DIR / "05_model_input"

    MODEL_DIR: Path = BASE_DIR / "models"

    REPORT_DIR: Path = BASE_DIR / "reports"

    ARTIFACT_DIR: Path = BASE_DIR / "artifacts"

    MLFLOW_DIR: Path = BASE_DIR / "mlruns"

    class Config:
        env_file = ".env"


settings = Settings()
