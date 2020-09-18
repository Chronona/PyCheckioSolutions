#!/usr/local/bin/checkio --domain=py run find-sequence


from typing import List
import numpy as np


def check_row(matrix):
    for i in matrix:
        count = 0
        number = None
        for j in i:
            if count == 0:
                number = j
                count = 1
            else:
                if j == number:
                    count += 1
                    if count > 3:
                        return True
                else:
                    number = j
                    count = 1
    return False


def check_diagonal(matrix):
    new_array = []
    row_number = 0
    for i in matrix:
        i = np.concatenate([i[row_number:], i[:row_number]])
        new_array.append(i.tolist())
        row_number += 1
    matrix = np.array(new_array).T

    count_reset = len(matrix)
    for i in matrix:
        count = 0
        number = None
        for j in range(len(i)):
            if count == 0 or j == count_reset:
                number = i[j]
                count = 1
            else:
                if i[j] == number:
                    count += 1
                    if count > 3:
                        return True
                else:
                    number = i[j]
                    count = 1
        count_reset -= 1
    return False


def checkio(matrix: List[List[int]]) -> bool:
    matrix = np.array(matrix)
    return (
        check_row(matrix)
        or check_row(matrix.T)
        or check_diagonal(matrix)
        or check_diagonal(np.flipud(matrix))
    )


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
    assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
    assert (
        checkio(
            [
                [2, 1, 1, 6, 1],
                [1, 3, 2, 1, 1],
                [4, 1, 1, 3, 1],
                [5, 5, 5, 5, 5],
                [1, 1, 3, 1, 1],
            ]
        )
        == True
    )
    assert (
        checkio(
            [
                [7, 1, 1, 8, 1, 1],
                [1, 1, 7, 3, 1, 5],
                [2, 3, 1, 2, 5, 1],
                [1, 1, 1, 5, 1, 4],
                [4, 6, 5, 1, 3, 1],
                [1, 1, 9, 1, 2, 1],
            ]
        )
        == True
    )
    print("All Done! Time to check!")

