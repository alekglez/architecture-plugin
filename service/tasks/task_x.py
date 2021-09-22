# -*- coding: utf-8 -*-

from .base import Task


class TaskX(Task):
    pass


def register(factory_) -> None:
    factory_.register("task_x", TaskX)
