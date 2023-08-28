TOP_ROW_KEYBOARD = set("qwertyuiop")
MIDDLE_ROW_KEYBOARD = set("asdfghjkl")
BOTTOM_ROW_KEYBOARD = set("zxcvbnm")

# insert all the words in the resources/states.txt file to a set
states = set()
with open("resources/states.txt", "r") as f:
    for line in f:
        states.add(line.strip().lower())


def find_special_state() -> str:
    """
    @summary:
        return the first state that its name is typed using only one row of the keyboard
    @return: str
        The first state that its name is typed using only one row of the keyboard
    """
    for state in states:
        if TOP_ROW_KEYBOARD.issuperset(state) or MIDDLE_ROW_KEYBOARD.issuperset(state) or BOTTOM_ROW_KEYBOARD.issuperset(state):
            return state


if __name__ == "__main__":
    print(find_special_state())