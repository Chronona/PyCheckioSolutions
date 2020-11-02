#!/usr/local/bin/checkio --domain=py run compress-list

# A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another, there is only one in the result Iterable (list, tuple, iterator ...).
# 
# 
# 
# Input:List.
# 
# Output:"Compressed" Iterable (list, tuple, iterator ...).
# 
# 
# END_DESC

compress = lambda items: [items[i] for i in range(len(items)) if i == 0 or items[i] != items[i - 1]]