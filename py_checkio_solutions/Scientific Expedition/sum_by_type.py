#!/usr/local/bin/checkio --domain=py run sum-by-type

# You have a list. Each value from that list can be either a string or an integer. Your task here is to return two values. The first one is a concatenation of all strings from the given list. The second one is a sum of all integers from the given list.
# 
# Input:An array of strings ans integers
# 
# Output:A list or tuple
# 
# Precondition:both given ints should be between -1000 and 1000
# 
# 
# END_DESC

from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    result = ["", 0]
    for i in items:
        if isinstance(i, str):
            result[0] += i
        elif isinstance(i, int):
            result[1] += i
    return tuple(result)