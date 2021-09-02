import requests


BASE_URL = 'http://127.0.0.1:5000/todo/api/v1.0'


def make_url(func):
    def wrap_it(*args, **kwargs):
        url = None
        if args:
            url = BASE_URL + args[0]
            args = args[1:]
        if kwargs.get('url'):
            url = BASE_URL + kwargs['url']
            del kwargs['url']
        return func(*args, **kwargs, url=url)
    return wrap_it


def authorise(func):
    def wrap_it(*args, **kwargs):
        return func(*args, **kwargs, auth=('miguel', 'python'))
    return wrap_it


@authorise
@make_url
def create(*args, **kwargs):
    return requests.post(*args, **kwargs)


@authorise
@make_url
def read(*args, **kwargs):
    return requests.get(*args, **kwargs)


@authorise
@make_url
def update(*args, **kwargs):
    return requests.put(*args, **kwargs)


@authorise
@make_url
def delete(*args, **kwargs):
    return requests.delete(*args, **kwargs)
