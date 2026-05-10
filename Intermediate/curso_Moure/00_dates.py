### dates ###

import datetime

from datetime import datetime

now = datetime.now()

print(now)

timestamp = now.timestamp()

fecha = now.fromtimestamp(timestamp)

print(timestamp)
print(fecha)




def print_date(date): 
    print(now.day)
    print(now.fold)
    print(now.microsecond)
    print(now.hour)
    print(now.month)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 2, 2)

print(year_2023)


from datetime import time

current_time = time(22, 55, 10)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year, current_date.month + 1, current_date.day ) 

print(current_date)

diff = year_2023 - now
print(diff)
diff= year_2023.date() - current_date
print(diff)


from datetime import timedelta

star_timedelta = timedelta(200, 100, 100, weeks= 10)

end_timedelta = timedelta (300, 100, 100, weeks= 13)

print(star_timedelta - end_timedelta)
print(star_timedelta + end_timedelta)
print(star_timedelta * end_timedelta)

