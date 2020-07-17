#!/usr/local/bin/checkio --domain=py run when-is-friday

# Friday is an awesome day. It's the end of the week after which you can just relax and attend to all of the things you've been pushing away. It's really good to know how many days you still have to wait, isn't it?
# 
# Your task is to write a function that will count how many days are left from a certain date to Friday. The argument will be a particular date in a string format looking like this: 'dd.mm.yyyy', where 'dd' - day, 'mm' - month, and 'yyyy' - year.
# For example, if that given day is Thursday, then the answer will be 1. If that day is Monday, the result is 4. And if that day is Friday, the function should return 0.
# 
# 
# 
# Input:Date as a string.
# 
# Output:The amount of days left until Friday.
# 
# Precondition:
# 1<= year<= 3000
# 
# 
# END_DESC

import datetime


def friday(day):
    day = day.split(".")
    dd = int(day[0])
    mm = int(day[1])
    yyyy = int(day[2])
    week_day = datetime.datetime(yyyy, mm, dd).weekday()
    if week_day <= 4:
        return 4-week_day
    if week_day == 5:
        return 6
    if week_day == 6:
        return 5