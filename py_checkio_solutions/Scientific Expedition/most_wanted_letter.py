#!/usr/local/bin/checkio --domain=py run most-wanted-letter

# You are given a text, which contains different English letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the Latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC

import collections


def checkio(text: str) -> str:
    text = [i for i in sorted(text.lower()) if i.isalpha()]
    text = collections.Counter(text)
    return text.most_common()[0][0]