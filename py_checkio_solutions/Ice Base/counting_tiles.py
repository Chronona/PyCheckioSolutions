#!/usr/local/bin/checkio --domain=py run counting-tiles

# Stephan needs some help building a circular landing zone using the ice square tiles for their new Ice Base.    Before he converts the area to a construction place, Stephan needs to figure out how many square tiles he will need.
# 
# Each square tile has size of 1x1 meters.     You need to calculate how many whole and partial tiles are needed for a circle with a radius of N meters.     The center of the circle will be at the intersection of four tiles. For example: a circle with a radius of 2 metres    requires 4 whole tiles and 12 partial tiles.
# 
# Input:The radius of a circle as a float
# 
# Output:The quantities whole and partial tiles as a list with two integers -- [solid, partial].
# 
# Precondition:
# 0 < radius ≤ 4
# 
# 
# 
# END_DESC

import math


def checkio(radius):
    perfect_tiles = 0
    partial_tiles = 0
    for x in range(math.ceil(radius)):
        for y in range(math.ceil(radius)):
            lower_left_length = math.sqrt(x ** 2 + y ** 2)
            upper_right_length = math.sqrt((x + 1) ** 2 + (y + 1) ** 2)
            if lower_left_length < radius:
                if upper_right_length < radius:
                    perfect_tiles += 1
                else:
                    partial_tiles += 1
    result = [perfect_tiles * 4, partial_tiles * 4]
    return result