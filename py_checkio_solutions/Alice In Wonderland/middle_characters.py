#!/usr/local/bin/checkio --domain=py run middle-characters


def middle(text):
    if len(text) % 2 == 0:
        middle_point = int(len(text) / 2 - 1)
        return text[middle_point : middle_point + 2]
    else:
        text += "_"
        middle_point = int(len(text) / 2 - 1)
        return text[middle_point : middle_point + 1]


if __name__ == "__main__":
    print("Example:")
    print(middle("example"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle("example") == "m"
    assert middle("test") == "es"
    assert middle("very-very long sentence") == "o"
    assert middle("I") == "I"
    assert middle("no") == "no"
    print("Coding complete? Click 'Check' to earn cool rewards!")
