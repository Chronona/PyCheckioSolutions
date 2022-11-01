#!/home/user/.local/bin/checkio --domain=py run bigger-together

# Your mission here is to find a difference between the maximally positive and maximally negative numbers. Those numbers can be found by concatenating the given array of numbers.
# 
# Let’s check an example. If you have numbers 1,2,3, then 321 is the maximum number, and 123 - is the minimum. The difference between those numbers is 198. But if you have numbers 4, 3 and 12 then 4312 is the maximum number, and 1234 - is the minimum. As you can see, a simple order is not what we are looking for here.
# 
# Input:A list of positive integers.
# 
# Output:An integer.
# 
# Precondition:All elements of the list can't be less than 0
# The list can't be empty
# 
# 
# END_DESC

import itertools


def bigger_together(ints):
    strs = [str(i) for i in ints]
    number_list = list(itertools.permutations((strs)))
    maximum = None
    minimum = None
    for i in number_list:
        i = int("".join(i))
        if maximum is None:
            maximum = i
            minimum = i
        else:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
    return maximum - minimum


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    assert bigger_together([1, 2, 3, 4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print("Done! I feel like you good enough to click Check")