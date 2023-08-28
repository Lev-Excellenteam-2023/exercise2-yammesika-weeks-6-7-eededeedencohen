TOP_ROW_KEYBOARD = set("qwertyuiop")
MIDDLE_ROW_KEYBOARD = set("asdfghjkl")
BOTTOM_ROW_KEYBOARD = set("zxcvbnm")


def find_special_state(file_path: str) -> str:
    """
    @summary:
        return the first line from a file that all his words contains only one row of the keyboard
    @param file_path: str
        The path to the file that we will check
    @return: str
        The first line from a file that all his words contains only one row of the keyboard
    """
    set_of_rows = set()
    try:
        with open(file_path, "r") as file:
            for line in file:
                set_of_rows.add(line.strip().lower())

        for row in set_of_rows:
            if TOP_ROW_KEYBOARD.issuperset(row) or MIDDLE_ROW_KEYBOARD.issuperset(
                    row) or BOTTOM_ROW_KEYBOARD.issuperset(row):
                return row
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    path_states_file = "resources/statehs.txt"
    print(find_special_state(path_states_file))
