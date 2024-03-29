#!/home/user/.local/bin/checkio --domain=py run remove-all-before

# Not all of the elements are important. What you need to do here is to remove from the list all of the elements before the given one.
# 
# 
# 
# For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which is 1 and 2.
# 
# We have two edge cases here: (1) if a cutting element cannot be found, then the list shoudn't be changed. (2) if the list is empty, then it should remain empty.
# 
# Input:List and the border element.
# 
# Output:Iterable (tuple, list, iterator ...).
# 
# 
# END_DESC

#%%
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    for i in range(len(items)):
        if items[i] == border:
            return items[i:]
    return items


#%%
%%timeit
assert(remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5])
assert(remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3])
assert(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4])
assert(remove_all_before([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7])
assert(remove_all_before([], 0) == [])
assert(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7) == [7, 7, 7, 7, 7, 7, 7, 7, 7])
assert(remove_all_before([10, 1, 5, 6, 7, 10], 5) == [5, 6, 7, 10])
assert(remove_all_before([1, 2, 6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3], 6) == [6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3])

# %%
my

5.21 µs ± 30 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
your
5.78 µs ± 52.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)