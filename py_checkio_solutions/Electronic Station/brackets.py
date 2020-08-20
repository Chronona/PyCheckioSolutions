#!/usr/local/bin/checkio --domain=py run brackets


import re


def checkio(expression):
    brackets = "".join(re.findall(r"[\(\)\[\]\{\}]", expression))
    while True:
        temp = brackets
        brackets = brackets.replace("()", "")
        brackets = brackets.replace("[]", "")
        brackets = brackets.replace("{}", "")
        if brackets == temp:
            break
    if len(re.findall(r"[\(\)\[\]\{\}]", brackets)) == 0:
        return True
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
