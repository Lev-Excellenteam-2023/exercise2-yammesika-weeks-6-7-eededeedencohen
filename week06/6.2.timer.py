#------------------------
# ריצת 2000 - 6.2
#------------------------

#===========================================================================
# timer function:
# gets a function and unlimited number of parameters for that function.
# returns the time it took to execute the function with those parameters.
#===========================================================================
import timeit

def timer(func, *args):
    start = timeit.default_timer()
    func(*args)
    end = timeit.default_timer()
    # return in seconds
    return str(end - start) + " seconds"



# main program
if __name__ == "__main__":
    print(f"zip: {timer(zip, [1, 2, 3], [4, 5, 6])} \n")

    # print hello timer
    print(f"print: {timer(print, 'hello world')}")






    



    









    




