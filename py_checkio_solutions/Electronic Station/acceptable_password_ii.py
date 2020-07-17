#!/usr/local/bin/checkio --domain=py run acceptable-password-ii

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

import re

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and re.search("[0-9]",password):
        return True
    return False