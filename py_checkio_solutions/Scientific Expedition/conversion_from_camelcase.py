#!/usr/local/bin/checkio --domain=py run conversion-from-camelcase

# Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".
# 
# Input:A function name as a CamelCase string.
# 
# Output:The same string, but in under_score.
# 
# Precondition:
# 0<len(string)<= 100
# Input data won't contain any numbers.
# 
# 
# 
# END_DESC

def from_camel_case(name):
    result = ""
    for i in range(len(name)):
        if i == 0:
            result += name[i].lower()
        elif name[i].isupper():
            result += "_"+name[i].lower()
        else:
            result += name[i]
    return result