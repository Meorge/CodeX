from datetime import datetime
now = datetime.now()

if now.month == 1:
    this_month = "January"
if now.month == 2:
    this_month = "February"
if now.month == 3:
    this_month = "March"
if now.month == 4:
    this_month = "April"
if now.month == 5:
    this_month = "May"
if now.month == 6:
    this_month = "June"
if now.month == 7:
    this_month = "July"
if now.month == 8:
    this_month = "August"
if now.month == 9:
    this_month = "September"
if now.month == 10:
    this_month = "October"
if now.month == 11:
    this_month = "November"
if now.month == 12:
    this_month = "December"


this_day = str(now.day)
this_year = str(now.year)
date = '%s/%s/%s' % (now.month, now.day, now.year)
time = '%s:%s:%s' % (now.hour, now.minute, now.second)
print("Today is " + this_month + " " + this_day + ", " + this_year + ". The time is " + time + ".")