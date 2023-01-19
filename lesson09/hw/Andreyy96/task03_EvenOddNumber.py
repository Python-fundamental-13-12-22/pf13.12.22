def check_odd_even(number):
    try:
        if int(number) % 2 == 0:
            print('Entered number is even')
        elif int(number) % 2 != 0:
            print('Entered number is odd')
    except ValueError:
        print('You entered not a number')


check_odd_even (24)     # output: 'Entered number is even'
check_odd_even (19)     # output: 'Entered number is odd'
check_odd_even('syty')  # output: 'You entered not a number'
check_odd_even('!')     # output: 'You entered not a number'
check_odd_even('6')     # output: 'Entered number is even'
