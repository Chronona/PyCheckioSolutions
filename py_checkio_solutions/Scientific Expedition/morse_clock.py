#!/usr/local/bin/checkio --domain=py run morse-clock

# 
# END_DESC

def checkio(time_string: str) -> str:
    time_string = time_string.split(":")
    for i, j in zip(time_string, range(3)):
        tens_place = int(i) // 10
        ones_place = int(i) - tens_place * 10
        if j == 0:
            tens_place_bin = format(tens_place, "b").zfill(2)
        else:
            tens_place_bin = format(tens_place, "b").zfill(3)
        ones_place_bin = format(ones_place, "b").zfill(4)
        tens_place_morse = "".join(["-" if i == "1" else "." for i in tens_place_bin])
        ones_place_morse = "".join(["-" if i == "1" else "." for i in ones_place_bin])
        if j == 0:
            hh = tens_place_morse + " " + ones_place_morse
        elif j == 1:
            mm = tens_place_morse + " " + ones_place_morse
        else:
            ss = tens_place_morse + " " + ones_place_morse
    return hh + " : " + mm + " : " + ss