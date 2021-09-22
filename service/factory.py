# -*- coding: utf-8 -*-

from typing import Callable, Dict
from .tasks.base import Task


creators: Dict[str, Callable[..., Task]] = {}


def register(task_type: str, creator_fn: Callable[..., Task]) -> None:
    creators[task_type] = creator_fn


def unregister(task_type: str) -> None:
    creators.pop(task_type)


def create_task(task_type: str) -> Task:
    try:
        fn = creators[task_type]
        return fn()

    except KeyError:
        raise ValueError(f"Unknown task type: {task_type}") from None
