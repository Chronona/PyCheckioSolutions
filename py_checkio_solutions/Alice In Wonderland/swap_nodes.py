#!/usr/local/bin/checkio --domain=py run swap-nodes

import itertools


def swap_nodes(a):
    def split_list(l, n):
        for i in range(0, len(l), n):
            yield l[i : i + n]

    result = list(split_list(a, 2))
    result = [i[::-1] for i in result]
    result = list(itertools.chain.from_iterable(result))
    return result


if __name__ == "__main__":
    print("Example:")
    print(list(swap_nodes([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(swap_nodes([1, 2, 3, 4])) == [2, 1, 4, 3]
    assert list(swap_nodes([5, 5, 5, 5])) == [5, 5, 5, 5]
    assert list(swap_nodes([1, 2, 3])) == [2, 1, 3]
    assert list(swap_nodes([3])) == [3]
    assert list(swap_nodes(["hello", "world"])) == ["world", "hello"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
