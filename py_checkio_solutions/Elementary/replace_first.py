#!/usr/local/bin/checkio --domain=py run replace-first

# In a given list the first element should become the last one. An empty list or list with only one element should stay the same.
# 
# 
# 
# Input:List.
# 
# Output:Iterable.
# 
# 
# END_DESC

from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items == []:
        return items
    first = items[0]
    items.append(first)
    return items[1:]