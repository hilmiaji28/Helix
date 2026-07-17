from __future__ import annotations

import pandas as pd

from .builder import BaseFeatureBuilder


class FeaturePipeline:
    def __init__(self, builder: BaseFeatureBuilder):
        self.builder = builder

    def run(self, df: pd.DataFrame):
        return self.builder.build(df)
