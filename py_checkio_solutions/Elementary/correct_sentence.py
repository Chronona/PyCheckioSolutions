#!/usr/local/bin/checkio --domain=py run correct-sentence

# For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
# 
# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.
# 
# Input:A string.
# 
# Output:A string.
# 
# Precondition:No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
# 
# 
# END_DESC

def correct_sentence(text: str) -> str:
    first_word = text[0]
    remaining_word = text[1:]
    sentence=first_word.upper() + remaining_word
    if "." in text[-1]:
        return(sentence)
    return(sentence + ".")