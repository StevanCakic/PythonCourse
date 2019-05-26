import datetime
# Prvi dio
# Sta ako nazovete fajl kao modul?
'''
print(dir(datetime))
# print(help(datetime.date))

gvr = datetime.date(1951, 1, 31)

print(gvr)
print(type(gvr))

print(gvr.day)
print(gvr.month)
print(gvr.year)

second_mill = datetime.date(2000, 1, 1)
# Kako da vidim koji ce biti datum za 100 dana
dt = datetime.timedelta(100)

print(second_mill + dt)

# Šta misliti kako biste vidjeli koje je datum bio prije 100 dana u odnosu na 1.1.2000.
# TODO

'''
# Drugi dio
# Formatiranje datuma
# Otvorimo dokument gdje se nalaze formati za datume
'''
gvr = datetime.date(1951, 1, 31)
# Day name, Month name Day-#, Year

# old way
print(gvr.strftime("%A, %B %d, %Y"))

# new way
print("{:%A, %B %d, %Y}".format(gvr))

# Prva SpaceX reuse raketa lansiranja: 30. Marta 2017, 22:27 UTC
# Kako ovo da zabilježimo

# year, month, day
launch_date = datetime.date(2017, 3, 30)
print(launch_date)
# hour, minute, second, etc.
launch_time = datetime.time(22, 27, 0)
print(launch_time)
# kombinacija
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_datetime)

# mozete provjeriti min/max time i date, kao i resolution, tj. min razliku izmedju vremena
print(datetime.time.min)
print(datetime.date.max)

# Get current time:

now = datetime.datetime.now()
print(now)
print(now.microsecond)

sputnik = "10/4/1957"
moon_landing = "7/20/1969"

moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))

date_difference = now - moon_landing_datetime
print(date_difference.days)

# ali nema years i months, kako to da rijesimo
from dateutil.relativedelta import relativedelta
date_difference_years = relativedelta(now, moon_landing_datetime).years
print(date_difference_years)

'''