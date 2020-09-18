#!/usr/local/bin/checkio --domain=py run chunk


from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    result = []
    temp = []
    for i in items:
        if len(temp) < size:
            temp.append(i)
        else:
            result.append(temp)
            temp = []
            temp.append(i)
    if len(temp) != 0:
        result.append(temp)
    return result


if __name__ == "__main__":
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
