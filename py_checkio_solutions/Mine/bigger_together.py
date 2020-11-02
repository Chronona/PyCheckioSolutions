#!/usr/local/bin/checkio --domain=py run bigger-together


import itertools


def bigger_together(ints):
    strs = [str(i) for i in ints]
    number_list = list(itertools.permutations((strs)))
    maximum = None
    minimum = None
    for i in number_list:
        i = int("".join(i))
        if maximum is None:
            maximum = i
            minimum = i
        else:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
    return maximum - minimum


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    assert bigger_together([1, 2, 3, 4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print("Done! I feel like you good enough to click Check")
