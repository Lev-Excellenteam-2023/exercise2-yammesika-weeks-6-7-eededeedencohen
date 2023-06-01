#------------------
# zipwith - 6.5
#------------------

#========================================================
# zip_with function:
# get a function and two iterables.
# return a list:
# the item in the N-th index is the result of the function with the N-th item in the iterables. 
# that means, the functions gets two arguments with the N-th item in each iterable.
#========================================================

def zip_with(func, *iterable):
    return [func(*item) for item in zip(*iterable)]

# main program
if __name__ == "__main__":
    print (zip_with(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
    print (zip_with(max, (5, 4), (2, 5), (6, -6)))

