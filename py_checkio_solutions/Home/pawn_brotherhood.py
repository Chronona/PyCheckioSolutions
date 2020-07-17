#!/usr/local/bin/checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns: set) -> int:
    result = 0
    x = list("abcdefghi")
    y = list(str(123456789))
    pawns = list(pawns)
    dict = {}
    for i in range(len(pawns)):
        pawn = list((str(pawns[i])))
        dict[i] = pawn
    print(dict)
    for i in dict:
        i = dict[i]
        pawn_x = x.index(i[0])
        pawn_y = y.index(i[1])
        try:
            x1 = x[pawn_x - 1]
        except IndexError:
            x1 = None
        try:
            y1 = y[pawn_y - 1]
        except IndexError:
            y1 = None
        try:
            x2 = x[pawn_x + 1]
        except IndexError:
            x2 = None
        safe_position1 = [x1, y1]
        safe_position2 = [x2, y1]
        for i in dict.values():
            if safe_position1 == i or safe_position2 == i:
                result += 1
                print(i)
                break
    return result