#!/usr/local/bin/checkio --domain=py run words-order


def is_ascending(items):
    if len(items) < 1:
        return True
    temp = items[0]
    for i in items[1:]:
        if i > temp:
            temp = i
        else:
            return False
    return True


def words_order(text: str, words: list) -> bool:
    items = []
    text_list = text.split(" ")
    for i in words:
        if i in text_list:
            point = text_list.index(i)
            items.append(point)
        else:
            return False

    return is_ascending(items)


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
