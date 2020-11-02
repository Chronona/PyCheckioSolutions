#!/usr/local/bin/checkio --domain=py run how-deep


def how_deep(structure):
    structure = "".join([i for i in str(structure) if i == "(" or i == ")"])
    count = 0
    while "()" in structure:
        structure = structure.replace("()", "")
        count += 1
    return count


if __name__ == "__main__":
    print("Example:")
    print(how_deep((1, 2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
