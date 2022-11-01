#!/home/user/.local/bin/checkio --domain=py run frequency-sorting

# Sort the given list so that its    elements end up in the decreasing frequency order, that is, the number of    times they appear in elements. If two elements have the same frequency, they    should end up according to their natural order. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].
# 
# If you want to practice more with the similar case, trySort Array by Element Frequencymission.
# 
# Input:List of integers.
# 
# Output:List or another Iterable (tuple, iterator, generator).
# 
# Preconditions:list length <= 100;max number <= 100.
# 
# 
# END_DESC

import collections


def frequency_sorting(numbers):
    numbers = sorted(numbers)
    c = collections.Counter(numbers)
    sorted_num = c.most_common()
    result = []
    for i in range(len(sorted_num)):
        result += [sorted_num[i][0]] * sorted_num[i][1]
    return result


if __name__ == "__main__":
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [
        4,
        4,
        4,
        3,
        3,
        11,
        11,
        7,
        13,
    ], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [
        10,
        10,
        21,
        21,
        55,
        55,
        99,
        99,
    ], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")