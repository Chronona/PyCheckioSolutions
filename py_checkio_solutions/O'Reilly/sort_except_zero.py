#!/home/user/.local/bin/checkio --domain=py run sort-except-zero

# Sort the numbers in a list. But the position of zeros should not be changed.
# 
# Input:A List.
# 
# Output:An Iterable (tuple, list, iterator ...).
# 
# Precondition:
# 
# All numbers are positive.
# 
# 
# END_DESC

from typing import Iterable


def except_zero(items: list) -> Iterable:
    zero = []
    for i in range(len(items)):
        if items[i] == 0:
            zero.append(i)
    sorted_items = sorted(items)[len(zero) :]
    result = []
    for i in range(len(items)):
        if i in zero:
            result.append(0)
        else:
            result.append(sorted_items[0])
            sorted_items = sorted_items[1:]
    return result


if __name__ == "__main__":
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")