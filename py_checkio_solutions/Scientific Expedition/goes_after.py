#!/usr/local/bin/checkio --domain=py run goes-after

# In a given word you need to check if one symbol goes right after another.
# 
# Cases you should expect while solving this challenge:
# 
# If more than one symbol is in the list you should always count the first oneone of the symbols are not in the given word - your function should return False;any symbol appears in a word more than once - use only the first one;two symbols are the same - your function should return False;the condition is case sensitive, which means 'a' and 'A' are two different symbols.Input:Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbold that should go after the first one.
# 
# Output:A bool.
# 
# 
# END_DESC

def goes_after(word: str, first: str, second: str) -> bool:
    word = ''.join(list(dict.fromkeys(word)))
    first_is_ok = False
    for i in word:
        if i == first:
            first_is_ok = True
        elif first_is_ok and i == second:
            return True
        else:
            first_is_ok = False
    return False