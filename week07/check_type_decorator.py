#-----------------------------------------
# Decorator Factory function for count_words function:
# functools.wraps - to keep the original function name and docstring. 
# The factory should take one argument, a type,
# and then returns a decorator that the checks if the parameter the function receives is of the correct type.
# If it is wrong, it should raise a custom error. 
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