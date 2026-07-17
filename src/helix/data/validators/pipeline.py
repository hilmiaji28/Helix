from helix.core.paths import ARTIFACT_DIR

from .datatype import DatatypeValidator
from .duplicate import DuplicateValidator
from .missing import MissingValidator
from .outlier import OutlierValidator
from .report import ValidationReport
from .schema import SchemaValidator


class ValidationPipeline:
    def __init__(self):
        self.missing = MissingValidator()

        self.duplicate = DuplicateValidator()

        self.datatype = DatatypeValidator()

        self.schema = SchemaValidator()

        self.outlier = OutlierValidator()

    def run(
        self,
        df,
    ):
        report = ValidationReport(
            rows=df.shape[0],
            columns=df.shape[1],
            missing=self.missing.validate(df),
            duplicates=self.duplicate.validate(df),
            datatype=self.datatype.validate(df),
            schema=self.schema.validate(df),
            outlier=self.outlier.validate(df),
            status="PASS",
        )

        report.save(ARTIFACT_DIR / "reports" / "validation.json")

        return report
