#!/usr/local/bin/checkio --domain=py run acceptable-password-v

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but it cannot consist of just digits;having numbers or containing just numbers does not apply to the password longer than 9.a string should not contain the word "password" in any case.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

import re

def is_acceptable_password(password: str) -> bool:
    if "password" in password.lower():
        return False
    elif len(password) >= 10:
        return True
    elif len(password) > 6 and re.search("[0-9]",password) and password.isnumeric() is False:
        return True
    return False