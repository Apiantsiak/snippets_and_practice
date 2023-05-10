from functools import wraps

trace_enabled = False


def trace(func):
    """Output information about called function"""

    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner if trace_enabled else func


@trace
def foo(x):
    """Return pass arg"""
    return x


# @trace => foo = trace(foo)

def square(func):
    return lambda x: func(x * x)


def add_some(func):
    return lambda x: func(x + 42)


# boo => square(add_sum(boo))

@square
@add_some
def boo(number):
    return number


if __name__ == '__main__':
    print(foo(42))
    print(boo(2))
