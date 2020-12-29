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

def park_benches(benches: List[Tuple[int, int]], dist: int) -> int:
    if len(benches) == 1:
        return benches[0][1]

    ans1 = count_bench_ren(benches, dist)
    ans2 = count_bench_ren(benches[1:], dist)
    
    print(ans1, ans2)
    return max(ans1, ans2)

def count_bench_ren(benches, dist):
    print(benches)
    length = 0
    start = benches[0][0]
    for i in range(len(benches)):
        b_len = benches[i][1]
        print("s:{}: n:{} b:{} l:{}".format(start, benches[i][0], b_len, length))
        if length == 0:
            length += benches[i][1]
            start += b_len
        elif start + dist > benches[i][0]:
            print("ng")
            pass
        else:
            print("ok")
            length += b_len
            start = benches[i][0] + b_len

    return length
#%%
park_benches([(1, 3), (6, 5), (13, 4)], 3)
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
