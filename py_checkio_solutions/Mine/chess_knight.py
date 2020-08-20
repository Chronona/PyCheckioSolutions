#!/usr/local/bin/checkio --domain=py run chess-knight


def check_movable(position, first, second):
    result = []
    x0 = position[0]
    y0 = position[1]
    for move_x in first:
        x = chr(ord(x0) + move_x)
        if x in list("abcdefgh"):
            for move_y in second:
                y = chr(ord(y0) + move_y)
                if y in list("12345678"):
                    result.append(x + y)
    return result


def move_knight(position):
    result = []
    result += check_movable(position, [-1, 1], [-2, 2])
    result += check_movable(position, [-2, 2], [-1, 1])
    return result


def chess_knight(start, moves):
    if moves == 1:
        return sorted(set(move_knight(start)))
    result = []
    result += move_knight(start)
    for i in move_knight(start):
        result += move_knight(i)
    return sorted(set(result))


if __name__ == "__main__":
    print("Example:")
    print(chess_knight("a1", 1))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight("a1", 1) == ["b3", "c2"]
    assert chess_knight("h8", 2) == [
        "d6",
        "d8",
        "e5",
        "e7",
        "f4",
        "f7",
        "f8",
        "g5",
        "g6",
        "h4",
        "h6",
        "h8",
    ]
    print("Coding complete? Click 'Check' to earn cool rewards!")

