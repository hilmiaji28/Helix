from abc import ABC, abstractmethod

import pandas as pd


class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> pd.DataFrame:
        """
        Load dataset.
        """
        raise NotImplementedError
