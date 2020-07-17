#!/usr/local/bin/checkio --domain=py run backward-string

# You should return a given string in reverse order.
# 
# Input:A string.
# 
# Output:A string.
# 
# 
# END_DESC

def backward_string(val: str) -> str:
    return "".join(list(reversed(val)))