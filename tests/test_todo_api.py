import requests


def test_unauthorized_read_tasks():
    response = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')
    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_authorized_read_tasks():
    response = requests.get(
        url='http://127.0.0.1:5000/todo/api/v1.0/tasks',
        auth=('miguel', 'python',)
    )

    tasks = response.json()['tasks']
    assert response.status_code == 200
    assert len(tasks) == 2
    assert tasks[0]['title'] == 'Buy groceries'


def test_authorized_create_task():

    # GIVEN
    original_tasks = requests.get(
        url='http://127.0.0.1:5000/todo/api/v1.0/tasks',
        auth=('miguel', 'python',)
    ).json()['tasks']

    # WHEN
    response = requests.post(
        url='http://127.0.0.1:5000/todo/api/v1.0/tasks',
        auth=('miguel', 'python',),
        json={'title': 'do homework'}
    )
    task = response.json()['task']

    # THEN
    assert response.status_code == 201
    assert task['title'] == 'do homework'
    assert task['description'] == ''
    assert task['done'] is False

    # WHEN
    new_tasks = requests.get(
        url='http://127.0.0.1:5000/todo/api/v1.0/tasks',
        auth=('miguel', 'python',)
    ).json()['tasks']

    # THEN
    assert len(new_tasks) == len(original_tasks) + 1
