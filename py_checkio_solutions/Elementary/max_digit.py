#!/usr/local/bin/checkio --domain=py run max-digit

# You have a number and you need to determine which digit in this number is the biggest.
# 
# Input:A positive int.
# 
# Output:An Int (0-9).
# 
# 
# END_DESC

max_digit = lambda number: max([int(i) for i in str(number)])