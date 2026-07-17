"""
HELIX Domain Contracts.
"""

from __future__ import annotations

from typing import Protocol

import pandas as pd


class Predictable(Protocol):
    def predict(
        self,
        X: pd.DataFrame,
    ): ...


class Trainable(Protocol):
    def train(
        self,
        X: pd.DataFrame,
        y: pd.Series,
    ): ...
