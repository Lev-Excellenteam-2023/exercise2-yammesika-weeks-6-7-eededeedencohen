#==============================
# פילטר מותאם אישית - 6.2
#==============================

def my_filter(func, iterable):
    """ filter the iterable by the given function.
    :param func: the function to filter the iterable
    :param iterable: the iterable to filter
    :return: the filtered iterable
    """
    for i in iterable:
        if func(i):
            yield i

# main program
if __name__ == "__main__":
    print(list(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print(list(my_filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))




