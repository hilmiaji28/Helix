import json
from pathlib import Path

import joblib
import pandas as pd


class IOManager:
    @staticmethod
    def save_parquet(df, path: Path):
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_parquet(
            path,
            index=False,
        )

    @staticmethod
    def load_parquet(path: Path):
        return pd.read_parquet(path)

    @staticmethod
    def save_pickle(obj, path: Path):
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        joblib.dump(
            obj,
            path,
        )

    @staticmethod
    def load_pickle(path: Path):
        return joblib.load(path)

    @staticmethod
    def save_json(data, path: Path):
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(path, "w") as f:
            json.dump(
                data,
                f,
                indent=4,
            )

    @staticmethod
    def load_json(path: Path):
        with open(path) as f:
            return json.load(f)
