#Video tutorial on datetime module.

from datetime import datetime

birthday = datetime(1987, 6, 13, 8, 30, 13)

print(birthday.year)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday)

datetime.now

print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now() - datetime(2018, 1, 1))

parsed_date = datetime.strptime("Jan 15, 2018", "%b %d, %Y")

print(parsed_date.month)

parsed_date2 = datetime.strptime("Jul 04, 2011", "%b %d, %Y")

print(parsed_date2.year)
print(parsed_date2.month)

date_string = datetime.strftime(datetime.now(), "%b, %d, %Y")

print(date_string)