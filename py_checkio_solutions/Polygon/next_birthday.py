#!/usr/local/bin/checkio --domain=py run next-birthday

# You have to write a function that receives a "today" date and a dictionary of family birthdates,    and for the person(s) whose birthday is next (today or later),    return the number of days between "today" and that birthday, and the age they will be.
#
# Note about leap days:If someone is born on February 29th, then he or she will    celebrate birthdays on March 1st when necessary.
#
# Input:two arguments:a tuple of three integers (year, month, day) representing a datea dictionary: keys are string and values are dates.Output:an integer and a dictionary (keys are string and values are integers).
#
#
# END_DESC
#%%

from typing import Dict, Tuple
import datetime

Date = Tuple[int, int, int]


def next_birthday(
    today: Date, birthdates: Dict[str, Date]
) -> Tuple[int, Dict[str, int]]:
    birthdates = dict(sorted(birthdates.items(), key=lambda x: x[1][1]))
    start = today[1]
    closest_birthday = ""
    while closest_birthday == "":
        for parson in birthdates:
            if (
                birthdates[parson][1:3] == (2, 29)
                and today[0] % 4 != 0
                and today[1:3] == (3, 1)
            ):
                return (0, {parson: today[0] - birthdates[parson][0]})
            if birthdates[parson][1] == start:
                print(parson)
                closest_birthday = parson
                bd = birthdates[closest_birthday]
                dt1 = datetime.datetime(year=today[0], month=bd[1], day=bd[2])
                dt2 = datetime.datetime(year=today[0], month=today[1], day=today[2])
                dt = dt1 - dt2
                if dt.days >= 0:
                    break
                else:
                    closest_birthday = ""
        start += 1
        if start > 12:
            start = 1
    return (dt.days, {closest_birthday: today[0] - bd[0]})


if __name__ == "__main__":
    FAMILY = {
        "Brian": (1967, 5, 31),
        "Léna": (1970, 10, 3),
        "Philippe": (1991, 6, 15),
        "Yasmine": (1996, 2, 29),
        "Emma": (2000, 12, 25),
    }

    TESTS = [
        ((2020, 9, 8), (25, {"Léna": 50})),
        ((2021, 10, 4), (82, {"Emma": 21})),
        ((2022, 3, 1), (0, {"Yasmine": 26})),
    ]

    for nb, (day, answer) in enumerate(TESTS, 1):
        user_result = tuple(next_birthday(day, FAMILY.copy()))
        if user_result != answer:
            print(f"You failed the test #{nb}.")
            print(f"Your result: {user_result}")
            print(f"Right result: {answer}")
            break
    else:
        print('Well done! Click on "Check" for real tests.')
# %%
FAMILY = {
    "Brian": (1967, 5, 31),
    "Léna": (1970, 10, 3),
    "Philippe": (1991, 6, 15),
    "Yasmine": (1996, 2, 29),
    "Emma": (2000, 12, 25),
}
[i for i in FAMILY.values()]
# %%
next_birthday(
    [2014, 3, 29],
    {
        "Emilie": [1990, 7, 31],
        "Jean-Baptiste": [1985, 6, 3],
        "Cameron": [1995, 11, 12],
        "Mia": [1999, 4, 5],
        "Elena": [1980, 1, 8],
        "Alexei": [1993, 10, 28],
        "Youssef": [1992, 4, 5],
        "Soraya": [1996, 12, 27],
        "Jiao": [1988, 2, 29],
        "Kang": [2012, 8, 15],
        "Pedro": [1959, 5, 2],
        "Manuela": [1961, 3, 18],
        "Inaya": [1968, 9, 22],
        "Moussa": [1976, 2, 29],
    },
)
# [7,{"Mia":15,"Youssef":22}]
# %%
