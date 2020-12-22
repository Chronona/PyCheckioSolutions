#!/usr/local/bin/checkio --domain=py run merge-intervals

#%%
def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    output = []
    result = []
    for i in intervals:
        if output == []:
            output = list(i)
        elif output[0] < i[0] and output[1] > i[1]:
            continue
        elif output[1] >= i[0] or output[1] + 1 == i[0]:
            output[1] = i[1]
        else:
            result.append(tuple(output))
            output = list(i)
    result.append(tuple(output))
    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [
        (1, 6),
        (8, 10),
        (12, 19),
    ], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [
        (1, 15),
        (17, 20),
    ], "Third"
    print("Done! Go ahead and Check IT")
