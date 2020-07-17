#!/usr/local/bin/checkio --domain=py run acceptable-password-iii

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but cannot consist of just digits.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

import re

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and re.search("[0-9]",password) and password.isnumeric() is False:
        return True
    return False