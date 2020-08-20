#!/usr/local/bin/checkio --domain=py run gcd


import math
from functools import reduce


def greatest_common_divisor(*args):
    def gcd(*numbers):
        return reduce(math.gcd, numbers)

    def gcd_list(numbers):
        return reduce(math.gcd, numbers)

    return gcd(*args)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
