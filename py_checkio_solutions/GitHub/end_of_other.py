#!/usr/local/bin/checkio --domain=py run end-of-other


def checkio(words_set):
    for word in words_set:
        if len([i for i in words_set if i.endswith(word)]) > 1:
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
