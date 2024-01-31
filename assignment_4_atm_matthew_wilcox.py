# assignment 4 atm

personal_pin = '1234'
attempts = 3
balance = 1000000000

while attempts > 0:  # loop while attempts greater than 0
    pin_attempted = input(f'Please enter your PIN ({attempts}) attempts remaining: ')  # get user PIN input attempt
    if pin_attempted == personal_pin:   # if PIN matches personal PIN
        print(f'Your account balance is: ${balance:,.2f}. Goodbye!')    # print balance output
        break   # end loop if correct PIN entered
    else:
        print('Invalid Pin.')
        attempts = attempts - 1  # reduce tries by 1
    if attempts == 0:
        print('Account is locked. The police is on its way.')   # 3 wrong tries output

