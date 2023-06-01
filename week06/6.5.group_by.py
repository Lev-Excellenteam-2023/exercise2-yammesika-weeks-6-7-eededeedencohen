#------------------
# group_by - 6.5
#------------------

#=======================================
# group_by function:
# get a function and an iterable.
# return a dictionary:
# key: the value returned from the function.
# value: a list of all the items in the iterable that returned the key.
#=======================================

def group_by(func,iterable):
    return {key:[item for item in iterable if func(item) == key] 
            for key in set([func(item) for item in iterable])}

# main program
if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))





 