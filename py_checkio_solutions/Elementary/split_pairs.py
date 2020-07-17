#!/usr/local/bin/checkio --domain=py run split-pairs

# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').
# 
# Input:A string.
# 
# Output:An iterable of strings.
# 
# Precondition:0<=len(str)<=100
# 
# 
# END_DESC

def split_pairs(a):
    if len(a) == 0:
        return []
    if len(a)%2 != 0:
        a += "_"
    return [a[i:i+2] for i in range(0, len(a), 2)]