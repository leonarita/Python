print('Welcome to Bank ATM')

restart = ('Y')
chances = 3
balance = 999.12

while chances >= 0:
    pin = int(input('Please enter you 4 digit pin: '))

    if pin == 1234:
        print('You entered you pin correctly')
        print('Please Press 1 for your balance')
        print('Please Press 2 to make a withdrawl')
        print('Please Press 3 to pay in')
        print('Please Press 4 to return card \n')

        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 for your balance')
            print('Please Press 2 to make a withdrawl')
            print('Please Press 3 to pay in')
            print('Please Press 4 to return card')
            option = int(input('What would you like to choose? '))

            if option == 1:
                print('Your balance is $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you!')
                    break

            elif option == 2:
                option2 = ("y")

                withdrawl = float(input('How much would you like to withdraw? '
                                        '10, 20, 40, 60, 80, 100 for other enter 1: '))

                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('\nYour balance is now $', balance)
                    restart = input('Would you like to go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank you!')
                        break
                    elif withdrawl != [10, 20, 40, 60, 80, 100]:
                        print('Invalid amount, please re-entry\n')
                    elif withdrawl == 1:
                        withdrawl = float(input('Please enter desired amount'))

            elif option == 3:
                Pay_in = float(input('How much would you like to pay in?'))
                balance += Pay_in
                print('\nYour balance is now $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you!')
                    break

            elif option == 4:
                print('Please wait whilst your card is returned... \n')
                print('Thank you for you service')
                break

            else:
                print('Please enter a correct number. \n')
                restart = ('y')

    elif pin != ('1234'):
        print('Incorrect password')
        chances -= 1
        if chances == 0:
            print('\nNo more trie')
            break