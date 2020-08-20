#!/usr/local/bin/checkio --domain=py run isometric-strings


def isometric_strings(str1: str, str2: str) -> bool:
    if len(set(str1)) != len(set(str2)):
        return False
    str1_unique = list(dict.fromkeys(str1))
    str2_unique = list(dict.fromkeys(str2))
    str3 = str1
    for i, j in zip(str1_unique, str2_unique):
        str3 = str3.replace(i, j)
    if str2 == str3:
        return True
    return False


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
