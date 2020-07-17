#!/usr/local/bin/checkio --domain=py run feed-pigeons

# I start to feed one of the pigeons.    A minute later two more fly by and a minute after that another 3.    Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute,    but in case there's not enough food for all the birds, the pigeons who arrived first ate first.    Pigeons are hungry animals and eat without knowing when to stop.    If I haveNportions of bird feed, how many pigeons will be fed with at least one portion of wheat?
# 
# 
# 
# Input:A quantity of portions wheat as a positive integer.
# 
# Output:The number of fed pigeons as an integer.
# 
# Precondition:0 < N < 105.
# 
# 
# END_DESC

def checkio(number):
    food = number 
    minute = 0 
    fed_birds = 0 
    birds = 0 

    while True:
        minute += 1 
        old_birds = birds 
        birds += minute 
        if food < birds: 
            remains_food = food - old_birds 
            if remains_food > 0:
                fed_birds += remains_food 
            return fed_birds
        food -= birds 
        fed_birds += minute