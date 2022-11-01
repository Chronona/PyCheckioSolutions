#!/usr/local/bin/checkio --domain=py run integer-palindrome

# The idea of the mission is very easy. You need to determine whether the given integer is a palindrome or not in base B.    A number is a palindrome if it reads the same in both directions, for example 121 is a palindrome, and 122 is not.    If the integer is a palindrome in base B, return True, if not, return False.
# 
# Input:Given Int and base B(Int).
# 
# Output:Bool.
# 
# Precondition:number >= 0;number is integer;B >= 2;B is integer.
# 
# 
# END_DESC

def int_palindrome(number: int, B: int) -> bool:

    # your code here
    return False


print("Example:")
print(int_palindrome(455, 2))

assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")