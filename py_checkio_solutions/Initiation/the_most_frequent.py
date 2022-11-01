#!/usr/local/bin/checkio --domain=py run the-most-frequent


def count_up(word, word_list):
    return len([i for i in word_list if i == word])

def most_frequent(data: list) -> str:
    unique_data = set(data)
    result = ""
    count = 0
    for i in unique_data:
        if result == "":
            result = i
            count = count_up(i, data)
        else:
            temp = count_up(i, data)
            if temp > count:
                result = i
                count = temp
    return result

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
