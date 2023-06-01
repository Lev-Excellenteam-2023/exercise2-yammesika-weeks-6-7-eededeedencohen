#-----------------------------------------
# deforator: check_type function:
# get a type.
# returns a decorator that the checks if the parameter the function receives is of the correct type.
#-----------------------------------------
from functools import wraps

def check_type(type_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], type_):
                raise TypeError(f"Expected {type_}")
            return func(*args, **kwargs)
        return wrapper
    return decorator