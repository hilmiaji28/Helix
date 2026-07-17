from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseFeatureBuilder(ABC):
    """
    Base class untuk seluruh feature builder.
    """

    @abstractmethod
    def build(self, df: pd.DataFrame) -> pd.DataFrame:
        """Build new features."""
        raise NotImplementedError


class IdentityFeatureBuilder(BaseFeatureBuilder):
    """
    Tidak membuat feature baru.
    Berguna sebagai default pipeline.
    """

    def build(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.copy()
