#!/home/user/.local/bin/checkio --domain=py run reverse-every-ascending

# Create and return a newIterablethat    contains the same elements as the argument listitems,    but with the reversed order of the elements inside every maximal strictly ascending subsequence.    This function should not modify the contents of the original list.
# 
# Input:List of integers.
# 
# Output:Iterable of integers.
# 
# Precondition:List contains only integers.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def reverse_ascending(items):
    result = []
    temp = []
    for i in items:
        if temp == []:
            temp.append(i)
        else:
            if temp[-1] < i:
                temp.append(i)
            else:
                result += temp[::-1]
                temp = [i]
    if temp != []:
        result += temp[::-1]
    return result


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")