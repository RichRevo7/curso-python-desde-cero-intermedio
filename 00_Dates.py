### Dates ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2026 = datetime(2026, 1, 1)

print_date(year_2026)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

corrent_date = date.today()

print(corrent_date.year)
print(corrent_date.month)
print(corrent_date.day)

corrent_date = date(2025, 1, 8)
print(corrent_date.year)
print(corrent_date.month)
print(corrent_date.day)

corrent_date = date(corrent_date.year, corrent_date.month + 1, corrent_date.day)

print(corrent_date.month)

diff = year_2026 - now
print(diff)

diff = year_2026.date() - corrent_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)