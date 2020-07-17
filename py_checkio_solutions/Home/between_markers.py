#!/usr/local/bin/checkio --domain=py run between-markers

# You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
# 
# The initial and final markers are always different.If there is no initial marker, then the first character should be considered the beginning of a string.If there is no final marker, then the last character should be considered the ending of a string.If the initial and final markers are missing then simply return the whole string.If the final marker comes before the initial marker, then return an empty string.Input:Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
# 
# Output:A string.
# 
# Precondition:can't be more than one final marker and can't be more than one initial. Marker can't be an empty string
# 
# 
# END_DESC

def between_markers(text: str, begin: str, end: str) -> str:
    s = text.index(begin) if begin in text else None
    e = text.index(end) if end in text else None
    if s is None:
        if e is None:
            return text
        return text[:e]
    if e is None:
        return text[s+len(begin):]
    return text[s+len(begin):e]