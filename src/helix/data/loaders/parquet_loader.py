from pathlib import Path

import pandas as pd

from .base import BaseLoader


class ParquetLoader(BaseLoader):
    def __init__(
        self,
        path: Path,
    ):
        self.path = path

    def load(self):
        return pd.read_parquet(self.path)
