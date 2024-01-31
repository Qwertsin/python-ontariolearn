import time
import datetime
import random

f_text = random.randint(1, 4)
lucky_num = random.randint(1, 100)
today = datetime.date.today()
add_days = random.randint(1,365)

future_date = today + datetime.timedelta(days=add_days)




name = input('Please enter your name: ')
print('Welcome to the Fortune World!', name.upper())
time.sleep(2)
print('Are you ready to know your fortune, lucky number, and destiny date?')

time.sleep(2)

if f_text == 1:
    print('A great adventure awaits you right around the corner.')

if f_text == 2:
    print('Today is your day, JAS will give you 100% in the assignment.')

if f_text == 3:
    print('A smile is your power; make sure you use it today.')

if f_text == 4:
    print('Good things come to those who wait.')

print('Your Lucky Number is!', lucky_num)

print('You will meet a special person on the following date: ', future_date)