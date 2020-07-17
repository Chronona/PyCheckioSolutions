#!/usr/local/bin/checkio --domain=py run long-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t need more than one day to solve them. All of these missions can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.
# 
# Input:String.Output:Int.
# 
# 
# 
# 
# END_DESC

def long_repeat(line: str) -> int:
    if len(line) == 0:
        return 0
    letter_count = []
    letter = line[0]
    for i in line[1:]:
        if letter[0] == i:
            letter += i
        else:
            letter_count.append(len(letter))
            letter = i
    letter_count.append(len(letter))
    return max(letter_count)