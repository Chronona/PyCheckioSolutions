#!/usr/local/bin/checkio --domain=py run beginning-zeros

# You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
# 
# Input:A string, that consist of digits.
# 
# Output:An Int.
# 
# Precondition:0-9
# 
# 
# END_DESC

def beginning_zeros(number: str) -> int:
    result = 0
    for i in number:
        if i == "0":
            result += 1
        else:
            return result
    return result