from abc import ABC, abstractmethod

import pandas as pd


class BaseCleaner(ABC):
    """
    Base class for all data cleaners.
    """

    @abstractmethod
    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        raise NotImplementedError
