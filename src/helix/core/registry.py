from helix.core.io import IOManager
from helix.core.paths import MODEL_DIR


class Registry:
    def __init__(self):
        self.path = MODEL_DIR / "registry.json"

        if self.path.exists():
            self.registry = IOManager.load_json(self.path)

        else:
            self.registry = {}

    def register(
        self,
        name,
        metadata,
    ):
        self.registry[name] = metadata

        IOManager.save_json(
            self.registry,
            self.path,
        )

    def get(
        self,
        name,
    ):
        return self.registry.get(name)

    def all(self):
        return self.registry
