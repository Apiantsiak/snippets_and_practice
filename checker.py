"""This module includes a decorator function that checks the user's authorization."""

from flask import session
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        return "You are NOT logger in."
    return wrapper
