# -*- coding: utf-8 -*-

from typing import Protocol


class Task(Protocol):
    """ Basic Task """

    def execute(self) -> None:
        """ It does some stuffs """
        print(f"Doing something from {self.__class__.__name__}...")
