#!/usr/local/bin/checkio --domain=py run nonogram-encode

# I believe, you have heart about picture logic puzzlesnonogramsand solved them. This mission is the opposite: you already have a binary image,    formed by strings of equal length, where background empty cell is whitespace and    picture cell filled with 'X'.
# 
# Your goal is to create a nonogram from the image: write a number clue for solving    this image like it was hidden. Your function should return a list of two lists.    The first one consists of lists with numbers for columns clue, the second one -    the same for rows clue. All lists in columns clue, as well as in rows,    should be of same 'depth' (complemented with 0). Let's see all this on example:
# 
# 
# example = [' X X ',
#            'X X X', 
#            ' X X ']
#     Example with solution to see the whole idea:
# 
# 
#     columns clue 01010
#                  11111
# rows clue 0 1 1 ' X X '
#           1 1 1 'X X X'
#           0 1 1 ' X X '
#     So, for this example your function should return the following:
# 
# 
# nonogram_encode(example) = [[[0, 1, 0, 1, 0],
#                              [1, 1, 1, 1, 1]],
#                             [[0, 1, 1],
#                              [1, 1, 1],
#                              [0, 1, 1]]]
# # the same, non formatted view
# [[[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]], [[0, 1, 1], [1, 1, 1], [0, 1, 1]]]
#     
# 
# Input:List of strings.
# 
# Output:List of 2 lists.
# 
# Examples:
# 
# assert nonogram_encode([" X X ", "X X X", " X X "]) == [
#     [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
#     [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
# ]
# assert nonogram_encode(["X"]) == [[[1]], [[1]]]Precondition:len(data[i]) == len(data[0])set(data[i]) == set([' ', 'X'])for lists in output: len(list[i]) == len(list[0])
# 
# 
# END_DESC

def nonogram_encode(data: list[str]) -> list:
    # your code here
    return []


print("Example:")
print(nonogram_encode([" X X ", "X X X", " X X "]))

assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]

print("The mission is done! Click 'Check Solution' to earn rewards!")