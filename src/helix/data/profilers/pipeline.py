import pandas as pd

from helix.core.io import IOManager
from helix.core.paths import ARTIFACT_DIR


class ProfilingPipeline:
    def run(
        self,
        df: pd.DataFrame,
    ):
        report = {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "missing": int(df.isna().sum().sum()),
            "duplicates": int(df.duplicated().sum()),
            "numeric": df.select_dtypes(include="number").columns.tolist(),
            "categorical": df.select_dtypes(exclude="number").columns.tolist(),
        }

        IOManager.save_json(
            report,
            ARTIFACT_DIR / "reports" / "profile.json",
        )

        return report
