import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ValidationReport:
    rows: int

    columns: int

    missing: dict

    duplicates: dict

    datatype: dict

    schema: dict

    outlier: dict

    status: str

    def save(
        self,
        path: Path,
    ):
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            path,
            "w",
        ) as f:
            json.dump(
                self.__dict__,
                f,
                indent=4,
            )
