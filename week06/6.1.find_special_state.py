#=======================
# שטוחלנדיה - 6.1
#=======================


# set of the letters in the 1st row of the keyboard
topRow = set("qwertyuiop")

# set of the letters in the 2nd row of the keyboard
midRow = set("asdfghjkl")

# set of the letters in the 3rd row of the keyboard
botRow = set("zxcvbnm")

# insert all the words in the resources/states.txt file to a set
states = set()
with open("resources/states.txt", "r") as f:
    for line in f:
        states.add(line.strip().lower())

#-------------------------------------------------------------
# find_special_state function:
# returns the state that has all the letters in the same row
#-------------------------------------------------------------
def find_special_state():
    for state in states:
        if topRow.issuperset(state) or midRow.issuperset(state) or botRow.issuperset(state):
            return state

# main program
if __name__ == "__main__":
    print(find_special_state())




