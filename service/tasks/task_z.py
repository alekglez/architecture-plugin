# -*- coding: utf-8 -*-

from .base import Task


class TaskZ(Task):
    pass


def register(factory_) -> None:
    factory_.register("task_z", TaskZ)
