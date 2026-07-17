from __future__ import annotations

from .builder import BaseFeatureBuilder


class FeatureRegistry:
    _builders: dict[str, type[BaseFeatureBuilder]] = {}

    @classmethod
    def register(cls, name: str, builder: type[BaseFeatureBuilder]):
        cls._builders[name] = builder

    @classmethod
    def get(cls, name: str):
        if name not in cls._builders:
            raise ValueError(f"Feature builder '{name}' belum terdaftar.")

        return cls._builders[name]

    @classmethod
    def available(cls):
        return sorted(cls._builders.keys())
