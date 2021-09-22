# -*- coding: utf-8 -*-

import json

from service import factory, loader
from service.tasks import task_x, task_y, task_z


def main() -> None:
    task_x.register(factory)
    task_y.register(factory)
    task_z.register(factory)

    with open("./configs/config.json") as f:
        config = json.load(f)
        loader.load_plugins(factory, config.get("plugins", []))

        tasks_ = [factory.create_task(task) for task in config.get("tasks", [])]
        for task in tasks_:
            if task:
                task.execute()


if __name__ == "__main__":
    main()
