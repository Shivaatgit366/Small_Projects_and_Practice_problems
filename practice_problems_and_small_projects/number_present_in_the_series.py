# to find if all the numbers in a given list of integers are part of the series.
# f(0) = 0, f(1) = 1, f(n) = 9*f(n-1) - 11*f(n-2) for all n > 1.

formula_lookups = {}


def formula(num: int):
    if num < 0:
        raise ValueError("don't give negative numbers")

    if num in formula_lookups:
        return formula_lookups[num]

    if num == 0:
        ans = 0
    elif num == 1:
        ans = 1
    else:
        ans = 9 * formula(num - 1) - 11 * formula(num - 2)

    formula_lookups[num] = ans
    return ans


def is_part_of_series(lst):
    sorted_list = sorted(lst)
    x = 0
    for number in sorted_list:
        while True:
            answer = formula(x)
            if answer == number:
                break
            if answer > number:
                return False
            x = x + 1
    return True


if __name__ == '__main__':
    test_list = [1, 0, 9, 70, 531, 4009, 10]
    print(is_part_of_series(test_list))
