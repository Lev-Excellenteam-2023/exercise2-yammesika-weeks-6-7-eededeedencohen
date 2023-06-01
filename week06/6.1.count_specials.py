#================================
# 6.1 - ספירת מלאי
#================================
from check_type_decorator import check_type


#--------------------------------------------------------------------------
# return how many numbers that smaller than n and are divisible by 3 or 7
#--------------------------------------------------------------------------
@check_type(int)
def count_specials(n):
    s = set()
    for i in range(1, n):
        if i % 3 == 0 or i % 7 == 0:
            s.add(i)
    return len(s)


# main function
def main():
    n = 100
    print("There are", count_specials(n), "numbers that smaller than", n, "and are divisible by 3 or 7")


# main program
if __name__ == "__main__":
    main()
    



    
