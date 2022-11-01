#!/usr/local/bin/checkio --domain=py run move-zeros

# You are given a list of integers.    Move all zeros in the list to the end of it.    The order of non-zero elements should not change.
# 
# Input:A list of integers.
# 
# Output:A list of integers.
# 
# Examples:
# 
# assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
# assert move_zeros([0]) == [0]
# END_DESC

def move_zeros(items: list[int]) -> list[int]:
    # your code here
    return []


print("Example:")
print(move_zeros([0, 1, 0, 3, 12]))

assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros([0]) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")