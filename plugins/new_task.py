# -*- coding: utf-8 -*-

from service.tasks.base import Task


class NewTask(Task):
    def execute(self):
        print("New task executed from plugin...")


def register(factory_) -> None:
    factory_.register("new_task", NewTask)
