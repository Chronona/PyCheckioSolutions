#!/usr/local/bin/checkio --domain=py run count-digits

# You need to count the number of digits in a given string.
# 
# Input:A Str.
# 
# Output:An Int.
# 
# 
# END_DESC

import re

def count_digits(text: str) -> int:
    result = 0
    text = text.split(" ")
    for i in text:
        if not i.isalpha():
            result += len(re.sub(r"\D", "", i))
    return result