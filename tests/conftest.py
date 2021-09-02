import pytest

from todo_api.resources import todos


@pytest.fixture(scope='function', autouse=True)
def reset_tasks():
    pass
    yield
    todos.delete('/tasks/reset')
