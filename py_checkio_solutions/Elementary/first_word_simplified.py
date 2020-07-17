#!/usr/local/bin/checkio --domain=py run first-word-simplified

# You are given a string and you have to find its first word.
# 
# This is a simplified version of theFirst Wordmission, which can be solved later.
# 
# The input string consists of only English letters and spaces.There aren’t any spaces at the beginning and the end of the string.Input:A string.
# 
# Output:A string.
# 
# Precondition:The text can contain a-z, A-Z and spaces.
# 
# 
# END_DESC

def first_word(text: str) -> str:
    space = text.find(" ")
    if space == -1:
        return(text)
    return(text[:space])