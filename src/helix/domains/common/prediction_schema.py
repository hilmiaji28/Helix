"""
HELIX Prediction Schema.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd


@dataclass(slots=True)
class PredictionResult:
    """
    Standard prediction result.
    """

    prediction: pd.DataFrame

    metrics: Any | None = None
