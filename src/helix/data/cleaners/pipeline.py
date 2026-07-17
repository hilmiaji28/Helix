import pandas as pd

from helix.core.paths import ARTIFACT_DIR

from .column_cleaner import ColumnCleaner
from .datatype_cleaner import DatatypeCleaner
from .duplicate_cleaner import DuplicateCleaner
from .missing_cleaner import MissingCleaner
from .report import CleaningReport
from .string_cleaner import StringCleaner


class CleaningPipeline:
    def __init__(self):
        self.column = ColumnCleaner()

        self.string = StringCleaner()

        self.duplicate = DuplicateCleaner()

        self.missing = MissingCleaner()

        self.datatype = DatatypeCleaner()

    def run(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        before_rows = len(df)

        duplicate_before = int(df.duplicated().sum())

        empty_before = int(df.isna().all(axis=1).sum())

        df = self.column.clean(df)

        df = self.string.clean(df)

        df = self.duplicate.clean(df)

        df = self.missing.clean(df)

        df = self.datatype.clean(df)

        report = CleaningReport(
            before_rows=before_rows,
            after_rows=len(df),
            removed_duplicates=duplicate_before,
            removed_empty_rows=empty_before,
        )

        report.save(ARTIFACT_DIR / "reports" / "cleaning.json")

        return df
