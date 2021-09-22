# -*- coding: utf-8 -*-

import importlib
from typing import List

from service import factory


class PluginInterface:
    @staticmethod
    def register(factory_: factory) -> None:
        """ Register in the factory """


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(f"plugins.{name}")  # type: ignore


def load_plugins(factory_: factory, plugins: List[str]) -> None:
    for plugin in plugins:
        plugin = import_module(plugin)
        plugin.register(factory_)
