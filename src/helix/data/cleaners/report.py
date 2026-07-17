import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CleaningReport:
    before_rows: int

    after_rows: int

    removed_duplicates: int

    removed_empty_rows: int

    def save(
        self,
        path: Path,
    ):
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(path, "w") as f:
            json.dump(
                self.__dict__,
                f,
                indent=4,
            )
