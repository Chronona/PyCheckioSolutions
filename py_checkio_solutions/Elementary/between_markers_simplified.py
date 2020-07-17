#!/usr/local/bin/checkio --domain=py run between-markers-simplified

# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
# 
# This is a simplified version of theBetween Markersmission.
# 
# The initial and final markers are always different.The initial and final markers are always 1 char size.The initial and final markers always exist in a string and go one after another.Input:Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
# 
# Output:A string.
# 
# Precondition:There can't be more than one final and one initial markers.
# 
# 
# END_DESC

def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+1:text.index(end)]