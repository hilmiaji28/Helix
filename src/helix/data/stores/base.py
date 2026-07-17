from abc import ABC, abstractmethod

import pandas as pd


class BaseStore(ABC):
    @abstractmethod
    def save_dataframe(
        self,
        name: str,
        df: pd.DataFrame,
    ): ...

    @abstractmethod
    def load_dataframe(
        self,
        name: str,
    ): ...
