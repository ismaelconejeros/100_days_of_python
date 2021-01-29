import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1990, month=5, day=14, hour=16, minute=32)


print(date_of_birth)