from flask import Flask
from pycodegen_rest_api import (
    TaskAPI,
)

app = Flask(__name__)

task_api = TaskAPI(
    flask_app=app,
)


@task_api.add_task({
    methods(['POST']),
    from_params(['a']),
    url_format('some_task/:project_id/something'),
})
def simple_task(a: int, b: int, project_id: str) -> int:
    if (a < 1):
        raise InvalidProjectIdError(...) # error response handled by framework
    return a + b

class UserError(ResponseError)
    error_code = 400

class InvalidProjectIdError(UserError):
    ...