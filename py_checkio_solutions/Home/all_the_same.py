#!/usr/local/bin/checkio --domain=py run all-the-same

# In this mission you should check if all elements in the given list are equal.
# 
# Input:List.
# 
# Output:Bool.
# 
# The idea for this mission was found onPython Tricks series by Dan Bader
# 
# Precondition:all elements of the input list are hashable
# 
# 
# END_DESC

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    for i in elements:
        if i != elements[0]:
            return False
    return True