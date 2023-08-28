import timeit
from typing import Any


def timer(func: callable, *args: Any) -> str:
    """
    @summary:
        return the time it took to execute the function with list of parameters
    @param func: callable
        The function that we will execute
    @param args: Any
        The parameters for the function that we will execute
    @return: str
        The time it took to execute the function with list of parameters
    """
    start = timeit.default_timer()
    func(*args)
    end = timeit.default_timer()
    # return in seconds
    return str(end - start) + " seconds"


if __name__ == "__main__":
    print(f"zip: {timer(zip, [1, 2, 3], [4, 5, 6])} \n")

    print(f"print: {timer(print, 'hello world')}")