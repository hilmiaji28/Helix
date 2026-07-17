class HelixError(Exception):
    """Base HELIX exception."""


class DatasetError(HelixError):
    pass


class ValidationError(HelixError):
    pass


class FeatureError(HelixError):
    pass


class ModelError(HelixError):
    pass


class RegistryError(HelixError):
    pass
