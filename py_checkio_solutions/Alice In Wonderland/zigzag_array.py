#!/usr/local/bin/checkio --domain=py run zigzag-array

# This function creates an List of lists. that represents a two-dimensional grid with the given number of rows and  cols. This grid should contain the integers fromstarttostart + rows * cols - 1in ascending order, but the elements of every odd-numbered row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
# 
# Input:Two ints rows and cols. One optional argument start.
# 
# Output:List of lists.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from typing import List


def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    result = []
    if rows == 0:
        return result
    if cols == 0:
        result = [[] for i in range(rows)]
        return result
    maximum = start + rows * cols
    number_list = []
    is_reversed = False
    count = start
    while count <= maximum:
        if len(number_list) < cols:
            number_list.append(count)
            count += 1
        else:
            if is_reversed:
                number_list = number_list[::-1]
                is_reversed = False
            else:
                is_reversed = True
            result.append(number_list)
            number_list = []
    return result