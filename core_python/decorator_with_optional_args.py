from functools import wraps

from advance_deco_with_args import with_argument


# naive version with emty ()
@with_argument
def trace(func, text="Hello"):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Arg from deco: {text}")
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@trace()
def foo(number):
    return number


# advance version without ()
def adv_trace(func=None, *, text="Hello"):
    # with ()
    if func is None:
        return lambda func: adv_trace(func, text=text)

    # without ()
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Arg from deco: {text}")
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@adv_trace(text="BYE")  # works only with kwargs
def boo(number):
    return number


if __name__ == '__main__':
    print(foo(42))
    print(boo(42))
