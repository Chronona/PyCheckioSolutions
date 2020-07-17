#!/usr/local/bin/checkio --domain=py run end-zeros

# Try to find out how many zeros a given number has at the end.
# 
# Input:A positive Int
# 
# Output:An Int.
# 
# 
# END_DESC

def end_zeros(num: int) -> int:
    result = 0
    for i in reversed(str(num)):
        if i == "0":
            result += 1
        else:
            return result
    return result