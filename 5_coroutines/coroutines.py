from inspect import getgeneratorstate
from typing import Generator


def coroutine(func):
    def wrapper(*args, **kwargs):
        g: Generator = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper


def gen():
    x = "Ready to accept message."
    message = yield x
    print("Gen received: ", message)


@coroutine
def average():
    cnt = 0
    sm = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done!")
            break
        else:
            cnt += 1
            sm += x
            average = round(sm / cnt, 2)


gen_ = gen()
avg = average()
