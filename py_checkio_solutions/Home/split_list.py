#!/usr/local/bin/checkio --domain=py run split-list

# You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.
# 
# 
# 
# Input:Array.
# 
# Output:Array or two arrays.
# 
# 
# END_DESC

def split_list(items: list) -> list:
    is_odd = False
    if len(items)%2 != 0:
        items.append(0)
        is_odd = True
    cut = int(len(items)/2)
    first = items[:cut]
    if is_odd:
        second = items[cut:-1]
    else:
        second = items[cut:]
    return [first, second]