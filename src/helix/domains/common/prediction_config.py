"""
HELIX Prediction Configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PredictionConfig:
    """
    Shared configuration for prediction domains.
    """

    model_name: str

    version: str = "v1"

    save_prediction: bool = True
