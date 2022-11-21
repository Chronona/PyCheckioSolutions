#!/home/user/.local/bin/checkio --domain=py run adjacent-letters

import collections

def delete_same_letters(text):
    duplicated_letter = [k for k, v in collections.Counter(text).items() if v > 1]
    for i in duplicated_letter:
        text = text.replace(i*2, "")
    return text


def adjacent_letters(line: str) -> str:
    temp = line
    while True:
        result = delete_same_letters(line)
        if temp == result:
            return result
        else:
            temp = result
            line = result

print("Example:")
print(adjacent_letters("abbaca"))

assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")