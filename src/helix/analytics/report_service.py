import json

from helix.core.config import settings


class ReportService:
    def save(
        self,
        report,
        filename,
    ):
        folder = settings.ARTIFACT_DIR / "reports"

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            folder / filename,
            "w",
        ) as f:
            json.dump(
                report,
                f,
                indent=4,
            )
