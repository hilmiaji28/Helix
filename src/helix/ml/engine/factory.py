"""
HELIX Engine Factory.
"""

from __future__ import annotations

from typing import Any

from .registry import (
    ENGINE_REGISTRY,
    TaskType,
)


class EngineFactory:
    """
    Factory for creating machine learning engines.
    """

    @staticmethod
    def available_tasks() -> list[str]:
        """
        Return available task names.
        """

        return [task.value for task in TaskType]

    @staticmethod
    def create(
        task: TaskType | str,
        **config_kwargs: Any,
    ):
        """
        Create a machine learning engine.

        Parameters
        ----------
        task : TaskType | str
            Machine learning task.

        **config_kwargs
            Configuration values passed to
            the corresponding Config class.

        Returns
        -------
        BaseEngine
        """

        if isinstance(task, str):
            try:
                task = TaskType(task.lower())

            except ValueError as exc:
                raise ValueError(
                    f"Unsupported task '{task}'. "
                    f"Available tasks: "
                    f"{EngineFactory.available_tasks()}"
                ) from exc

        engine_cls, config_cls = ENGINE_REGISTRY[task]

        config = config_cls(
            **config_kwargs,
        )

        return engine_cls(config)
