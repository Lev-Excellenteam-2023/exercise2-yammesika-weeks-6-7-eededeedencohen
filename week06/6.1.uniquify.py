#==============
# 6.1 - חזרת
#==============
from check_type_decorator import check_type

# Description: Return a list with duplicates removed
@check_type(list)
def uniquify(lst):
    return list(set(lst))

# main program
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print("Original list: ", lst)
    lst = uniquify(lst)
    print("Uniquified list: ", lst)
