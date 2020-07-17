#!/usr/local/bin/checkio --domain=py run first-word

# You are given a string where you have to find its first word.
# 
# When solving a task pay attention to the following points:
# 
# There can be dots and commas in a string.A string can start with a letter or, for example, a dot or space.A word can contain an apostrophe and it's a part of a word.The whole text can be represented with one word and that's it.Input:A string.
# 
# Output:A string.
# 
# Precondition:the text can contain a-z A-Z , . '
# 
# 
# END_DESC

def first_word(text: str) -> str:
    import re
    a = re.split("[^a-zA-Z']",text)
    output =""
    for i in a:
        output += i
        if output != "":
            return(output)