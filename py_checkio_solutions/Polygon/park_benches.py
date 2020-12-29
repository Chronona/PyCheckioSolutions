#!/usr/local/bin/checkio --domain=py run park-benches

# You will need to remove some benches to keep the social distance.
#
# You are given two arguments:A list of the bench's detail (a tuple of the leftmost coordinate and the length).The minimum social distance between benches.
#
# In order to make sure that the distance between benches is at least the social distance, we remove some benches.What is the maximum total length of the remaining benches?
#
# NOTE:
#
# A list of the bench's detail is sorted.Input:Two arguments:A list of tuples of two integers.An integer.
#
# Output:An integer.
#
# Precondition:
# 1 ≤ len(benches) ≤ 100
#
#
# END_DESC
#%%
from typing import List, Tuple
import itertools

import numpy as np





def count_bench_ren(benches, dist):
    length = 0
    start = benches[0][0]
    for i in range(len(benches)):
        b_len = benches[i][1]
        if length == 0:
            length += benches[i][1]
            start += b_len
        elif start + dist > benches[i][0]:
            pass
        else:
            length += b_len
            start = benches[i][0] + b_len

    return length

def park_benches(benches: List[Tuple[int, int]], dist: int) -> int:
    if len(benches) == 1:
        return benches[0][1]

    result = 0
    
    for i in range(1, len(benches) + 1):
        com_list = itertools.combinations(benches, i)
        for i in com_list:
            temp = count_bench_ren(np.array(i), dist)
            if temp > result:
                result = temp
    import sys

    print("{}{: >25}{}{: >10}{}".format('|','Variable Name','|','Memory','|'))
    print(" ------------------------------------ ")
    for var_name in dir():
        if not var_name.startswith("_"):
            print("{}{: >25}{}{: >10}{}".format('|',var_name,'|',sys.getsizeof(eval(var_name)),'|'))
    return result


        




#%%
park_benches([[1, 6], [10, 7], [20, 7], [31, 6], [40, 7], [51, 2], [57, 1], [62, 1], [67, 2], [72, 4], [79, 1], [81, 4], [87, 2], [90, 2], [96, 7], [106, 1], [110, 5], [116, 3], [122, 4], [130, 6], [139, 4], [146, 5], [155, 2], [160, 4], [167, 4], [173, 3], [177, 7], [188, 2], [194, 2], [198, 5], [207, 5], [216, 7], [225, 2], [228, 6], [238, 7], [249, 7], [257, 5], [265, 7], [275, 4], [283, 5], [292, 2], [296, 2], [299, 1], [302, 2], [307, 1], [309, 1], [314, 5], [321, 5], [328, 5], [334, 4]], 3)
#%%





if __name__ == "__main__":
    #print("Example:")
    #print(park_benches([(0, 2), (3, 3)], 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert park_benches([(0, 2), (3, 3)], 2) == 3, "1 of 2 benches"
    assert park_benches([(1, 3), (6, 5), (13, 4)], 3) == 7, "2 of 3 benches "
    assert park_benches([(1, 2), (5, 6), (13, 3)], 3) == 6, "1 of 3 benches"
    assert park_benches([(0, 2), (3, 3), (8, 2), (11, 3)], 3) == 6, "2 of 4 benches"
    assert park_benches([(0, 5)], 7) == 5, "1 bench"
    assert (
        park_benches([(0, 4), (5, 3), (10, 2), (15, 1), (17, 5)], 1) == 15
    ), "5 benches"
    assert (
        park_benches(
            [(4, 2), (7, 4), (14, 5), (23, 6), (31, 5), (37, 5), (47, 6), (55, 4)], 3
        )
        == 26
    ), "5 of 8 benches"
    assert (
        park_benches(
            [
                (2, 8),
                (10, 4),
                (14, 10),
                (25, 7),
                (33, 2),
                (36, 1),
                (38, 1),
                (39, 3),
                (44, 4),
                (50, 9),
            ],
            2,
        )
        == 36
    ), "6 of 10 benches"
    print("Coding complete? Click 'Check' to earn cool rewards!")
# %%
# %%
a = [(1, 3), (6, 5), (13, 4)]
[
    list(map(lambda x: -1 * x, j))
    for j in sorted([sorted(i, reverse=True) for i in a], reverse=True)
]
# %%
[j for j in a]
# %%

# %%
