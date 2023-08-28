from check_type_decorator import check_type


@check_type(int)
def count_specials(n: int) -> int:
    """
     @summary:
        return how many numbers that smaller than n and are divisible by 3 or 7
    @param n: int
        The number up to which we will check numbers that are divisible by 3 or 7
    @return: int
        The number of numbers that smaller than n and are divisible by 3 or 7
    """
    divisible_by_3_or_7 = set(divisible_number for divisible_number in range(1, n)
                              if divisible_number % 3 == 0 or divisible_number % 7 == 0)
    return len(divisible_by_3_or_7)


def main():
    n = 100
    print("There are", count_specials(n), "numbers that smaller than", n, "and are divisible by 3 or 7")


if __name__ == "__main__":
    main()