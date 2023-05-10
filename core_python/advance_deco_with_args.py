from functools import wraps, update_wrapper


def with_argument(deco):
    @wraps(deco)
    def wrapper(*args, **kwargs):
        def decorator(func):
            result = deco(func, *args, **kwargs)
            update_wrapper(result, func)
            return result

        return decorator

    return wrapper


@with_argument
def trace(func, text):
    def inner(*args, **kwargs):
        print(f"Arg from deco: {text}")
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@trace(100)
def foo(number):
    return number


if __name__ == '__main__':
    print(foo(42))
