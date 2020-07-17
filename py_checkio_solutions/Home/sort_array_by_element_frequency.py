#!/usr/local/bin/checkio --domain=py run sort-array-by-element-frequency

# Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
# 
# Input:Iterable
# 
# Output:Iterable
# 
# Precondition:elements can be ints or strings
# 
# The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

import collections


def frequency_sort(items):
    counts = collections.Counter([i for i in items]).most_common()
    result = []
    for i in range(len(counts)):
        result += [counts[i][0]] * counts[i][1]
    return result