def full_names(first_names: list[str], last_names: list[str], min_length: int = 2) -> list[str]:
    """
    @summary:
        return a list of full names that are longer than the minimum length.
    @param first_names: list[str]
        list of First names
    @param last_names: list[str]
        list of Last names
    @param min_length: int
        The minimum length of the full name to be returned (default 2)
    @return: list[str]
        list of full names that are longer than the minimum length.
    """
    all_full_names_combinations = [first_name + " " + last_name for first_name in first_names for last_name in last_names]
    return [full_name for full_name in all_full_names_combinations if len(full_name) >= min_length]


FIRST_NAMES = ['avi', 'moshe', 'yaakov']
LAST_NAMES = ['cohen', 'levi', 'mizrahi']
MINIMUM_LENGTH = 8


if __name__ == "__main__":
    print(full_names(FIRST_NAMES, LAST_NAMES, MINIMUM_LENGTH))
    print(f"There are {len((full_names(FIRST_NAMES, LAST_NAMES, MINIMUM_LENGTH)))} full names")
