"""
practice_week6.py

This activity you have to print a picture that looks like an envelope"""

first = 'Matthew'
last = 'Wilcox'

print('+---------------------------------------------+')
print('|                                        #### |')
print('|                                        #### |')
print('|                                        #### |')
print('|                                             |')
print('|                                             |')
print('|                       {} {}        |'.format(first, last))
print('|                       123 ABC Cres          |')
print('|                       Springfield, CA 1234  |')
print('|                                             |')
print('+---------------------------------------------+')

'''concatenating strings, 4 methods'''

print(first + ' ' + last)
print('%s %s' % (first, last))
print('{} {}'.format(first, last))
print(f'{first} {last}')

''' format a number as a percentage value'''

x = 5 / 6
print(f'{x:%}')
''' print a 16 digit number that only displays the last 4 digits'''
y = '0123456789012345'
print(f'************{y[:4]}')

''' format 1876543.32 to $1,876,543.32'''
z = 1876543.32
print(f'${z:,}')

''' convert A1B2C3 to postal code A1B 2C3'''
postal_code = 'A1B2C3'
print(f'{postal_code[:3]} {postal_code[3:]}')

''' convert 10 digits into a phone number'''
phone = 9059871234
print(f'({str(phone)[:3]}) {str(phone)[3:6]}-{str(phone)[6:]}')
