from typing import Generator


class SomeException(Exception):
    """Random exception.
    """


def coroutine(func):
    def inner(*args, **kwargs):
        g: Generator = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    while True:
        try:
            message = yield
        except Exception as e:
            return f"{e.__class__.__name__} raised."
        else:
            print("..........", message)


@coroutine
def delegator(g: Generator):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except SomeException as e:
    #         g.throw(e)
    res = yield from g
    print("res: ", res)


sg = subgen()
g = delegator(sg)
