

print('Question_1:- Print the following variables as a concatenated string using the "old-style" formatting. The result should be "Hello World".')
print('word1 = "Hello"')
print('word2 = "World"')

word1 = "Hello"
word2 = "World"

print('\n%s %s\n' % (word1, word2))
    
print('Question_2:- Print the following variables as a concatenated string\n using the "new-style" formatting. The result should be "Hello World".')
print('word1 = "Hello"')
print('word2 = "World"')

print('\n{} {}\n'.format(word1, word2))

print('Question_3:- Print the following variables as a concatenated string using an f-string. The result should be "Hello World".')
print('word1 = "Hello"')
print('word2 = "World"')

print(f'\n{word1} {word2}\n')

print('Question_4:- Print the following variable 1234.9 as a dollar currency value.')
print('It should be prepended by the $ symbol and have 2   decimal places.')
print('amount = 1234.9')

amount = 1234.9
print(f'\n${amount:.2f}\n')

print('Question_5    Print the following variable as a percentage value (i.e. 25%).')
print('value = 0.25')

value = 0.25
print(f'\n{value:.0%}\n')

print('Question_6:-    Print the following as a string including the positive sign.')
print('value = 1234')

value = 1234
print(f'\n{value:+}\n')
   
print('Question_7:-    Print the following value as a dollar currency value including')
print('comma separators. (E.g. $123,567,90.00)')
print('amount = 29430435872349.3283')

amount = 29430435872349.3283
print(f'\n${amount:,}\n')
    
print('Question_8 :-    Print the following integer as a North American telephone')
print('number (e.g. (xxx) xxx-xxxx)')
print('number = 4165551234')

number = 4165551234
print(f'\n({str(number)[:3]}) {str(number)[3:6]}-{str(number)[6:]}\n')

print('Question_9:-    Print the following integer with leading zeros so that   it occupies 4 characters (e.g. 0001)')
print('number = 72')
number = 72

print(f'\n{number:04}\n')

print('Question_10:- Print a string which repeats the * character exactly 50 times.')

x = '*'
print(f'\n{x:*^50}\n')

print('Question_11:-Print the phrase "Hello World" centered within a series of *')
print('characters. The total length of the string should be 79 characters.')
print('E.g. *** Hello World ***')

word3 = 'Hello World'
print(f'\n{word3:*^79}\n')

print("Question_12:-Print today's date in the following format: Nov 01, 2022")

from datetime import date

today = date.today()
print(today.strftime('\n%b %d, %Y\n'))

print("Question_13:-    Print today's date in the following format: November 01, 2022")

print(today.strftime('\n%B %d, %Y\n'))

print("Question_14:-    Print the today's date in the following format: YYYY-MM-DD format.")

print('')
print(today)
print('')

print('Question_15:-    Print the current time in 24 hour format with seconds.')
print('(i.e. 23:21:03)')

from datetime import datetime

time =datetime.now()
print(time.strftime('\n%H:%M:%S\n'))


print('Question_16:- Print the current time using AM/PM (e.g 01:34 PM)')

print(time.strftime('\n%I:%M:%S%p\n'))

print("Qestion_17:-Print tomorrow's weekday name ")
#('.e. if today is Friday,tomorrow is Saturday')

from datetime import timedelta
tomorrow = date.today() + timedelta(days=1)
print(tomorrow.strftime('\n%A\n'))

print('Question_18:- Using the strptime function, print the following string')
print('as a date object.')
print("'my_date = '2014-12-20'")

my_date = '2014-12-20'

date_obj = datetime.strptime(my_date, '%Y-%m-%d').date()
print('')
print(date_obj)
print('')

print('Question_19:-  Using the strptime function, convert and print the following')
print('as a datetime object.')
print("my_datetime = '2014-12-20 23:12'")

my_datetime = '2014-12-20 23:12'
datetime_obj = datetime.strptime(my_datetime, '%Y-%m-%d %H:%M')
format_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M')

print('')
print(format_datetime)
print('')

print('Question_20:-  Subtract 5 hours from the current datetime and print.')

current_datetime = datetime.now()
modified_datetime = current_datetime - timedelta(hours=5)
print('')
print(modified_datetime)
print('')

print('Question_21:-    Add 7 days to the current datetime and print.')

modified_datetime = current_datetime + timedelta(days=7)
print('')
print(modified_datetime)
print('')

print('Question_22:-    Print the following string as a date object. Assume that')
print('a week begins on a Sunday.')
print("'my_date = 'Day 2 of week 23, 2020'")

#unsure how to do this one....
#my_date = 'Day 2 of week 23, 2020'
#datetime.strftime(my_date, 'Day %d of week %w, %Y')
#print(my_date(2,23,2020))

print('')
print('')


print('Question_23:- Print the last three characters of the following string.')
print("alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('')
print(alphabet[-3:])
print('')
    
print('Question_24:-Print the current date and time in ISO-8601 format.')

print('')
print(current_datetime.isoformat())
print('')

print("Question_25:-Using today's date, how many days have elapsed since the")
print('beginning of the year? (e.g. If today is Jan 3, there would')
print('be 2 days). Return as an integer.')

current_date = date.today()

days_elapsed = current_date - date(2023,1,1)

print('')
print(days_elapsed.days)
print('')


print('Question_26:-How much time is left this year? Print a timedelta')

time_left = datetime(2024, 1,1,0,0,0) - datetime.today()

print('')
print(time_left)
print('')

print('Question_27:-How many seconds are left this year? Return an integer.')
  #'(Hint: look for a helper function on timedelta)')

seconds_left = datetime(2024, 1,1,0,0,0) - datetime.today()

print('')
print(int(seconds_left.total_seconds()))
print('')

print("Question_28:- Print today's year, month and day")

print('')
print(date.today().year)
print(date.today().month)
print(date.today().day)


