from enum import Enum


class TaskType(str, Enum):
    REGRESSION = "regression"
    CLASSIFICATION = "classification"


class ModelStatus(str, Enum):
    TRAINING = "training"
    READY = "ready"
    FAILED = "failed"


class DatasetStage(str, Enum):
    RAW = "raw"
    INTERIM = "interim"
    PROCESSED = "processed"
    FEATURES = "features"
    PREDICTIONS = "predictions"
