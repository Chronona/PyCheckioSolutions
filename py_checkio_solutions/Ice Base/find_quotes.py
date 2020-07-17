#!/usr/local/bin/checkio --domain=py run find-quotes

# Your task at hand is to find all quotes in the text. And, as is already usual, do everything as quickly as possible :)You are given a string that consists of characters and a paired number of quotation marks. You need to  return an Iterable consisting  of the texts inside the quotation marks. But choose only quotes with double quotation marks ("). Single quotation marks (') aren’t appropriate.
# 
# Input:A string.
# 
# Output:An iterable.
# 
# 
# END_DESC

import re
def find_quotes(a):
    result = []
    while True:
        quotes = [m.start() for m in re.finditer('"', a)]
        if quotes == []:
            return result
        word = a[quotes[0]+1:quotes[1]]
        result.append(word)
        a = a.replace('"','',2)