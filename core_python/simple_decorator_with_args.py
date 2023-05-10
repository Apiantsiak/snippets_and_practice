from functools import wraps


def trace(text):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f"Arg from deco: {text}")
            print(func.__name__, args, kwargs)
            return func(*args, **kwargs)

        return inner

    return decorator


# @trace => deco = trace(handle)
#           foo = deco(foo)

@trace(100)
def foo(number):
    return number


if __name__ == '__main__':
    foo(42)
