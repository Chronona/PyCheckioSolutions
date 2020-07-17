#!/usr/local/bin/checkio --domain=py run sum-numbers

# In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.
# 
# The text consists from numbers, spaces and english letters
# 
# Input:A string.
# 
# Output:An int.
# 
# 
# END_DESC

def sum_numbers(text: str) -> int:
    result = 0
    text = text.split(" ")
    for i in text:
        if i.isdigit():
            result += int(i)
    return result