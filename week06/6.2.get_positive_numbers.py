#=======================
# נשאר? חיובי - 6.2
#=======================

def get_positive_numbers():
    # series of numbers by user input until user enters a negative number
    counter = 0
    while True:
        number = input("Enter a number: ")
        number = int(number)
        if number < 0:
            break
        counter += 1


# main program
if __name__ == "__main__":
    print("There are", get_positive_numbers(), "positive numbers")



