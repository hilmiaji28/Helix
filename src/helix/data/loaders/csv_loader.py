import pandas as pd

from helix.core.logging import get_logger
from helix.core.paths import RAW_DATA_DIR

logger = get_logger(__name__)


class CSVLoader:
    def __init__(
        self,
        filename: str,
    ):
        self.path = RAW_DATA_DIR / filename

    def load(self) -> pd.DataFrame:
        logger.info(
            "Reading %s",
            self.path,
        )

        if not self.path.exists():
            raise FileNotFoundError(
                self.path,
            )

        df = pd.read_csv(
            self.path,
        )

        logger.info(
            "Rows : %s",
            df.shape[0],
        )

        logger.info(
            "Columns : %s",
            df.shape[1],
        )

        return df
