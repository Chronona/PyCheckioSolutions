#!/usr/local/bin/checkio --domain=py run create-intervals


def create_intervals(data):
    if len(data) == 0:
        return []
    result = []
    output = [0, 0]
    for i in sorted(data):
        if output == [0, 0]:
            output = [i, i]
        elif output[1] + 1 == i:
            output[1] = i
        else:
            result.append(tuple(output))
            output = [i, i]
    result.append(tuple(output))
    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print("Almost done! The only thing left to do is to Check it!")