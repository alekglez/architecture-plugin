# -*- coding: utf-8 -*-

from .base import Task


class TaskY(Task):
    pass


def register(factory_) -> None:
    factory_.register("task_y", TaskY)
