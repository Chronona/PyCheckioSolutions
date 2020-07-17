#!/usr/local/bin/checkio --domain=py run acceptable-password-i

# You are at the beginning of a password series. Every mission is based on the previous one. Going forward the missions will become slightly more complex.
# 
# In this mission, you need to create a password verification function.
# 
# The verification condition is:
# 
# the length should be bigger than 6.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    return False