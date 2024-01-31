"""
Assignment 3.
"""
##Place your import statements below this line
import datetime


def main():
    """
    Enter your code below. Ensure your code is within the body of the main() function.
    i.e. it is tabbed-in at least once.
    """

    """ Question 1: Name"""
    name = input('Please state your Name: ')  # Request name input from user

    """ Question 2: Sex"""
    sex = input('Please state your Sex. \n \'M\' for Male, \'F\' for Female, and \'N\' for Non-binary: ')
    sex = sex.upper()  # Turn key input into upper case
    try:
        sex_options = ('M', 'F', 'N')
        if sex not in sex_options:  # if sex variable is one of the 3 options then program continues
            raise ValueError  # This allows me to create a Value error to trip the except

    except ValueError:
        print('Incorrect option! PLease enter \'M\' for Male, \'F\' for Female, and \'N\' for Non-binary')
        exit()

    male = ('male', 'He', 'was', 'his')  # pronoun required in sentence based upon sex response
    female = ('female', 'She', 'was', 'her')
    non_binary = ('non-binary', 'They', 'were', 'their')

    """ Question 3: Date of Birth"""
    date_of_birth = input('Please input your date of birth \'YYYY-mm-dd\': ')
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')  # if date is in correct format then program continues
    except ValueError:
        print('Incorrect format, please enter date in \'YYYY-mm-dd\' format!')
        exit()

    today = datetime.datetime.today()  # obtain today's datetime
    age = (today - datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')).days / 365.25  # Age formula

    """ Question 4: Place/city of Birth"""
    place_of_birth = input('What city were you born within?: ')

    """ Question 5: SIN # """
    sin = int(input('Please provide your SIN number \'12234567890\':'))  # takes sin as an integer

    """ Output based upon Sex declared"""

    if sex == 'M':
        print(
            f'{name} is a {int(age)} year old {male[0]}. {male[1]} {male[2]} born in {place_of_birth} and {male[3]} SIN # is {sin}.')

    if sex == 'F':
        print(
            f'{name} is a {int(age)} year old {female[0]}. {female[1]} {female[2]} born in {place_of_birth} and {female[3]} SIN # is {sin}.')

    if sex == 'N':
        print(
            f'{name} is a {int(age)} year old {non_binary[0]}. {non_binary[1]} {non_binary[2]} born in {place_of_birth} and {non_binary[3]} SIN # is {sin}.')

    # This comment is within the body of the main() function.


# This comment is NOT within the body of the main() function.

# Do not edit below
if __name__ == '__main__':
    main()
