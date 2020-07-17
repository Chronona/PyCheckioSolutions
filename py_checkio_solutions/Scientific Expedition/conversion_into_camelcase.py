#!/usr/local/bin/checkio --domain=py run conversion-into-camelcase

# Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated without any intervening characters.
# 
# Input:A function name as a string.
# 
# Output:The same string, but in CamelCase.
# 
# Precondition:
# 0<len(string)<= 100
# Input data won't contain any numbers.
# 
# 
# 
# END_DESC

to_camel_case = lambda name: "".join([i[0].upper()+i[1:] for i in name.split("_")])