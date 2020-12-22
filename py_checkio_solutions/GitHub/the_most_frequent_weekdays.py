#!/usr/local/bin/checkio --domain=py run the-most-frequent-weekdays


import datetime
from calendar import monthrange

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def count_day(count_list, year, month, day_num, kinds_of_day):
    if datetime.datetime(int(year), int(month), day_num + 1).weekday() == kinds_of_day:
        count_list[kinds_of_day] += 1


def most_frequent_days(a):

    count_list = [0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 13):
        year = a
        month = i
        day, last_day = monthrange(int(year), int(month))
        for day_num in range(last_day):
            for j in range(0, 7):
                count_day(count_list, year, month, day_num, j)
    the_most_frequent_day = [
        i for i, v in enumerate(count_list) if v == max(count_list)
    ]
    return [i for i in weekdays if weekdays.index(i) in the_most_frequent_day]


if __name__ == "__main__":
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ["Tuesday", "Wednesday"]
    assert most_frequent_days(1167) == ["Sunday"]
    assert most_frequent_days(1216) == ["Friday", "Saturday"]
    assert most_frequent_days(1492) == ["Friday", "Saturday"]
    assert most_frequent_days(1770) == ["Monday"]
    assert most_frequent_days(1785) == ["Saturday"]
    assert most_frequent_days(212) == ["Wednesday", "Thursday"]
    assert most_frequent_days(1) == ["Monday"]
    assert most_frequent_days(2135) == ["Saturday"]
    assert most_frequent_days(3043) == ["Sunday"]
    assert most_frequent_days(2001) == ["Monday"]
    assert most_frequent_days(3150) == ["Sunday"]
    assert most_frequent_days(3230) == ["Tuesday"]
    assert most_frequent_days(328) == ["Monday", "Sunday"]
    assert most_frequent_days(2016) == ["Friday", "Saturday"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
