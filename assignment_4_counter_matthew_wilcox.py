
# assignment 4 counter

print('Hello')

# Start Value
while True:
    try:
        start_value = input('Enter a start value (Default: 0): ')  # receive string input
        if start_value:  # if not empty
            start_int = int(start_value)  # turn into integer
        else:
            start_int = 0  # default value 0
        break

    except ValueError:
        print('Please enter number characters only')

    # End Value
while True:
    try:
        end_int = int(input('Enter an end value greater than your start value: '))
        if end_int > start_int:  # if end_int is indeed an integer and greater then break
            break
        else:
            print('Incorrect value entered. Please insert a number greater than start value: ')

    except ValueError:
        print('Incorrect value entered. Please insert a number greater than start value: ')

    # Step Value
while True:
    try:
        step_value = input(
            'Enter a step value which should be no larger than the difference between the start and end value('
            'Default: 1): ')
        if step_value and step_value != '0':  # if step_value not empty and not equal to string 0
            step_int = int(step_value)
        else:
            step_int = 1
        if abs(step_int) <= abs(end_int - start_int):  # if absolute step interval is less than or equal to difference
            # of end less start
            break
        else:
            print(
                f'Step value should be no larger than the difference between start and end ({abs(end_int - start_int)})'
                '. Please enter again.')    # tell reader number is too big than difference
    except ValueError:
        print('Incorrect value. Please enter a valid number.')

    # interval counting

for i in range(start_int, end_int + 1, step_int):   # loop through all numbers including last number
    print(i, end=" ")   # no line break print number

print('\nYour sequence has been completed. Thank you!')
