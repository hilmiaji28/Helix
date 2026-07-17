"""
HELIX Serialization Utilities.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib


class ModelSerializer:
    """
    Generic serializer for machine learning artifacts.
    """

    @staticmethod
    def save(
        obj: Any,
        path: str | Path,
    ) -> None:
        """
        Serialize any Python object.
        """

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        joblib.dump(
            obj,
            path,
        )

    @staticmethod
    def load(
        path: str | Path,
    ) -> Any:
        """
        Load serialized object.
        """

        return joblib.load(
            Path(path),
        )
