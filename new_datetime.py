# Day 16 of 30 day of python challengr
from datetime import date
from datetime import datetime

'''Get the current day, month, year, hour, minute and timestamp from datetime module'''

now = datetime.now()
print(now)
print('Current year:',  now.year)
print('Current month:', now.month)
print('Current day:', now.day)
print('Current time:', now.hour)
print('Current minute:', now.minute)
print('Current second:', now.second)
print('Current timestamp:', now.timestamp())

'''Format the current date using this format: "%m/%d/%Y, %H:%M:%S")'''
time = now.strftime('%m/%d/%Y, %H:%M:%S')
print(time)

'''Today is 5 December, 2019. Change this time string to time.'''
today = '5 December 2019'
today_to_time= datetime.strptime(today, '%d %B %Y')
print(today_to_time)

'''Calculate the time difference between now and new year.'''
today = date(year= 2022, month= 2, day = 16)
new_year = date(year= 2023, month=1, day = 1)
time_difference = new_year - today
print(time_difference)

'''Calculate the time difference between 1 January 1970 and now.'''
today = date(year= 2022, month= 2, day= 16)
few_year = date(year= 1970, month = 1, day= 1)
time_diff = today - few_year
print(time_diff)

