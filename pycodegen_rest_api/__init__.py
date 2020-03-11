from flask import Flask, request, Request, make_response
from dataclasses import dataclass
from typing import (
    Callable,
    Optional, Set)

from pycodegen_rest_api.TaskOptions import BaseTaskOption


class FileInput:
    file_name: str


# TODO: separate out flask-api
#   (only create "task-api definition", not actual implementation
@dataclass
class TaskAPI:
    flask_app: Flask

    def _wrap_task_for_flask_api(
            self,
            req_to_params,
            task_fn,
    ):
        def __wrap_task_for_flask_api__(
        ):
            req: Request = request
            params = req_to_params(req)
            try:
                result = task_fn(params)
                resp = make_response()
            except:
                pass


        return __wrap_task_for_flask_api__

    def add_task(
            self,
            options: Optional[Set[BaseTaskOption]] = None,
    ):
        def __add_task(task_fn]: Callable):
            name = task_fn.__name__
            flask_fn = self._wrap_task_for_flask_api()
            self.flask_app.route(f'/{name}', methods=['POST'])
            # self.flask_app.route(task_fn)
        return __add_task